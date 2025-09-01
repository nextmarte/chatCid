
from fastapi import FastAPI
from pydantic import BaseModel
import ollama

app = FastAPI()

class ChatRequest(BaseModel):
    model: str
    message: str

@app.get("/models")
async def list_models():
    """
    Lista todos os modelos disponíveis localmente no Ollama.
    """
    return ollama.list()

@app.post("/chat")
async def chat(request: ChatRequest):
    """
    Envia uma mensagem para um modelo de chat específico e retorna a resposta.
    """
    response = ollama.chat(
        model=request.model,
        messages=[
            {
                'role': 'user',
                'content': request.message,
            },
        ]
    )
    return response['message']

@app.get("/")
def read_root():
    return {"message": "API de Chat com Ollama está no ar!"}

