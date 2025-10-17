"""
Ponto de entrada principal da aplicação.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

from sample.routes import router as chat_router
from utils.rate_limiter import limiter

app = FastAPI(
    title="Agents with CrewAI",
    description="API para orquestração de agentes de IA com CrewAI e Groq.",
    version="0.0.1",
)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router)

@app.get("/", include_in_schema=False)
async def health_check():
    """Verificação simples de saúde da API."""
    return {"status": "ok", "service": "CrewAI Assistant on FastAPI"}
