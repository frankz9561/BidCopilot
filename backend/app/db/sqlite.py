from __future__ import annotations

from pathlib import Path

from app.core.config import get_settings


def ensure_sqlite_path() -> Path:
    settings = get_settings()
    settings.data_dir.mkdir(parents=True, exist_ok=True)
    if not settings.sqlite_path.exists():
        settings.sqlite_path.touch()
    return settings.sqlite_path
