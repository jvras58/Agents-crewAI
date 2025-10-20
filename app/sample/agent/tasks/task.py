"""
Configuração das tarefas e Crew para o agente sample.
# https://docs.crewai.com/en/guides/agents/crafting-effective-agents
"""

from crewai import Crew, Task
from sample.agent.assistant_agent import get_assistant_agent
from sample.agent.researcher_agent import get_researcher_agent

from utils.config.prompt_builder import build_prompt_by_name
from utils.llm import get_llm
from utils.rag_config import setup_rag_tool_json
from utils.settings import get_settings


def setup_sample_crew() -> Crew:
    """Configura o Crew para os Agentes de Sample."""

    llm = get_llm()
    rag_tool_json = setup_rag_tool_json()

    researcher = get_researcher_agent(llm=llm, rag_tool=rag_tool_json)
    assistant = get_assistant_agent(llm=llm)

    prompt1 = build_prompt_by_name("sample_task_1", "app/sample/agent/prompt")
    prompt2 = build_prompt_by_name("sample_task_2", "app/sample/agent/prompt")

    task1 = Task(
        role=prompt1["role"],
        description=prompt1["description"],
        agent=researcher,
        expected_output=prompt1["expected_output"],
    )

    task2 = Task(
        role=prompt2["role"],
        description=prompt2["description"],
        agent=assistant,
        context=[task1],
        expected_output=prompt2["expected_output"],
    )

    return Crew(
        agents=[researcher, assistant],
        tasks=[task1, task2],
        tools=[rag_tool_json],
        verbose=get_settings().VERBOSE,
        max_rpm=60,
    )
