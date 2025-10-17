"""Modelos Pydantic para requisições e respostas da API."""

from pydantic import BaseModel
from typing import List

class ChatRequest(BaseModel):
    """Modelo para a requisição de chat do usuário."""
    query: str

class ChatResponse(BaseModel):
    """Modelo para a resposta do chat."""
    response: str
    sources: List[str] = []
