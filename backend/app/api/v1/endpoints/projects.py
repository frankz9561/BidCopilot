from __future__ import annotations

from fastapi import APIRouter, status

from app.schemas.projects import ProjectCreate, ProjectRead, ProjectUpdate
from app.utils.ids import new_id
from app.utils.time import utcnow

router = APIRouter(prefix="/projects", tags=["projects"])


@router.get("", response_model=list[ProjectRead])
async def list_projects() -> list[ProjectRead]:
    return []


@router.post("", response_model=ProjectRead, status_code=status.HTTP_201_CREATED)
async def create_project(payload: ProjectCreate) -> ProjectRead:
    now = utcnow()
    return ProjectRead(
        id=new_id("proj"),
        name=payload.name,
        rfp_doc_id=payload.rfp_doc_id,
        status=payload.status,
        metadata=payload.metadata,
        created_at=now,
        updated_at=now,
    )


@router.get("/{project_id}", response_model=ProjectRead)
async def get_project(project_id: str) -> ProjectRead:
    now = utcnow()
    return ProjectRead(
        id=project_id,
        name="",
        rfp_doc_id=None,
        status="active",
        metadata=None,
        created_at=now,
        updated_at=now,
    )


@router.patch("/{project_id}", response_model=ProjectRead)
async def update_project(project_id: str, payload: ProjectUpdate) -> ProjectRead:
    now = utcnow()
    return ProjectRead(
        id=project_id,
        name=payload.name or "",
        rfp_doc_id=payload.rfp_doc_id,
        status=payload.status or "active",
        metadata=payload.metadata,
        created_at=now,
        updated_at=now,
    )
