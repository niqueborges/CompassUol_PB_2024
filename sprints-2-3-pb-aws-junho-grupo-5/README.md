# **Avaliação das Sprints 2 e 3 - Programa de Bolsas Compass UOL / AWS - Turma JUNHO/2024** 📝

## **👥 Desenvolvedores**

Este repositório foi desenvolvido por um grupo de alunos participantes do **Programa de Bolsas Compass UOL 2024**. As contribuições de todos os membros do grupo foram essenciais para a realização dos projetos e para o aprendizado coletivo. Entretanto, esta branch irá refatorar o projeto para ser usado localmente sem AWS.

- **Gerson Ramos**
- **Iuri Souza**
- **Monique da Silva Borges** (Quem refatorou)

---

# **Projeto NBA API** 🏀

*Sistema em JavaScript/NodeJS que produz uma interface para consulta de API pública.*

## **📑 Índice**

1. [📂 Estrutura do Projeto](#-estrutura-do-projeto)
2. [🛠️ Tecnologias Utilizadas](#️-tecnologias-utilizadas)
3. [📁 Estrutura de Diretórios](#-estrutura-de-diretórios)
4. [💻 Funcionalidades](#-funcionalidades)
5. [🚀 Como Usar](#-como-usar)
6. [🛠️ Etapas do Projeto](#-etapas-do-projeto)
7. [😓 Dificuldades](#-dificuldades)
8. [📜 Licença](#-licença)

---

## **📂 Estrutura do Projeto**

- `index.html`: Contém a estrutura HTML do sistema.
- `team.html`: Página de exibição de detalhes e estatísticas de um time.
- `script.js`: Script para manipular a interface do usuário e interagir com a API.
- `team.js`: Script específico para lidar com a página de detalhes do time.
- `style.css`: Contém a estilização do sistema.
- `index.js`: Código de servidor Node.js que gerencia as requisições para a API.
- `routes/nbaRoutes.js`: Define as rotas para acesso à API NBA.
- `Dockerfile`: Define como construir a imagem Docker da aplicação.
- `docker-compose.yml`: Facilita o gerenciamento dos contêineres Docker.
- `README.md`: Este arquivo contém informações sobre o projeto, como usá-lo e sua estrutura.

---

## **🛠️ Tecnologias Utilizadas**

- ![HTML5 Badge](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
- ![CSS Badge](https://img.shields.io/badge/CSS-239120?&style=for-the-badge&logo=css3&logoColor=white)
- ![JavaScript Badge](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=white)
- ![Node.js Badge](https://img.shields.io/badge/Node.js-43853D?style=for-the-badge&logo=node.js&logoColor=white)
- ![Docker Badge](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

---

## **📁 Estrutura de Diretórios**

Este repositório contém o código-fonte do projeto **NBA API**:

```plaintext
├── CompassUol_PB_2024/
│   ├── assets/
│   │   └── logo-compass.png
│   ├── sprint-1-pb-aws-junho-Monique-Borges/
│   ├── sprints-2-3-pb-aws-junho-grupo-5/
├── README.md
├── .gitignore
```

---

## **💻 Funcionalidades**

- Consulta de dados da API pública da NBA.
- Exibição dos dados em uma interface simples e interativa.
- Dockerização da aplicação para fácil execução local.
- Implementação de API utilizando Node.js.

---

## **🚀 Como Usar**

1. **Clonar o Repositório**:

   Clone o repositório em sua máquina local:

   ```bash
   git clone -b grupo-5 https://github.com/Compass-pb-aws-2024-JUNHO/sprints-2-3-pb-aws-junho.git
   cd sprints-2-3-pb-aws-junho/src
   ```

2. **Configurar a Chave da API**:

   Obtenha uma chave de API na [RapidAPI](https://rapidapi.com/api-sports/api/api-nba) e adicione-a no arquivo `routes/nbaRoutes.js` na `const API_KEY`.

3. **Configurar Docker (opcional)**:

   Se ainda não tiver o Docker instalado, siga as instruções em [docker.com](https://www.docker.com/get-started) para instalação.

4. **Iniciar a Aplicação Localmente com Docker**:

   Execute os seguintes comandos para subir a aplicação com Docker:

   ```bash
   docker-compose up
   ```

   Acesse a aplicação no navegador usando o endereço `http://localhost:3000/`.

5. **Escolher um Time**:

   Na página principal, selecione um time na lista de times disponíveis.

6. **Verificar Estatísticas do Time**:

   Ao escolher um time, você será direcionado para uma página que exibe as estatísticas e os jogadores do time na temporada selecionada.  
   Você pode alterar a temporada usando o menu suspenso para ver as estatísticas e jogadores de anos diferentes.

7. **Botão de Voltar**:

   Utilize o botão de voltar para retornar à página de seleção de times.

---

## **🛠️ Etapas do Projeto**

1. **Planejamento e Design**:
   - Definição das funcionalidades principais e planejamento da interface do usuário.
   - Criação de wireframes para mapear o fluxo da aplicação.

2. **Desenvolvimento da API**:
   - Implementação da API em Node.js para consumir dados da API pública da NBA.
   - Criação das rotas necessárias para servir os dados ao cliente.

3. **Desenvolvimento Frontend**:
   - Criação da interface do usuário utilizando HTML, CSS e JavaScript.
   - Implementação das interações com a API via RapidAPI.

4. **Dockerização e Execução Local**:
   - Configuração de `Dockerfile` e `docker-compose.yml` para contêineres Docker.
   - Execução da aplicação localmente.

5. **Teste e Validação**:
   - Testes funcionais e de usabilidade para garantir a experiência do usuário.
   - Ajustes baseados no feedback dos testes.

---

## **😓 Dificuldades**

- **CORS**: Configuração de CORS para permitir requisições de origens diferentes.
- **Permissões de Docker**: Problemas com permissões ao executar Docker localmente.
- **Depuração de Erros**: Integração com a API da NBA e depuração de erros nas rotas.

---

## **📜 Licença**

Licença MIt

---