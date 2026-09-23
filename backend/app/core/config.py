"""Application configuration using Pydantic BaseSettings."""

from typing import List, Union
from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment or defaults."""

    # Project Information
    PROJECT_NAME: str = "AI Travel Concierge & Smart Travel Guardian"
    VERSION: str = "0.1.0"
    API_V1_PREFIX: str = "/api"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True

    # Security & JWT
    SECRET_KEY: str = "super-secret-guardian-jwt-key-2026-travel-concierge"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24 hours for dev

    # CORS Configuration
    ALLOWED_ORIGINS: Union[List[str], str] = [
        "http://localhost:3000",
        "http://localhost:8000",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:8000",
        "*",
    ]

    @field_validator("ALLOWED_ORIGINS", mode="before")
    @classmethod
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> List[str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",") if i.strip()]
        elif isinstance(v, (list, str)):
            return v  # type: ignore
        return ["*"]

    # AI & External Integrations
    OPENAI_API_KEY: Union[str, None] = None
    OPENAI_MODEL: str = "gpt-4o-mini"
    WEATHER_API_KEY: Union[str, None] = None
    AMADEUS_API_KEY: Union[str, None] = None
    AMADEUS_API_SECRET: Union[str, None] = None
    GOOGLE_MAPS_API_KEY: Union[str, None] = None

    model_config = SettingsConfigDict(
        env_file=(".env", "../.env"),
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )


# Singleton settings instance
settings = Settings()
