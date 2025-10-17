"""
Configuração da ferramentas de busca.
"""
from crewai_tools import JSONSearchTool


def setup_rag_tool_json() -> JSONSearchTool:
    """Inicializa e configura um JSONSearchTool usando o LLM existente e a
    configuração de embeddings do Google.

    Observação: esta função substitui o uso anterior de um índice Chroma
    persistente pelo `JSONSearchTool`, que realiza buscas dentro de arquivos
    JSON. Mantemos a configuração do modelo de embedding do Google.
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
