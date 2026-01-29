from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict


class ProjectBase(BaseModel):
    name: str
    rfp_doc_id: str | None = None
    status: str = "active"
    metadata: dict[str, Any] | None = None


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(BaseModel):
    name: str | None = None
    rfp_doc_id: str | None = None
    status: str | None = None
    metadata: dict[str, Any] | None = None


class ProjectRead(ProjectBase):
    model_config = ConfigDict(from_attributes=True)

    id: str
    created_at: datetime | None = None
    updated_at: datetime | None = None
