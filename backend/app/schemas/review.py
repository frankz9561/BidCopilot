from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict


class ReviewReportBase(BaseModel):
    draft_id: str
    missing_citations: list[dict[str, Any]] | None = None
    weak_support: list[dict[str, Any]] | None = None
    overclaims: list[dict[str, Any]] | None = None
    risk_flags: list[dict[str, Any]] | None = None
    suggestions: list[dict[str, Any]] | None = None


class ReviewReportCreate(ReviewReportBase):
    pass


class ReviewReportRead(ReviewReportBase):
    model_config = ConfigDict(from_attributes=True)

    id: str
    created_at: datetime | None = None
