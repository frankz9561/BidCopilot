from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict


class DocumentBase(BaseModel):
    project_id: str | None = None
    name: str
    file_path: str
    file_hash: str | None = None
    file_size: int | None = None
    category: str | None = None
    status: str = "processing"
    total_chunks: int | None = None
    metadata: dict[str, Any] | None = None


class DocumentCreate(DocumentBase):
    pass


class DocumentUpdate(BaseModel):
    name: str | None = None
    category: str | None = None
    status: str | None = None
    metadata: dict[str, Any] | None = None


class DocumentRead(DocumentBase):
    model_config = ConfigDict(from_attributes=True)

    id: str
    created_at: datetime | None = None
    updated_at: datetime | None = None
