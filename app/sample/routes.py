"""Definição das rotas da API para interação com o CrewAI."""
from functools import lru_cache

from crewai import Crew
from fastapi import APIRouter, Depends, HTTPException, Request
from sample.agent.tasks.task import setup_sample_crew

from utils.rate_limiter import limiter

from .schema import ChatRequest, ChatResponse

router = APIRouter(prefix="/api/v1", tags=["Chat/CrewAI Sample"])


@router.post("/chat", response_model=ChatResponse)
@limiter.limit("3/minute")  # TODO: Aplica o limite de 3 requisições por minuto
async def chat_endpoint(
    request: Request,
    chat_request: ChatRequest,
    crew: Crew = Depends(lru_cache(setup_sample_crew)),
):
    """
    Processa uma consulta de chat, orquestrando os agentes via CrewAI.
    """
    try:
        result = crew.kickoff(inputs={"query": chat_request.query})
        # O resultado contém a resposta final do último agente.
        # A extração robusta de 'sources' (fontes) do CrewAI requer
        # formatação específica nas Tasks, por isso a lista é vazia por padrão aqui.
        return ChatResponse(response=result.raw, sources=[])
    except Exception as e:
        print(f"Erro no processamento do CrewAI. Detalhe: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e)) from e
