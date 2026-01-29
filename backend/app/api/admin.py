from __future__ import annotations

from fastapi import APIRouter

from app.schemas.common import MessageResponse

router = APIRouter(prefix="/admin", tags=["admin"])


@router.post("/shutdown", response_model=MessageResponse)
async def shutdown() -> MessageResponse:
    return MessageResponse(status="ok", message="Shutdown requested")
