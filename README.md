# 🤖 Agentes com CrewAI

Uma API Simples construída com FastAPI que orquestra agentes de IA usando CrewAI para fornecer respostas inteligentes.

## 🚀 Características

- **API REST** com FastAPI
- **Orquestração de Agentes** com CrewAI
- **Provedores LLM** (Groq com LiteLLM)
- **Rastreamento** de execução opcional

## 📋 Pré-requisitos

- Python 3.12+
- UV (gerenciador de pacotes)

## ⚙️ Instalação

1. **Clone o repositório:**
   ```bash
   git clone <repository-url>
   cd agent
   ```

2. **Instale as dependências:**
   ```bash
   # Usando Makefile (recomendado)
   make sync
   
   # Ou manualmente
   uv sync
   ```

3. **Configure as variáveis de ambiente:**
   ```bash
   cp .env-semple .env
   # Edite o arquivo .env com suas chaves de API
   ```

## 🔧 Configuração

### Variáveis de Ambiente Obrigatórias

| Variável | Descrição | Exemplo |
|-----------|-----------|---------|
| `LLM_PROVIDER` | Provedor do LLM | `groq`, `openai`, `huggingface`, `litellm` |
| `GROQ_API_KEY` | Chave da API Groq | `gsk_...` |
| `CREWAI_TRACING_ENABLED` | Habilitar rastreamento | `true` ou `false` |


## 🚀 Execução

### 🛠️ Usando Makefile (Recomendado)

O projeto inclui um Makefile para facilitar o desenvolvimento. Execute `make` para ver todos os comandos disponíveis:

```bash
# Ver todos os comandos disponíveis
make
```

### Desenvolvimento Manual
```bash
# Configurar variáveis de ambiente
export LLM_PROVIDER=groq
export GROQ_API_KEY="sua-chave-groq"
```

### Produção
```bash
make run prod
```

A API estará disponível em `http://localhost:8000`

## 📚 Uso da API

### Endpoints Disponíveis

- **GET** `/` - Verificação de saúde (desabilitado o schema no swagger)
- **POST** `/api/v1/chat` - Chat com o agente de semple

### Exemplo de Requisição

```bash
curl -X POST "http://localhost:8000/api/v1/chat" \
     -H "Content-Type: application/json" \
     -d '{
       "query": "Como funciona o Fastapi?"
     }'
```

### Exemplo de Resposta

```json
{
  "response": "Fastapi é uma framework...",
  "sources": []
}
```

## 🏗️ Arquitetura

### Visão Geral da Arquitetura

A aplicação é construída seguindo uma arquitetura modular com orquestração de agentes de IA:

```
🌐 Cliente HTTP → FastAPI → CrewAI Orchestrator → Agentes → Resposta
```

### Componentes Principais

| Componente | Responsabilidade | Localização |
|------------|------------------|-------------|
| **FastAPI** | Framework web REST API | `app/startup.py`, `app/` |
| **CrewAI** | Orquestração de agentes | `app/*/agent/tasks/task.py` |
| **Agentes** | Lógica especializada de IA | `app/*/agent/` |
| **RAG Tools** | Recuperação aumentada | `utils/rag_config.py` |
| **Utilitários** | Configurações e helpers | `utils/` |

### Fluxos de Dados

#### 1. Endpoint Chat (`/api/v1/chat`)
```
Requisição → FastAPI Router → Sample Crew → Researcher Agent → RAG Tools → Assistant Agent → Resposta
```


### Agentes Disponíveis

#### Sample Agents (Pipeline Sequencial)
- **Researcher Agent**: Busca e recupera contexto relevante usando RAG
- **Assistant Agent**: Gera resposta final baseada no contexto fornecido


### Integrações Externas

| Serviço | Propósito | Configuração |
|---------|-----------|--------------|
| **Groq API** | Modelo de linguagem principal | `GROQ_API_KEY` |
| **Google AI** | Embeddings para RAG | `EMBEDDINGS_GOOGLE_API_KEY` |
| **Serper API** | Busca web integrada | `SERPER_API_KEY` |

### Fontes de Dados

- **PDFs Locais**: Documentos armazenados em `db/`
- **Busca Web**: Resultados em tempo real via Serper

### Estrutura de Diretórios

```
📁 agent/
├── 🚀 app/startup.py                 # Ponto de entrada FastAPI
├── 📡 app/                           # Endpoints e schemas
│   ├── 💬 sample/                   # Chat endpoint
│   │   ├── routes.py                # Router FastAPI para chat
│   │   ├── schema.py                # Schemas Pydantic para chat
│   │   └── agent/                   # Implementações dos agentes sample
│   │       ├── assistant_agent.py   # Agente assistente
│   │       ├── researcher_agent.py  # Agente pesquisador
│   │       ├── tasks/task.py        # Configuração de tarefas e crew
│   │       └── prompt/              # Prompts YAML para agentes sample
├── 🛠️ utils/                        # Utilitários compartilhados
│   ├── 📝 config/                   # Configurações de prompts
│   │   ├── prompt_builder.py        # Construtor de prompts
│   │   └── load_yaml.py             # Carregador de YAML
│   ├── 🧠 llm.py                    # Configuração LLM
│   ├── 🔍 rag_config.py             # RAG Tools
│   ├── ⚙️ settings.py               # Configurações Pydantic
│   └── rate_limiter.py              # Rate limiter
```

### Arquitetura C4 Model

📖 **[Visão de Contêineres](/dev/C4.md#visão-de-contêineres)**

📖 **[Visão de Componentes](/dev/C4.md#visão-de-componentes)**


## 🐳 Desenvolvimento com DevContainer

O repositório conta com uma arquitetura de containerização para facilitar o processo de desenvolvimento. Para ativá-lo, siga a documentação completa:

📖 **[Guia completo do DevContainer](/dev/DEVCONTAINER.md)**

## 🔍 Solução de Problemas

### Erro: "LLM Provider NOT provided"
- Verifique se `LLM_PROVIDER` está definido
- Confirme se a chave de API correspondente está configurada
- Valores válidos: `groq`, `openai`, `huggingface`, `litellm`

### Erro de conexão com APIs externas
- Verifique suas chaves de API
- Confirme conectividade com a internet
- Verifique limites de uso das APIs

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo LICENSE para detalhes.

## 🔗 Links Úteis

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [CrewAI Documentation](https://docs.crewai.com/)
- [Groq API](https://console.groq.com/)
- [Serper API](https://serper.dev/)
