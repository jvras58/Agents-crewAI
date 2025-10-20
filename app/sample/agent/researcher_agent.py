"""
Definição do Agente Pesquisador.
"""
from crewai import LLM, Agent
from crewai_tools import RagTool

from utils.config.prompt_builder import build_prompt_by_name
from utils.settings import get_settings


# FIXME: Acredito que esteja fazendo isso errado, revisar depois
# pois temos duas maneiras de usar Rag no crewai:
# https://docs.crewai.com/en/tools/overview ( Que seria o rag_tool_json )
# Ou https://docs.crewai.com/en/tools/ai-ml/ragtool ( Que seria o from crewai_tools import RagTool )
def get_researcher_agent(llm: LLM, rag_tool: RagTool) -> Agent:
    """
    Cria e retorna o Agente Pesquisador.

    Args:
        llm: A instância da LLM a ser usada.
        rag_tool: A instância da RagTool configurada.
    """
    prompt = build_prompt_by_name("researcher_agent", "app/sample/agent/prompt")

    return Agent(
        role=prompt["role"],
        goal=prompt["goal"],
        backstory=prompt["backstory"],
        tools=[],
        llm=llm,
        max_iter=3,
        max_retry_limit=1,
        max_execution_time=30,
        verbose=get_settings().VERBOSE,
    )
