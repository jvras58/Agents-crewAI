"""
Configuração das tarefas e Crew para o agente sample.
# https://docs.crewai.com/en/guides/agents/crafting-effective-agents
"""

from crewai import Crew, Task
from sample.agent.assistant_agent import get_assistant_agent
from sample.agent.researcher_agent import get_researcher_agent

from utils.llm import get_llm
from utils.rag_config import setup_rag_tool_json
from utils.settings import get_settings


def setup_sample_crew() -> Crew:
    """Configura o Crew para os Agentes de Sample."""

    llm = get_llm()
    rag_tool_json = setup_rag_tool_json()

    researcher = get_researcher_agent(llm=llm, rag_tool=rag_tool_json)
    assistant = get_assistant_agent(llm=llm)

    task1 = Task(
        description="Pesquise e recupere contexto relevante para a consulta: {query}.",
        agent=researcher,
        expected_output="Contexto detalhado e completo recuperado das fontes indexadas (RAG tool)."
    )

    task2 = Task(
        description="Usando SOMENTE o contexto fornecido pelo Pesquisador, crie uma resposta final clara e profissional para a consulta: {query}.",
        agent=assistant,
        context=[task1],
        expected_output="Resposta final formatada profissionalmente, baseada 100% no contexto recuperado."
    )

    return Crew(
        agents=[researcher, assistant],
        tasks=[task1, task2],
        tools=[rag_tool_json],
        verbose=get_settings().VERBOSE,
        max_rpm=60,
    )
