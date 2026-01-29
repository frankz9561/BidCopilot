from __future__ import annotations

from fastapi import APIRouter, status

from app.schemas.documents import DocumentCreate, DocumentRead, DocumentUpdate
from app.utils.ids import new_id
from app.utils.time import utcnow

router = APIRouter(prefix="/documents", tags=["documents"])


@router.get("", response_model=list[DocumentRead])
async def list_documents() -> list[DocumentRead]:
    return []


@router.post("", response_model=DocumentRead, status_code=status.HTTP_201_CREATED)
async def create_document(payload: DocumentCreate) -> DocumentRead:
    now = utcnow()
    return DocumentRead(
        id=new_id("doc"),
        project_id=payload.project_id,
        name=payload.name,
        file_path=payload.file_path,
        file_hash=payload.file_hash,
        file_size=payload.file_size,
        category=payload.category,
        status=payload.status,
        total_chunks=payload.total_chunks,
        metadata=payload.metadata,
        created_at=now,
        updated_at=now,
    )


@router.get("/{document_id}", response_model=DocumentRead)
async def get_document(document_id: str) -> DocumentRead:
    now = utcnow()
    return DocumentRead(
        id=document_id,
        project_id=None,
        name="",
        file_path="",
        file_hash=None,
        file_size=None,
        category=None,
        status="processing",
        total_chunks=None,
        metadata=None,
        created_at=now,
        updated_at=now,
    )


@router.patch("/{document_id}", response_model=DocumentRead)
async def update_document(document_id: str, payload: DocumentUpdate) -> DocumentRead:
    now = utcnow()
    return DocumentRead(
        id=document_id,
        project_id=None,
        name=payload.name or "",
        file_path="",
        file_hash=None,
        file_size=None,
        category=payload.category,
        status=payload.status or "processing",
        total_chunks=None,
        metadata=payload.metadata,
        created_at=now,
        updated_at=now,
    )
