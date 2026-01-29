from __future__ import annotations

from fastapi import APIRouter

from app.api.v1.endpoints import (
    documents,
    generation,
    projects,
    requirements,
    review,
    templates,
)

api_router = APIRouter()

api_router.include_router(projects.router)
api_router.include_router(documents.router)
api_router.include_router(requirements.router)
api_router.include_router(generation.router)
api_router.include_router(review.router)
api_router.include_router(templates.router)
