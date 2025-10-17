"""
Definição do Agente Pesquisador.
Responsável por buscar contexto usando o RagTool.
"""
from crewai import LLM, Agent
from crewai_tools import RagTool

from utils.config.prompt_builder import build_agent_prompt_by_name
from utils.settings import get_settings


def get_researcher_agent(llm: LLM, rag_tool: RagTool) -> Agent:
    """
    Cria e retorna o Agente Pesquisador.

    Args:
        llm: A instância da LLM a ser usada.
        rag_tool: A instância da RagTool configurada.
    """
    prompt = build_agent_prompt_by_name("researcher_agent", "app/sample/agent/prompt")

    return Agent(
        role=prompt["role"],
        goal=prompt["goal"],
        backstory=prompt["backstory"],
        # tools=[rag_tool], # TODO: Reativar quando tivermos uma chave embedding funcional (Google ou gpt)_
        tools=[],
        llm=llm,
        max_iter=3,
        max_retry_limit=1,
        max_execution_time=30,
        verbose=get_settings().VERBOSE,
    )
