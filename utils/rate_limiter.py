"""Módulo para configuração do rate limiter da aplicação."""
from fastapi import Request
from slowapi import Limiter
from slowapi.util import get_remote_address


def get_session_id(request: Request) -> str:
    """
    Extrai o identificador de sessão do header 'X-Session-ID'.
    Se não encontrar, usa o endereço de IP do cliente como fallback.
    """
    session_id = request.headers.get("X-Session-ID")
    if session_id:
        return session_id
    return get_remote_address(request)


# O ideal em produção é usar um backend como Redis:
# limiter = Limiter(key_func=get_session_id, storage_uri="redis://localhost:6379")
limiter = Limiter(key_func=get_session_id)
