# **📝 Sistema de Cadastro de Clientes com JavaScript**

![CompassUol](assets/logo-compass.png)

---

## **👥 Desenvolvedora**

- [Monique da Silva Borges](https://github.com/niqueborges)

---

## **📜 Descrição**

Este é um projeto simples e funcional de um sistema de cadastro de clientes utilizando HTML5, CSS3, JavaScript e localStorage. O projeto foi refatorado para melhorar a organização, eficiência e experiência do usuário.

---

## **📑 Índice**

1. 📜 [Descrição](#-descrição)  
2. 📂 [Estrutura](#-estrutura)  
3. 💻 [Tecnologias Utilizadas](#-tecnologias-utilizadas)  
4. 📁 [Estrutura de Diretórios](#-estrutura-de-diretórios)  
5. ⚙️ [Funcionalidades](#️-funcionalidades)  
6. 🚀 [Como Usar](#-como-usar)  
7. 🗓️ [Metodologia de Desenvolvimento](#️-metodologia-de-desenvolvimento)  
8. 📈 [Refatoração e Melhorias](#-refatoração-e-melhorias)  
9. 🤔 [Desafios Superados](#-desafios-superados)

---

## **📂 Estrutura**

- **index.html**: Contém a estrutura HTML do sistema e o formulário de cadastro.
- **cadastro_clientes.js**: Script JavaScript responsável por:
  - Gerenciamento do cadastro (criação, exibição e exclusão de clientes).
  - Validação de dados do formulário.
  - Manipulação do armazenamento local (localStorage).
- **stylesheet.css**: Arquivo CSS para estilização do sistema.
- **README.md**: Este arquivo com informações detalhadas sobre o projeto.

---

## **💻 Tecnologias Utilizadas**

![HTML Badge](https://img.shields.io/badge/HTML-5-%23E34F26?style=for-the-badge&logo=html5&logoColor=white)  
![CSS Badge](https://img.shields.io/badge/CSS-3-%231572B6?style=for-the-badge&logo=css3&logoColor=white)  
![JavaScript Badge](https://img.shields.io/badge/JavaScript-%23F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)  
![localStorage Badge](https://img.shields.io/badge/localStorage-%23FFB74D?style=for-the-badge&logoColor=black)

---

## **📁 Estrutura de Diretórios**

```plaintext
sprint-1-pb-aws-junho-Monique-Borges
├── src/
│   ├── index.html
│   ├── cadastro_clientes.js
│   └── css/
│       └── stylesheet.css
├── README.md
├── .gitignore
```

---

## **⚙️ Funcionalidades**

- **Cadastro de clientes:** Adicione nome, data de nascimento, telefone e e-mail.  
- **Validação de dados:** Verifique se os campos foram preenchidos corretamente, com validações para telefone e e-mail.  
- **Armazenamento local:** Os dados são salvos no `localStorage` do navegador, garantindo persistência mesmo após recarregar a página.  
- **Exibição de clientes:** Veja a lista completa de clientes cadastrados.  
- **Exclusão individual:** Apague cadastros de forma simples com apenas um clique.  

---

## **🚀 Como Usar**

Para utilizar o sistema localmente, siga os passos abaixo:

1. Clone este repositório:

```bash
git clone https://github.com/Compass-pb-aws-2024-JUNHO/sprint-1-pb-aws-junho/tree/Monique-Borges
```

2. Navegue até o diretório do projeto:

```bash
cd sprint-1-pb-aws-junho-Monique-Borges/src
```

3. Abra o arquivo `index.html` em seu navegador web e interaja com o sistema:

- Preencha o formulário com os dados do cliente e clique em "Cadastrar".  
- Os dados serão armazenados no navegador. Você pode visualizá-los em **Inspecionar > Application > Storage > Local Storage**.  
- A lista de clientes será exibida abaixo do formulário.  
- Para excluir um cliente, clique no botão "Excluir" ao lado do cadastro.  

---

## **📅 Metodologia de Desenvolvimento**

O projeto foi desenvolvido utilizando a metodologia **Ágil**, dividindo o trabalho em pequenas entregas incrementais para garantir qualidade e rapidez. Além disso, a refatoração seguiu boas práticas de organização e legibilidade do código.

---

## **📈 Refatoração e Melhorias**

### **1. Modularidade**  
- Código separado por responsabilidades:  
  - Manipulação do DOM.  
  - Operações com `localStorage`.  
  - Validação e feedback para o usuário.  

### **2. Validação Robusta**  
- Adicionadas verificações no JavaScript para garantir que os campos sejam preenchidos corretamente:  
  - Validação de e-mail e telefone utilizando expressões regulares.  
  - Prevenção de cadastro com campos vazios.  

### **3. Experiência do Usuário**  
- Feedback visual para ações do usuário (mensagens de sucesso ou erro).  
- Adicionado diálogo de confirmação para exclusões.  

### **4. Uso de Boas Práticas**  
- Código mais limpo e legível.  
- Redução de duplicidade utilizando funções reutilizáveis.  

---

## **🤔 Desafios Superados**

- **Validação de dados:** Aplicar validações no formulário usando expressões regulares e garantir usabilidade.  
- **Persistência de dados:** Configurar e manipular corretamente o localStorage para salvar e recuperar informações.  
- **Melhorias de UX/UI:** Criar uma interface visual agradável e garantir uma boa experiência para o usuário.  
- **Organização do código:** Modularizar o JavaScript para facilitar a manutenção e a reutilização.  

---

Este README segue as melhores práticas recomendadas durante o Programa de Bolsas Compass UOL e AWS. 😊

--- 
