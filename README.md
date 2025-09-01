# API de Chat com Ollama

Esta é uma API simples construída com FastAPI que serve como uma interface de chat local para os modelos de linguagem executados através do Ollama.

## Funcionalidades

- Lista todos os modelos de linguagem disponíveis na sua instalação local do Ollama.
- Permite conversar com qualquer um dos modelos disponíveis através de um endpoint RESTful.
- Fornece uma API no estilo OpenAI, mas rodando totalmente offline e local.

## Pré-requisitos

Antes de começar, garanta que você tenha os seguintes softwares instalados:

- [Python](https://www.python.org/downloads/) (versão 3.8 ou superior)
- [Ollama](https://ollama.com/) com pelo menos um modelo baixado (ex: `ollama run llama3`)
- [uv](https://github.com/astral-sh/uv) (gerenciador de pacotes e ambientes virtuais em Python)

## Instalação e Configuração

1.  **Clone o repositório (ou configure o projeto):**
    ```bash
    # Se estivesse em um repositório git
    # git clone <url-do-repositorio>
    # cd chat-ollama-api
    ```

2.  **Crie o ambiente virtual e instale as dependências:**
    O `uv` irá criar um ambiente virtual e instalar as bibliotecas listadas no `pyproject.toml` (ou `requirements.txt`).
    ```bash
    # Instala as dependências definidas no pyproject.toml
    uv sync
    ```
    Ou, se preferir usar o `requirements.txt`:
    ```bash
    uv pip install -r requirements.txt
    ```

## Como Executar a API

Para iniciar o servidor da API, execute o seguinte comando na raiz do projeto. Ele usará o `uv` para rodar o `uvicorn` dentro do ambiente virtual correto.

A API será executada na porta `8566`.

```bash
uv run uvicorn src.main:app --reload --port 8566
```

Você verá uma saída indicando que o servidor está no ar:
```
INFO:     Uvicorn running on http://127.0.0.1:8566 (Press CTRL+C to quit)
```

## Documentação da API

A API expõe os seguintes endpoints:

### 1. Listar Modelos Disponíveis

- **Endpoint:** `GET /models`
- **Descrição:** Retorna uma lista de todos os modelos que foram baixados e estão disponíveis na sua instalação do Ollama.
- **Exemplo de chamada com `curl`:**
  ```bash
  curl http://127.0.0.1:8566/models
  ```
- **Exemplo de Resposta (JSON):**
  ```json
  {
    "models": [
      {
        "name": "llama3:latest",
        "model": "llama3:latest",
        "modified_at": "2024-08-28T14:03:03.8430195Z",
        "size": 4661223675,
        "digest": "a2dd0b6f0a4538a3b67d3425b52c21b422c333d504a09a0b1b5221574248a52d",
        "details": {
          "parent_model": "",
          "format": "gguf",
          "family": "llama",
          "families": [
            "llama"
          ],
          "parameter_size": "8B",
          "quantization_level": "Q4_0"
        }
      }
    ]
  }
  ```

### 2. Enviar uma Mensagem para o Chat

- **Endpoint:** `POST /chat`
- **Descrição:** Envia uma pergunta para um modelo específico e recebe a resposta gerada por ele.
- **Corpo da Requisição (JSON):**
  - `model` (string, obrigatório): O nome do modelo a ser usado (ex: `"llama3"` ou `"llama3:latest"`).
  - `message` (string, obrigatório): A mensagem ou pergunta do usuário.
- **Exemplo de chamada com `curl`:**
  ```bash
  curl -X POST http://127.0.0.1:8566/chat \
  -H "Content-Type: application/json" \
  -d '{
      "model": "llama3",
      "message": "Qual é a capital do Brasil?"
  }'
  ```
- **Exemplo de Resposta (JSON):**
  ```json
  {
    "role": "assistant",
    "content": "A capital do Brasil é Brasília."
  }
  ```

## Tecnologias Utilizadas

- **FastAPI:** Framework web para a construção da API.
- **Ollama:** Para executar os modelos de linguagem localmente.
- **Uvicorn:** Servidor ASGI para rodar a aplicação FastAPI.
- **UV:** Para gerenciamento de dependências e ambiente virtual.
- **Pydantic:** Para validação de dados.
