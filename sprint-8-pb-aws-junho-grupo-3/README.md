# **API Vision - Detecção de Emoções e Cães Pastores**
---

![Amazon Rekognition](https://img.shields.io/badge/Amazon%20Rekognition-FF9900?style=flat-square&logo=amazonaws&logoColor=white&labelColor=black)
![Amazon Bedrock](https://img.shields.io/badge/Amazon%20Bedrock-00A3E0?style=flat-square&logo=amazonaws&logoColor=white&labelColor=black)
![Amazon S3](https://img.shields.io/badge/Amazon%20S3-569A31?style=flat-square&logo=amazonaws&logoColor=white&labelColor=black)
![Amazon CloudWatch](https://img.shields.io/badge/Amazon%20CloudWatch-FF9900?style=flat-square&logo=amazonaws&logoColor=white&labelColor=black)
![Python 3.9](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white&labelColor=black)
![Serverless Framework](https://img.shields.io/badge/Serverless%20Framework-0B9C48?style=flat-square&logo=serverless&logoColor=white&labelColor=black)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white&labelColor=black)

---

## **👥 Desenvolvedores**
| [<img loading="lazy" src="https://avatars.githubusercontent.com/u/69771619?v=4" width="115" alt="Carlos Altomare Catao">](https://github.com/CarlosCatao) <br>[Carlos Altomare Catao](https://github.com/CarlosCatao) | [<img loading="lazy" src="https://avatars.githubusercontent.com/u/130758430?v=4" width="115" alt="Hugo Bessa Susini Ribeiro">](https://github.com/hsusini) <br>[Hugo Bessa Susini Ribeiro](https://github.com/hsusini) | [<img loading="lazy" src="https://avatars.githubusercontent.com/u/165324231?v=4" width="115" alt="Paulo Henrique de Oliveira Carvalho">](https://github.com/Paulo-Henrique06) <br>[Paulo Henrique de Oliveira Carvalho](https://github.com/Paulo-Henrique06) | [<img loading="lazy" src="https://avatars.githubusercontent.com/u/95103547?v=4" width="115" alt="Monique da Silva Borges">](https://github.com/niqueborges) <br>[Monique da Silva Borges](https://github.com/niqueborges) |
|:---:|:---:|:---:|:---:|

---

## **📑 Índice**

- [📈 Status do Projeto](#-status-do-projeto)
- [✨ Funcionalidades](#-funcionalidades)
- [⚙️ Arquitetura e Fluxo de Trabalho](#-arquitetura-e-fluxo-de-trabalho)
- [⚙️ Variáveis de Ambiente](#⚙️-variáveis-de-ambiente)
- [📦 Como Rodar a Aplicação](#-como-rodar-a-aplicação)
- [🚀 Deploy](#-deploy)
- [💻 Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [📂 Estrutura de Diretórios](#-estrutura-de-diretórios)
- [📐 Padrões Utilizados](#-padrões-utilizados)
- [📅 Metodologia de Desenvolvimento](#-metodologia-de-desenvolvimento)
- [😿 Principais Dificuldades](#-principais-dificuldades)
- [📝 Licença](#-licença)

---

## **📈 Status do Projeto**

🚀 **Status**: Concluido

Este projeto visa desenvolver uma **API de Visão Computacional**, utilizando serviços da **AWS** para analisar emoções em imagens e identificar cães pastores. As principais tecnologias envolvem o **Amazon Rekognition** para análise de imagens e o **Amazon Bedrock**.

---

## **✨ Funcionalidades**

1. **Análise de Emoções em Imagens**:
   - A API recebe o nome de uma imagem e verifica, através do **Amazon Rekognition**, as emoções predominantes detectadas nas faces presentes.

2. **Detecção de Pets e Geração de Dicas**:
   - A API também permite a identificação de pets na imagem e utiliza o **Amazon Bedrock** para gerar dicas sobre cuidados com o animal detectado, incluindo identificação de cães pastores.

3. **Monitoramento via CloudWatch**:
   - A API utiliza o **Amazon CloudWatch** para monitorar o uso, erros e logs.

---

## **⚙️ Arquitetura e Fluxo de Trabalho**

A arquitetura do projeto envolve os seguintes componentes:

1. **API Vision**:
   Exemplo de requisição POST para a rota `/v1/vision`:
   ```json
   {
     "bucket": "myphotos",
     "imageName": "test-happy.jpg"
   }
   ```

   Exemplo de resposta:
   ```json
   {
     "url_to_image": "https://myphotos/test-happy.jpg",
     "created_image": "02-02-2023 17:00:00",
     "faces": [
       {
         "position": {
           "Height": 0.0633,
           "Left": 0.1718,
           "Top": 0.7366,
           "Width": 0.1106
         },
         "classified_emotion": "HAPPY",
         "classified_emotion_confidence": 99.93
       }
     ]
   }
   ```

2. **Detecção de Pets e Dicas (v2)**:
   Exemplo de requisição POST para a rota `/v2/vision`:
   ```json
   {
     "bucket": "myphotos",
     "imageName": "labrador.jpg"
   }
   ```

   Exemplo de resposta:
   ```json
   {
     "url_to_image": "https://myphotos/labrador.jpg",
     "created_image": "02-02-2023 17:00:00",
     "faces": [
       {
         "position": {
           "Height": 0.0633,
           "Left": 0.1718,
           "Top": 0.7366,
           "Width": 0.1106
         },
         "classified_emotion": "HAPPY",
         "classified_emotion_confidence": 99.93
       }
     ],
     "pet_detected": true,
     "pet_advice": "Labradores são cães ativos; lembre-se de oferecer exercícios diários."
   }
   ```

---

## **⚙️ Variáveis de Ambiente**
As variáveis de ambiente necessárias para a execução incluem as credenciais da **AWS** (chave de acesso e chave secreta) e detalhes dos serviços configurados, como o **Amazon Rekognition** e **Bedrock**.

---

## **📦 Como Rodar a Aplicação**

### **Pré-requisitos**:
- **Serverless Framework** instalado.
- **Credenciais AWS** configuradas corretamente.

### **Passos**:

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/seu-projeto.git
   ```

2. **Criar o ambiente de desenvolvimento**:

   **Windows**:
   ```bash
   python -m venv vision-env
   .\vision-env\Scripts\activate.bat
   ```

   **Linux**:
   ```bash
   python -m venv env
   source env/bin/activate
   ```

3. **Instale o Serverless Framework**:
   ```bash
   npm install -g serverless
   ```

4. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Configurar as variáveis de ambiente**:
   ```bash
   export AWS_ACCESS_KEY_ID=your_access_key
   export AWS_SECRET_ACCESS_KEY=your_secret_key
   ```

6. **Execute o deploy da aplicação**:
   ```bash
   serverless deploy
   ```

7. **Verifique os endpoints gerados** e utilize as rotas `/v1/vision` e `/v2/vision` para realizar as análises.

8. **Teste a API localmente**:
   ```bash
   serverless invoke local --function v1Description
   ```

---

## **🚀 Deploy**
O deploy é realizado via **Serverless Framework**, que configura e gerencia os serviços AWS necessários. Isso irá criar a API no **API Gateway**, as funções no **Lambda** e configurar os buckets no **S3**.

---

## **💻 Tecnologias Utilizadas**
- **Amazon Rekognition**: Serviço de análise de imagens.
- **Amazon Bedrock**: Geração de respostas baseadas na presença de pets.
- **Amazon S3**: Armazenamento de imagens.
- **Amazon CloudWatch**: Monitoramento e logs da API.
- **Python 3.9**: Linguagem utilizada no desenvolvimento da aplicação.
- **Serverless Framework**: Orquestra o deploy dos serviços serverless.
- **Git**: Sistema de controle de versão para rastrear alterações e facilitar a colaboração.

---

## **📂 Estrutura de Diretórios**
```bash
SPRINT-8-pb-aws-junho/
├── assets/                         # Recursos como imagens e arquivos estáticos
├── visao-computacional/            # Diretório da API de Visão Computacional
│   ├── extractors/                 # Funções de extração de dados
│   │   └── date.py                 # Arquivo de extração de data
│   ├── handlers/                   # Manipuladores de requisições da API
│   │   ├── health.py               # Verificação de saúde da API
│   │   ├── v1_description.py       # Manipulador da descrição V1
│   │   ├── v1_faces.py             # Manipulador de faces V1
│   │   ├── v2_description.py       # Manipulador da descrição V2
│   │   └── v2_pets.py              # Manipulador de pets V2
│   ├── package-lock.json           # Lock das dependências Node.js
│   ├── package.json                # Configurações do Node.jspackage-lock.json
│   └── serverless.yml              # Arquivo de configuração Serverless
├── .gitignore                      # Arquivo de exclusões Git
├── License                         # Arquivo de licença
├── README.md                       # Documentação principal do projeto
└── requirements.txt                # Dependências Python para o projeto
```
---

## **📐 Padrões Utilizados**
- **Commits Semânticos**: Para manter um histórico claro e organizado.
- **RESTFul API**: Para comunicação entre os serviços.
- **Arquitetura Serverless**: Toda a aplicação utiliza serviços gerenciados pela AWS.
- **Python PEP8**: Segue os padrões de formatação de código Python.

---

## **📅 Metodologia de Desenvolvimento**
O desenvolvimento seguiu a metodologia **Ágil**, com as seguintes práticas:

1. **Sprints**: Ciclos de desenvolvimento com metas definidas.
2. **Daily Meetings**: Reuniões diárias para acompanhamento de progresso.
3. **Code Review**: Revisões de código regulares para garantir qualidade e coesão.

---


---

## **😿 Principais Dificuldades**
- Configuração de permissões para os serviços AWS.
- Integração dos logs do **CloudWatch** de forma eficiente.
- Ajuste da precisão do **Rekognition** para detecção de pets e emoções.

---

## **📝 Licença**
Este projeto está licenciado sob a licença MIT.

---


Este README foi estruturado conforme as melhores práticas recomendadas no Programa de Bolsas Compass UOL e AWS.
