from __future__ import annotations

from fastapi import APIRouter, status

from app.schemas.generation import (
    GenerationTaskCreate,
    GenerationTaskRead,
    GenerationTaskUpdate,
)
from app.utils.ids import new_id
from app.utils.time import utcnow

router = APIRouter(prefix="/generation", tags=["generation"])


@router.get("", response_model=list[GenerationTaskRead])
async def list_generation_tasks() -> list[GenerationTaskRead]:
    return []


@router.post("", response_model=GenerationTaskRead, status_code=status.HTTP_201_CREATED)
async def create_generation_task(payload: GenerationTaskCreate) -> GenerationTaskRead:
    now = utcnow()
    return GenerationTaskRead(
        id=new_id("task"),
        project_id=payload.project_id,
        draft_id=payload.draft_id,
        task_type=payload.task_type,
        stage=payload.stage,
        status=payload.status,
        input_params=payload.input_params,
        prompt_version=payload.prompt_version,
        evidence_refs=payload.evidence_refs,
        output_content=None,
        citations=None,
        tokens_used=None,
        duration_seconds=None,
        error_message=None,
        created_at=now,
    )


@router.get("/{task_id}", response_model=GenerationTaskRead)
async def get_generation_task(task_id: str) -> GenerationTaskRead:
    now = utcnow()
    return GenerationTaskRead(
        id=task_id,
        project_id=None,
        draft_id=None,
        task_type="",
        stage=None,
        status="pending",
        input_params=None,
        prompt_version=None,
        evidence_refs=None,
        output_content=None,
        citations=None,
        tokens_used=None,
        duration_seconds=None,
        error_message=None,
        created_at=now,
    )


@router.patch("/{task_id}", response_model=GenerationTaskRead)
async def update_generation_task(
    task_id: str, payload: GenerationTaskUpdate
) -> GenerationTaskRead:
    now = utcnow()
    return GenerationTaskRead(
        id=task_id,
        project_id=None,
        draft_id=None,
        task_type="",
        stage=payload.stage,
        status=payload.status or "pending",
        input_params=None,
        prompt_version=None,
        evidence_refs=None,
        output_content=payload.output_content,
        citations=payload.citations,
        tokens_used=payload.tokens_used,
        duration_seconds=payload.duration_seconds,
        error_message=payload.error_message,
        created_at=now,
    )
