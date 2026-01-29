from __future__ import annotations

from functools import lru_cache
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="BIDCOPILOT_",
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "BidCopilot"
    env: str = Field(default="dev", description="Environment name")
    host: str = "127.0.0.1"
    port: int = 8765
    log_level: str = "info"
    allowed_origins: list[str] = ["*"]

    data_dir: Path = Path("data")
    sqlite_path: Path = Path("data/db.sqlite")

    # Local-only token for IPC protection; if None, token checks are skipped.
    local_token: str | None = None


@lru_cache
def get_settings() -> Settings:
    return Settings()
