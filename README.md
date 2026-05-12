# 📊 # Processing Pipeline com Python

Projeto em Python para processamento de eventos JSON, geração de estatísticas em CSV, tratamento de erros e testes unitários.


# Objetivo

Este projeto simula um pipeline simples de engenharia de dados responsável por:

- Ler eventos de um arquivo JSON
- Validar estrutura e timestamps
- Filtrar eventos dos últimos 30 dias
- Gerar métricas estatísticas
- Registrar eventos inválidos em deadletter
- Executar testes unitários

---

## Tecnologias utilizadas

- Python 3.8+
  - json
  - csv
  - datetime
  - unittest

O projeto utiliza apenas bibliotecas nativas do Python.


---

## 📂 Estrutura do projeto
.
├── processor.py
├── events.json
├── stats.csv
├── deadletter.json
└── README.md


---

## 📥 Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo


## Crie um ambiente virtual:

python -m venv venv
## source venv/bin/activate  # Linux/Mac
## venv\Scripts\activate     # Windows

## Instalar as dependências:
pip install -r requirements.txt

python script.py


## Formato do JSON esperado
## O arquivo events.json deve conter uma lista de objetos no seguinte formato:

[
    {
        "user_id": "user1",
        "event_type": "login",
        "timestamp": "2026-05-01T10:00:00Z"
    },
    {
        "user_id": "user2",
        "event_type": "purchase",
        "timestamp": "2026-05-02T12:30:00Z",
        "amount": 150.75
    }
]


## Saída esperada





## Tratamento de erros
## O script trata os seguintes erros:

    Arquivo JSON não encontrado
    JSON inválido
    Evento válido
    Evento com Estrutura inesperada (ex: ausência de user_id)
    Erros inesperados



##
##
##