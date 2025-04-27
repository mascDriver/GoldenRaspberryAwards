# Golden Raspberry Awards

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![SQLModel](https://img.shields.io/badge/SQLModel-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python&logoColor=white)
![Tests](https://img.shields.io/badge/Tests-Pytest-green?style=for-the-badge&logo=pytest&logoColor=white)

Uma API RESTful para gerenciar os dados do prêmio Golden Raspberry Awards, famoso por reconhecer os piores filmes da
indústria cinematográfica.

## 🚀 Funcionalidades

- Upload de filmes via arquivo CSV
- Consulta de intervalos entre vitórias consecutivas de produtores
- Identificação de produtores com menor e maior intervalo entre vitórias

## 📋 Pré-requisitos

- Python 3.12+
- Poetry (gerenciador de pacotes)

## 🔧 Instalação

1. Clone o repositório:

``` bash
   git clone <repository-url>
   cd GoldenRaspberryAwards
```

1. Instale as dependências:

``` bash
   poetry install
```

## 🚀 Executando a aplicação

``` bash
poetry run uvicorn app.main:app --reload
```

ou

``` bash
uvicorn app.main:app --reload
```

A API estará disponível em: [http://localhost:8000](http://localhost:8000)

## 📚 Documentação da API

A documentação completa da API está disponível em:

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## 📌 Endpoints

### 1. Upload de Filmes (CSV)

``` http
POST /awards/movies
```

- **Descrição**: Carrega dados de filmes a partir de um arquivo CSV
- **Corpo da Requisição**: Arquivo CSV (multipart/form-data)
- **Resposta de Sucesso**: 201 Created

### 2. Consulta de Intervalos entre Vitórias

``` http
GET /awards/intervals
```

- **Descrição**: Retorna produtores com menor e maior intervalo entre vitórias consecutivas
- **Resposta de Sucesso**: 200 OK

## 🧪 Testes

Execute os testes com:

``` bash
pytest
```

Os testes estão divididos em:

- Testes do endpoint de intervalos () `test_awards_intervals.py`
- Testes do endpoint de upload de filmes () `test_movies_upload.py`
- Testes de endpoints principais () `test_main.py`

## 📊 Formato do CSV

O arquivo CSV para upload deve seguir o formato:

``` 
year;title;studios;producers;winner
```

Exemplo:

``` 
1980;Can't Stop the Music;Associated Film Distribution;Allan Carr;yes
1980;Cruising;Lorimar Productions, United Artists;Jerry Weintraub;
```

## 🗂️ Estrutura do Projeto

``` 
GoldenRaspberryAwards/
├── app/                  # Código-fonte principal
│   ├── routers/          # Rotas da API
│   ├── main.py           # Ponto de entrada da aplicação
│   ├── models.py         # Modelos de dados SQLModel/Pydantic
│   ├── database.py       # Configuração do banco de dados
│   ├── settings.py       # Configurações da aplicação
│   └── utils.py          # Funções utilitárias
├── tests/                # Testes automatizados
│   ├── test_awards_intervals.py
│   ├── test_movies_upload.py
│   └── test_main.py  
├── assets/               # Arquivos estáticos/recursos
├── pyproject.toml        # Configuração do Poetry e dependências
└── README.md             # Este arquivo
```

## 📝 Licença

Este projeto está sob a licença [MIT](https://opensource.org/licenses/MIT) - veja o arquivo LICENSE para mais detalhes.

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests.
Desenvolvido para gerenciar os dados do famoso prêmio "Golden Raspberry Awards", celebrando os piores filmes da
indústria cinematográfica.
