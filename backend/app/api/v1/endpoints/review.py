from __future__ import annotations

from fastapi import APIRouter, status

from app.schemas.review import ReviewReportCreate, ReviewReportRead
from app.utils.ids import new_id
from app.utils.time import utcnow

router = APIRouter(prefix="/review", tags=["review"])


@router.get("/{draft_id}", response_model=ReviewReportRead)
async def get_review_report(draft_id: str) -> ReviewReportRead:
    now = utcnow()
    return ReviewReportRead(
        id=new_id("review"),
        draft_id=draft_id,
        missing_citations=None,
        weak_support=None,
        overclaims=None,
        risk_flags=None,
        suggestions=None,
        created_at=now,
    )


@router.post("", response_model=ReviewReportRead, status_code=status.HTTP_201_CREATED)
async def create_review_report(payload: ReviewReportCreate) -> ReviewReportRead:
    now = utcnow()
    return ReviewReportRead(
        id=new_id("review"),
        draft_id=payload.draft_id,
        missing_citations=payload.missing_citations,
        weak_support=payload.weak_support,
        overclaims=payload.overclaims,
        risk_flags=payload.risk_flags,
        suggestions=payload.suggestions,
        created_at=now,
    )
