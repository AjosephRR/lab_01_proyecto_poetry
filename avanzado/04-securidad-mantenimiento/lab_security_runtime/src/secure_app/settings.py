from functools import lru_cache
from typing import Literal

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_prefix="APP_",
        env_ignore_empty=True,
        extra="ignore",
        secrets_dir="/run/secrets",
        secrets_dir_missing="ok",
    )

    app_name: str = "secure-runtime-app"
    environment: Literal["local", "dev", "test", "prod"] = "local"
    debug: bool = False
    host: str = "0.0.0.0"
    port: int = 8000
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR"] = "INFO"

    api_key: SecretStr
    database_url: SecretStr

    allowed_origins: list[str] = ["http://localhost:3000"]

    def safe_dict(self) -> dict[str, object]:
        return {
            "app_name": self.app_name,
            "environment": self.environment,
            "debug": self.debug,
            "host": self.host,
            "port": self.port,
            "log_level": self.log_level,
            "allowed_origins": self.allowed_origins,
            "api_key_configured": bool(self.api_key.get_secret_value()),
            "database_url_configured": bool(self.database_url.get_secret_value()),
        }


@lru_cache
def get_settings() -> Settings:
    return Settings()
