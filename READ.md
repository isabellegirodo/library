<h1>CRUD em python seguindo o padão MVT</h1>

<h2>Primeiramente, crie um ambiente virtual e ative-o</h2>
`python3 -m venv venv

source venv/bin/activate`

<h2>Depois, instale as bibliotecas sqlmodel e matplotlib com o pip</h2>
`pip install sqlmodel

pip install matplotlib`

<h2>No arquivo models.py, temos a criação das tabelas no banco de dados</h2>
O comando `python3 models.py` cria o arquivo do banco de dados

<h2>No arquivo views.py, está a criação das funções que fazem a comunicação com o banco de dados.

(Esse arquivo contém toda a lógica do projeto)</h2>

<h2>No arquivo templates.py, fica a visualização para o usuário via terminal</h2>
