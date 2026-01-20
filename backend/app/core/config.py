from pydantic_settings import BaseSettings
from typing import List, Optional
import secrets

class Settings(BaseSettings):
    # Основные настройки
    PROJECT_NAME: str = "TechStore"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"

    # Безопасность
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # База данных
    DATABASE_URL: str = "postgresql://admin:admin123@db:5432/techstore"

    # Redis
    REDIS_URL: str = "redis://redis:6379"

    # CORS
    CORS_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:8000",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:8000",
    ]

    # Elasticsearch
    ELASTICSEARCH_URL: Optional[str] = None

    # Внешние API
    CURRENCY_API_KEY: Optional[str] = None
    SHIPPING_API_KEY: Optional[str] = None

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
