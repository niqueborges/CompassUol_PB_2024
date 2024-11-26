// Factory para criar objetos Cliente
function ClienteFactory() {
    function criarCliente(nome, dataNascimento, telefone, email) {
        return { nome, dataNascimento, telefone, email };
    }
    return { criarCliente };
}

// Manipulação de localStorage
const storageKey = 'clientes';

function salvarClientes(clientes) {
    localStorage.setItem(storageKey, JSON.stringify(clientes));
}

function recuperarClientes() {
    const clientes = localStorage.getItem(storageKey);
    return clientes ? JSON.parse(clientes) : [];
}

function adicionarClienteAoLocalStorage(cliente) {
    const clientes = recuperarClientes();
    clientes.push(cliente);
    salvarClientes(clientes);
    mostrarMensagem('Cliente cadastrado com sucesso!');
}

function excluirClienteDoLocalStorage(index) {
    const clientes = recuperarClientes();
    if (clientes[index]) {
        clientes.splice(index, 1);
        salvarClientes(clientes);
        mostrarMensagem('Cliente excluído com sucesso!', 'erro');
    }
}

// Exibição de mensagens
function mostrarMensagem(mensagem, tipo = 'sucesso') {
    const mensagemDiv = document.createElement('div');
    mensagemDiv.textContent = mensagem;
    mensagemDiv.className = tipo === 'sucesso' ? 'alert alert-success' : 'alert alert-danger';
    document.body.prepend(mensagemDiv);
    setTimeout(() => mensagemDiv.remove(), 3000);
}

// Exibir clientes na página
function exibirClientes() {
    const listaCadastro = document.getElementById('listaCadastro');
    listaCadastro.innerHTML = '';

    const clientes = recuperarClientes();
    const fragment = document.createDocumentFragment();

    clientes.forEach((cliente, index) => {
        const clienteElement = document.createElement('div');
        clienteElement.classList.add('cliente-item');
        clienteElement.innerHTML = `
            <p><strong>Nome:</strong> ${cliente.nome}</p>
            <p><strong>Data de Nascimento:</strong> ${cliente.dataNascimento}</p>
            <p><strong>Telefone:</strong> ${cliente.telefone}</p>
            <p><strong>Email:</strong> ${cliente.email}</p>
            <button class="btn btn-danger btn-sm">Excluir</button>
        `;

        const btnExcluir = clienteElement.querySelector('button');
        btnExcluir.addEventListener('click', () => {
            if (confirm('Tem certeza de que deseja excluir este cliente?')) {
                excluirClienteDoLocalStorage(index);
                exibirClientes();
            }
        });

        fragment.appendChild(clienteElement);
    });

    listaCadastro.appendChild(fragment);
}

// Evento de submit
const formCadastro = document.getElementById('formCadastro');
formCadastro.addEventListener('submit', (event) => {
    event.preventDefault();

    const { nome, dataNascimento, tel: telefone, email } = formCadastro;

    if (!nome.value || !dataNascimento.value || !telefone.value || !email.value) {
        alert('Por favor, preencha todos os campos.');
        return;
    }

    const factory = ClienteFactory();
    const novoCliente = factory.criarCliente(nome.value, dataNascimento.value, telefone.value, email.value);

    adicionarClienteAoLocalStorage(novoCliente);
    formCadastro.reset();
    exibirClientes();
});

// Exibir clientes ao carregar
window.addEventListener('DOMContentLoaded', exibirClientes);
