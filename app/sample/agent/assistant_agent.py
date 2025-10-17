"""
Definição do Agente Assistente.
Responsável por gerar a resposta final com base no contexto.
"""
from crewai import LLM, Agent

from utils.config.prompt_builder import build_agent_prompt_by_name
from utils.settings import get_settings


def get_assistant_agent(llm: LLM) -> Agent:
    """
    Cria e retorna o Agente Assistente.

    Args:
        llm: A instância da LLM a ser usada.
    """
    prompt = build_agent_prompt_by_name("assistant_agent", "app/sample/agent/prompt")

    return Agent(
        role=prompt["role"],
        goal=prompt["goal"],
        backstory=prompt["backstory"],
        llm=llm,
        max_iter=3,
        max_retry_limit=1,
        max_execution_time=30,
        verbose=get_settings().VERBOSE,
    )
