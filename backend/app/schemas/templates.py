from __future__ import annotations

from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict


class TemplateBase(BaseModel):
    name: str
    file_path: str
    schema: dict[str, Any] | None = None


class TemplateCreate(TemplateBase):
    pass


class TemplateUpdate(BaseModel):
    name: str | None = None
    file_path: str | None = None
    schema: dict[str, Any] | None = None


class TemplateRead(TemplateBase):
    model_config = ConfigDict(from_attributes=True)

    id: str
    created_at: datetime | None = None
    updated_at: datetime | None = None


class TemplateMapping(BaseModel):
    template_id: str
    mapping: dict[str, Any]
    validation_rules: dict[str, Any] | None = None
    updated_at: datetime | None = None
