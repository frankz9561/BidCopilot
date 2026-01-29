from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict


class GenerationTaskBase(BaseModel):
    project_id: str | None = None
    draft_id: str | None = None
    task_type: str
    stage: str | None = None
    status: str = "pending"
    input_params: dict[str, Any] | None = None
    prompt_version: str | None = None
    evidence_refs: list[str] | None = None


class GenerationTaskCreate(GenerationTaskBase):
    pass


class GenerationTaskUpdate(BaseModel):
    stage: str | None = None
    status: str | None = None
    output_content: str | None = None
    citations: list[dict[str, Any]] | None = None
    tokens_used: int | None = None
    duration_seconds: float | None = None
    error_message: str | None = None


class GenerationTaskRead(GenerationTaskBase):
    model_config = ConfigDict(from_attributes=True)

    id: str
    output_content: str | None = None
    citations: list[dict[str, Any]] | None = None
    tokens_used: int | None = None
    duration_seconds: float | None = None
    error_message: str | None = None
    created_at: datetime | None = None
