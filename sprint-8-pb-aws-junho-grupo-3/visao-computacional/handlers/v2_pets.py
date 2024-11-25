import json
import logging
import os
from dotenv import load_dotenv
import boto3
import sys
from extractors.date import format_date
from handlers.v1_faces import detect_faces  # Importa a função correta que detecta faces

load_dotenv()

# Adiciona o diretório do projeto ao sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Configuração do logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Inicializa a sessão boto3 com credenciais do AWS CLI
session = boto3.Session()

rekognition = session.client("rekognition")
bedrock = session.client("bedrock-runtime")  # Cliente para Bedrock


def detect_labels(bucket: str, image_name: str) -> dict:
    """Detecta rótulos em uma imagem armazenada no S3 usando Rekognition."""
    image_path = f"{os.getenv('FOLDER_NAME')}/{image_name}"
    try:
        response = rekognition.detect_labels(
            Image={"S3Object": {"Bucket": bucket, "Name": image_path}},
            MaxLabels=10,
            MinConfidence=75,
        )
        return response
    except Exception as e:
        logger.error(f"Erro ao detectar rótulos: {str(e)}")
        return {"error": str(e)}

def generate_pastor_tips(labels: list) -> dict:
    """Gera dicas sobre cães pastores baseadas em rótulos detectados."""
    keywords = ["Animal", "Dog", "Cat", "Pet", "German Shepherd"]
    pastor_labels = []
    for label in labels:
        if label.get("Name") in keywords:
            pastor_labels.append(
                    {  
                        "Confidence": label.get("Confidence"),  
                        "Name": label.get("Name")
                    } 
                )

    logger.info(f"Rótulos filtrados: {pastor_labels}")

    if pastor_labels:
        raca_nome = pastor_labels[-1]["Name"]
        logger.info(f"Raça identificada: {raca_nome}")

        prompt = (
            f"Eu gostaria de Dicas sobre cães pastores como {raca_nome}. "
            "Por favor, forneça informações detalhadas seguindo a estrutura abaixo:\n"
            "Nível de Energia e Necessidades de Exercícios: \n"
            "Temperamento e Comportamento: \n"
            "Cuidados e Necessidades: \n"
            "Problemas de Saúde Comuns: \n"
        )

        native_request = {
            "inputText": prompt,
            "textGenerationConfig": {
                "maxTokenCount": 500,
                "temperature": 0.7,
                "topP": 0.9,
            },
        }

        logger.info(f"Enviando prompt ao Bedrock: {prompt}")

        try:
            response = bedrock.invoke_model(
                modelId="amazon.titan-text-express-v1",
                body=json.dumps(native_request),
            )

            model_response = json.loads(response["body"].read())
            bedrock_response = model_response["results"][0]["outputText"]

            logger.info(f"Resposta do Bedrock: {bedrock_response}")

            return [
                {
                "labels": pastor_labels,
                "Dicas": bedrock_response
                }
            ]

        except Exception as e:
            logger.error(f"Erro ao invocar o modelo: {e}")
            return {"error": str(e)}

    logger.warning("Nenhuma raça identificada.")
    return [{"labels": None, "Dicas": None}]


def v2_vision(event: dict, context) -> dict:
    """Processa a imagem e gera dicas sobre cães pastores."""
    try:
        # Extrai e valida o corpo da requisição
        body = json.loads(event.get('body', '{}'))
        bucket = body.get('bucket')
        image_name = body.get('imageName')  # Nome da imagem

        # Detecta emoções na imagem
        faces = detect_faces(bucket, image_name)
        logger.info("Rekognition response: %s", json.dumps(faces))

        # Detectando pets usando Rekognition (labels)
        rekognition_label_response = detect_labels(bucket, image_name)
        labels = rekognition_label_response.get("Labels", [])

        # Verifica se há cães pastores e gera dicas
        pastor_analysis = generate_pastor_tips(labels)

        create_image = format_date()
        
        if faces == [{"position": {"Height": None, "Left": None, "Top": None, "Width": None}, "classified_emotion": None, "classified_emotion_confidence": None}]:
            response = {
                "url_to_image": f"https://{bucket}.s3.amazonaws.com/{os.getenv("FOLDER_NAME")}/{image_name}",
                "created_image": create_image,
                "pets": pastor_analysis,
            }
        else:
            response = {
                "url_to_image": f"https://{bucket}.s3.amazonaws.com/{os.getenv("FOLDER_NAME")}/{image_name}",
                "created_image": create_image,
                "faces": faces,
                "pets": pastor_analysis,
            }

        logger.info("Response: %s", json.dumps(response))
        return {"statusCode": 200, "body": json.dumps(response, ensure_ascii=False, indent=2)}

    except ValueError as ve:
        logger.error(f"Valor inválido: {str(ve)}")
        return {"statusCode": 400, "body": json.dumps({"error": str(ve)})}
    except Exception as e:
        logger.error(f"Erro ao processar a imagem: {str(e)}")
        return {"statusCode": 500, "body": json.dumps({"error": "Falha ao processar a imagem"})}
