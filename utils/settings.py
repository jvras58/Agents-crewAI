"""Gerenciamento de configurações da aplicação usando Pydantic."""
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class setup_Settings(BaseSettings):
    """
    Classe que representa as configurações definidas no .env da aplicação.
    """

    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        case_sensitive=True,
        env_ignore_empty=True,
    )

    GROQ_API_KEY: str
    SERPER_API_KEY: str | None = None
    EMBEDDINGS_GOOGLE_API_KEY: str | None = None

    # Configurações opcionais
    CREWAI_TRACING_ENABLED: bool = False
    VERBOSE: bool = False
    DB_URL: str | None = None
    PORT: int = 8000


@lru_cache
def get_settings() -> setup_Settings:
    """Obtém as configurações da aplicação, cacheadas para performance."""
    return setup_Settings()
