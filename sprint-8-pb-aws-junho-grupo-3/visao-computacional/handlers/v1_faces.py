import json
import os
import boto3
import logging
from botocore.exceptions import ClientError
from dotenv import load_dotenv
from extractors.date import format_date

# Carrega as variáveis do arquivo .env
load_dotenv()

# Configuração do logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Inicializa o cliente Rekognition
rekognition = boto3.client("rekognition", region_name='us-east-1')


def detect_faces(bucket_name: str, image_name: str) -> dict:
    """Detecta faces em uma imagem armazenada no S3 usando o AWS Rekognition."""

    if not bucket_name or not image_name:
        logger.error("Nome do bucket ou da imagem não pode ser vazio.")
        return {"error": "Nome do bucket ou da imagem não pode ser vazio."}

    try:
        # Inclui o caminho da pasta na chave da imagem
        full_image_path = f"{os.getenv('FOLDER_NAME')}/{image_name}"
        response = rekognition.detect_faces(
            Image={"S3Object": {"Bucket": bucket_name, "Name": full_image_path}},
            Attributes=["ALL"]
        )
        logger.info("Resposta do Rekognition recebida com sucesso.")
    except ClientError as e:
        logger.error("Erro ao chamar a API Rekognition: %s", e)
        return {"error": "Erro ao chamar a API Rekognition", "message": str(e)}

    if not response.get("FaceDetails"):
        logger.warning("Nenhuma face detectada na imagem.")
        return [{"position": {"Height": None, "Left": None, "Top": None, "Width": None}, "classified_emotion": None, "classified_emotion_confidence": None}]

    return process_faces(response["FaceDetails"])


def process_faces(face_details):
    """Processa as faces detectadas e retorna as informações formatadas."""
    face_data = []

    for face in face_details:
        emotions = face.get("Emotions", [])
        max_emotion = max(emotions, key=lambda e: e["Confidence"], default={"Type": None, "Confidence": 0})
        
        face_info = {
            "position": face["BoundingBox"],
            "classified_emotion": max_emotion["Type"],
            "classified_emotion_confidence": max_emotion["Confidence"]
        }

        face_data.append(face_info)

    logger.info("Processamento concluído. Total de faces detectadas: %d", len(face_data))
    return face_data


def v1_vision(event, context):
    """Função que processa a solicitação para analisar as imagens."""
    try:
        # Extrai e valida o corpo da requisição
        body = json.loads(event.get('body', '{}'))
        bucket = body.get('bucket')
        image_name = body.get('imageName')  # Nome da imagem

        # Valida se os campos estão preenchidos
        if not bucket or not image_name:
            logger.error("Faltando o nome do bucket ou da imagem.")
            return create_response(400, {
                "error": "Faltando o nome do bucket ou da imagem."
            })

        # Verifica se o bucket é permitido
        if bucket != os.getenv('BUCKET_NAME'):
            logger.error("Bucket não permitido: %s", bucket)
            return create_response(403, "Bucket não permitido.")

        # Obtém o nome da pasta da variável de ambiente
        folder_name = os.getenv('FOLDER_NAME')
        if not folder_name:
            logger.error("FOLDER_NAME não está definido nas variáveis de ambiente.")
            return create_response(500, "Erro interno: FOLDER_NAME não definido.")

        # Chama o AWS Rekognition para detectar faces
        result = detect_faces(bucket, image_name)

        # Prepara o caminho da imagem
        image_key = f"{folder_name}/{image_name}"
        image_url = f"https://{bucket}.s3.amazonaws.com/{image_key}"
        create_image = format_date()

        response = {
            "url_to_image": image_url,
            "created_image": create_image,
            "faces": result
        }

        logger.info("Response: %s", json.dumps(response))
        return {"statusCode": 200, "body": json.dumps(response, ensure_ascii=False, indent=2)}

    except json.JSONDecodeError:
        logger.error("JSON inválido no corpo da requisição.")
        return create_response(400, "JSON inválido no corpo da requisição.")
    except ClientError as e:
        logger.error(f"Erro ao chamar Rekognition: {e}")
        return create_response(500, "Erro ao chamar o serviço Rekognition.")
    except Exception as e:
        logger.error(f"Erro inesperado: {str(e)}")
        return create_response(500, "Erro interno do servidor")


def create_response(status_code, message):
    """Cria uma resposta padronizada."""
    if isinstance(message, dict):
        body = message
    else:
        body = {"message": message}
    return {
        "statusCode": status_code,
        "body": json.dumps(body)
    }
