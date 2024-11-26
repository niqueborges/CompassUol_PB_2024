const express = require('express');
const cors = require('cors');
const path = require('path');
const app = express();
const port = 3000;

const nbaRoutes = require('./routes/nbaRoutes');

// Permitir o uso de CORS
app.use(cors());

// Rota de API
app.use('/nba', nbaRoutes);

// Servir arquivos estáticos da pasta 'src/imagens' (e outros arquivos estáticos)
app.use('/images', express.static(path.join(__dirname, 'src/imagens'))); // Rota para imagens

// Servir arquivos estáticos como CSS e JS da pasta 'src'
app.use(express.static(path.join(__dirname, 'src'))); // Para servir arquivos como style.css, script.js

// Rota para a página principal
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'src', 'index.html'));
});

// Rota para a página de times
app.get('/team', (req, res) => {
    res.sendFile(path.join(__dirname, 'src', 'team.html'));
});

app.listen(port, () => {
    console.log(`Servidor rodando em http://localhost:${port}`);
});

