# 📊 Processamento de Eventos JSON com Python

Este projeto lê um arquivo JSON contendo eventos de usuários e calcula a quantidade de `user_id` únicos utilizando Python e pandas.

---

## Tecnologias utilizadas

- Python 3.8+
- pandas

---

## 📂 Estrutura do projeto
├── events.json # Arquivo de entrada (dados)
├── script.py # Script principal
├── requirements.txt # Dependências do projeto
└── README.md # Documentação


---

## 📥 Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo


## Crie um ambiente virtual (opcional, mas recomendado):

## python -m venv venv
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
    "timestamp": "2025-09-01T10:00:00Z",
    "amount": null
  }
]


## Saída esperada
## O script irá exibir:

    Total de usuários únicos
    Lista de IDs encontrados

Total de user_id únicos: 3
IDs encontrados: {'user1', 'user2', 'user3'}




## Tratamento de erros
## O script trata os seguintes erros:

    Arquivo JSON não encontrado
    JSON inválido
    Estrutura inesperada (ex: ausência de user_id)
    Erros inesperados



##
##
##