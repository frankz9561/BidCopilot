from __future__ import annotations

from fastapi import APIRouter, status

from app.schemas.templates import TemplateCreate, TemplateMapping, TemplateRead, TemplateUpdate
from app.utils.ids import new_id
from app.utils.time import utcnow

router = APIRouter(prefix="/templates", tags=["templates"])


@router.get("", response_model=list[TemplateRead])
async def list_templates() -> list[TemplateRead]:
    return []


@router.post("", response_model=TemplateRead, status_code=status.HTTP_201_CREATED)
async def create_template(payload: TemplateCreate) -> TemplateRead:
    now = utcnow()
    return TemplateRead(
        id=new_id("tpl"),
        name=payload.name,
        file_path=payload.file_path,
        schema=payload.schema,
        created_at=now,
        updated_at=now,
    )


@router.get("/{template_id}", response_model=TemplateRead)
async def get_template(template_id: str) -> TemplateRead:
    now = utcnow()
    return TemplateRead(
        id=template_id,
        name="",
        file_path="",
        schema=None,
        created_at=now,
        updated_at=now,
    )


@router.patch("/{template_id}", response_model=TemplateRead)
async def update_template(template_id: str, payload: TemplateUpdate) -> TemplateRead:
    now = utcnow()
    return TemplateRead(
        id=template_id,
        name=payload.name or "",
        file_path=payload.file_path or "",
        schema=payload.schema,
        created_at=now,
        updated_at=now,
    )


@router.get("/{template_id}/mapping", response_model=TemplateMapping)
async def get_template_mapping(template_id: str) -> TemplateMapping:
    now = utcnow()
    return TemplateMapping(
        template_id=template_id,
        mapping={},
        validation_rules=None,
        updated_at=now,
    )


@router.put("/{template_id}/mapping", response_model=TemplateMapping)
async def update_template_mapping(
    template_id: str, payload: TemplateMapping
) -> TemplateMapping:
    return TemplateMapping(
        template_id=template_id,
        mapping=payload.mapping,
        validation_rules=payload.validation_rules,
        updated_at=payload.updated_at,
    )
