"""
Configuração da ferramentas de busca.
# https://docs.crewai.com/en/tools/
# https://docs.crewai.com/en/tools/file-document/jsonsearchtool
"""
from crewai_tools import JSONSearchTool


def setup_rag_tool_json() -> JSONSearchTool:
    """Inicializa e configura um JSONSearchTool usando o LLM existente e a
    configuração de embeddings do Google.
    """

    config = {
        "embedding_model": {
            "provider": "google-generativeai",
            "config": {
                "model": "models/gemini-embedding-001",
                "task_type": "retrieval_document",
            },
        },
    }

    json_tool = JSONSearchTool(config=config, json_path='helpers/fastapi.json')

    return json_tool
