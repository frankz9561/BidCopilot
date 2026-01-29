from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class AppState:
    local_token: str | None
    port: int | None
    started_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
