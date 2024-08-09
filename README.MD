<h1>Documentação da API da Padaria</h1>

<p>Bem-vindo à documentação da API da Padaria! Esta API é projetada para gerenciar produtos e pedidos em uma padaria. A API foi desenvolvida usando <strong>FastAPI</strong> e <strong>PostgreSQL</strong>.</p>

<h2>Visão Geral</h2>
<p>A API da padaria fornece endpoints para realizar as seguintes operações:</p>
<ul>
    <li><strong>Gerenciar Produtos:</strong> Adicionar, listar, atualizar e excluir produtos.</li>
    <li><strong>Gerenciar Pedidos:</strong> Criar, listar e atualizar pedidos.</li>
</ul>

<h2>Pré-requisitos</h2>
<ul>
    <li><strong>Python 3.7 ou superior</strong></li>
    <li><strong>PostgreSQL</strong></li>
    <li><strong>Bibliotecas Python:</strong> FastAPI, Uvicorn, Psycopg2</li>
</ul>

<h2>Configuração do Ambiente Linux</h2>
<p>Para configurar o ambiente, siga os passos abaixo:</p>

<pre><code>sudo apt update
sudo apt install python3 python3-pip
pip install fastapi uvicorn psycopg2-binary
</code></pre>

<h2>Configuração do Banco de Dados</h2>
<p>Certifique-se de que o PostgreSQL está instalado e configurado. Crie um banco de dados para a padaria:</p>

<pre><code>sudo -u postgres psql
CREATE DATABASE padaria;
CREATE USER padaria_user WITH ENCRYPTED PASSWORD 'sua_senha';
GRANT ALL PRIVILEGES ON DATABASE padaria TO padaria_user;
\q
</code></pre>

<h2>Executando a API</h2>
<p>Para executar a API, você precisará de um arquivo de configuração para conectar ao banco de dados e o código principal da API.</p>

<h3>Arquivo de Configuração</h3>
<p>Crie um arquivo chamado <code>config.py</code> com o seguinte conteúdo:</p>

<pre><code>DATABASE_URL = "postgresql://padaria_user:sua_senha@localhost/padaria"
</code></pre>

<h3>Executar o Servidor</h3>
<p>Inicie o servidor Uvicorn com o seguinte comando:</p>

<pre><code>uvicorn main:app --reload
</code></pre>

<h2>Testando a API</h2>
<p>Você pode testar a API acessando os seguintes endpoints:</p>
<ul>
    <li><a href="http://127.0.0.1:8000/docs" target="_blank">Documentação automática do FastAPI</a></li>
    <li><a href="http://127.0.0.1:8000/redoc" target="_blank">Documentação alternativa</a></li>
</ul>

<h2>Notas</h2>
<p class="note">Certifique-se de substituir <code>sua_senha</code> pela senha real do seu banco de dados.</p>

<h2>Contribuição</h2>
<p>Se você deseja contribuir para o projeto, por favor, faça um fork do repositório e envie suas pull requests.</p>

<h2>Licença</h2>
<p>Este projeto está licenciado sob a MIT License - veja o arquivo <code>LICENSE</code> para detalhes.</p>