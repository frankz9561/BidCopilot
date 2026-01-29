from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict


class RequirementBase(BaseModel):
    project_id: str
    section: str | None = None
    requirement_text: str
    score_weight: float | None = None
    risk_level: str | None = None
    status: str = "open"
    source_chunk_ids: list[str] | None = None
    metadata: dict[str, Any] | None = None


class RequirementCreate(RequirementBase):
    pass


class RequirementUpdate(BaseModel):
    section: str | None = None
    requirement_text: str | None = None
    score_weight: float | None = None
    risk_level: str | None = None
    status: str | None = None
    source_chunk_ids: list[str] | None = None
    metadata: dict[str, Any] | None = None


class RequirementRead(RequirementBase):
    model_config = ConfigDict(from_attributes=True)

    id: str
    created_at: datetime | None = None
