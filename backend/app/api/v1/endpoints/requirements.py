from __future__ import annotations

from fastapi import APIRouter, status

from app.schemas.requirements import (
    RequirementCreate,
    RequirementRead,
    RequirementUpdate,
)
from app.utils.ids import new_id
from app.utils.time import utcnow

router = APIRouter(prefix="/requirements", tags=["requirements"])


@router.get("", response_model=list[RequirementRead])
async def list_requirements() -> list[RequirementRead]:
    return []


@router.post("", response_model=RequirementRead, status_code=status.HTTP_201_CREATED)
async def create_requirement(payload: RequirementCreate) -> RequirementRead:
    now = utcnow()
    return RequirementRead(
        id=new_id("req"),
        project_id=payload.project_id,
        section=payload.section,
        requirement_text=payload.requirement_text,
        score_weight=payload.score_weight,
        risk_level=payload.risk_level,
        status=payload.status,
        source_chunk_ids=payload.source_chunk_ids,
        metadata=payload.metadata,
        created_at=now,
    )


@router.get("/{requirement_id}", response_model=RequirementRead)
async def get_requirement(requirement_id: str) -> RequirementRead:
    now = utcnow()
    return RequirementRead(
        id=requirement_id,
        project_id="",
        section=None,
        requirement_text="",
        score_weight=None,
        risk_level=None,
        status="open",
        source_chunk_ids=None,
        metadata=None,
        created_at=now,
    )


@router.patch("/{requirement_id}", response_model=RequirementRead)
async def update_requirement(
    requirement_id: str, payload: RequirementUpdate
) -> RequirementRead:
    now = utcnow()
    return RequirementRead(
        id=requirement_id,
        project_id="",
        section=payload.section,
        requirement_text=payload.requirement_text or "",
        score_weight=payload.score_weight,
        risk_level=payload.risk_level,
        status=payload.status or "open",
        source_chunk_ids=payload.source_chunk_ids,
        metadata=payload.metadata,
        created_at=now,
    )
