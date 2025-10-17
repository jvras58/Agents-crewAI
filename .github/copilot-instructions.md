<!-- Copilot instructions for this repository (concise, actionable) -->
# Instruções rápidas para agentes AI — Agents-crewAI

Estas instruções ajudam um agente de codificação a ser imediatamente produtivo neste repositório. Foque nas áreas indicadas e edite apenas onde explicado.

- Visão geral (porquê): esta aplicação é uma API FastAPI que orquestra agentes usando CrewAI. Fluxo principal: HTTP -> `app/sample/routes.py` -> `app/sample/agent/tasks/task.py` (Crew) -> agentes (`app/sample/agent/*`) -> ferramentas RAG (`utils/rag_config.py`) -> LLM (`utils/llm.py`). Veja a arquitetura em `dev/C4.md`.

- Como rodar (dev / prod):
  - Dependências e comandos usam o gerenciador `uv` (Astral UV). Use `make sync` ou `uv sync` para sincronizar dependências. (Veja `Makefile` e `Dockerfile`.)
  - Desenvolvimento local: `make run` (equivalente a `uv run fastapi dev app/startup.py --host 0.0.0.0 --port 8000`).
  - Produção (imagem): `make prod` ou o CMD do `Dockerfile` que roda `uv run fastapi run app/startup.py`.

- Convezões e padrões importantes:
  - Prompts dos agentes são YAMLs em `app/sample/agent/prompt/` e `utils/prompt/`. Use `utils/config/prompt_builder.py` para construir prompts (mescla `backstory` + `examples`).
  - Singletons/configs: use `utils/settings.py` + `get_settings()` (cache via `lru_cache`). Não crie múltiplas instâncias da LLM; use `utils/llm.get_llm()`.
  - Criação de agentes: `get_assistant_agent` e `get_researcher_agent` retornam objetos `Agent(...)`. Evite alterar a assinatura do Agent sem atualizar `tasks/task.py`.
  - Orquestração: `app/sample/agent/tasks/task.py` monta `Crew(agents=[...], tasks=[...], tools=[...])`. Modificações aqui alteram o pipeline global.
  - Rate limiting: `slowapi` é usado em `app/startup.py` e `app/sample/routes.py` com key func `X-Session-ID` (veja `utils/rate_limiter.py`).

- Integrações e chaves externas:
  - LLM principal: GROQ. Chave obrigatória: `GROQ_API_KEY` (ver `utils/llm.py`). Se ausente, `get_llm()` lança erro.
  - Embeddings (RAG): `EMBEDDINGS_GOOGLE_API_KEY` e `SERPER_API_KEY` são opcionais; parte do código de tools está com `tools=[]` (comentado) até ter embedding funcional.
  - Não hardcode chaves: siga `.env-sample` e mantenha segredos em `.env` (excluído em `.gitignore`).

- Padrões de edição para agentes:
  - Para atualizar comportamento de um agente, edite o respectivo prompt YAML em `app/sample/agent/prompt/` e, se necessário, ajuste `get_*_agent(...)` para mudar parâmetros (`max_iter`, `max_execution_time`, `verbose`).
  - Para adicionar/ajustar ferramentas RAG, edite `utils/rag_config.py` e registre a tool em `tasks/task.py` (campo `tools=[...]`).
  - Para alterar o pipeline (nova task, reorder), modifique `app/sample/agent/tasks/task.py` — cada `Task` define `description`, `agent`, `context` e `expected_output`.

- Observações operacionais/diagnóstico:
  - Health-check: `GET /` (definido em `app/startup.py`).
  - Endpoint principal: `POST /api/v1/chat` (schema em `app/sample/schema.py`). Exemplo: `curl -X POST http://localhost:8000/api/v1/chat -H 'Content-Type: application/json' -d '{"query":"Como funciona o FastAPI?"}'`.
  - Logs e debug: use flag `VERBOSE` (em `.env`) e `print` é usado em handlers para erros do CrewAI; considerar melhorar logging centralizado se for editar.

- Regras de edição automática (para agentes copiloto):
  - Prefira mudanças pequenas e localizadas: prompts, `Task.description` e parâmetros de `Agent`. Evite grandes refactors do fluxo sem testes ou validação manual.
  - Ao adicionar dependência: atualize `pyproject.toml` e utilize `uv sync` para sincronizar; no DevContainer, `postCreateCommand` já roda `make`.
  - Testes rápidos: não existem testes unitários no repositório; verifique manualmente com `make run` + chamadas curl. Confirme que `get_llm()` não lança antes de integrar agentes (configurar `GROQ_API_KEY`).

- Arquivos de referência rápido (edite com cautela):
  - Entrypoint / app: `app/startup.py`
  - Rotas: `app/sample/routes.py`
  - Agentes: `app/sample/agent/assistant_agent.py`, `app/sample/agent/researcher_agent.py`
  - Pipeline/Crew: `app/sample/agent/tasks/task.py`
  - Prompts: `app/sample/agent/prompt/*.yaml`, `utils/prompt/fallback_agent_prompt.yaml`
  - LLM e RAG tools: `utils/llm.py`, `utils/rag_config.py`
  - Configs: `utils/settings.py`, `.env-sample`
  - Build & run: `Makefile`, `Dockerfile`, `.devcontainer/*`
