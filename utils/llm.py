"""Configuração do modelo de Linguagem Grande (LLM) com Groq."""

from functools import lru_cache

from crewai import LLM
from utils.settings import get_settings


@lru_cache(maxsize=1)
def get_llm() -> LLM:
    """Retorna a LLM configurada com Groq."""
    settings = get_settings()
    api_key = settings.GROQ_API_KEY
    
    if not api_key:
        raise ValueError('GROQ_API_KEY não encontrada nas configurações.')

    llm = LLM(
        model='groq/llama-3.1-8b-instant',
        api_key=api_key,
        temperature=0.7,
    )
    return llm
