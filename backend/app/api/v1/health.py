"""Health check endpoints."""

from datetime import datetime, timezone
from typing import Any, Dict
from fastapi import APIRouter
from app.core.config import settings

router = APIRouter()


@router.get("/health", tags=["Health"])
async def health_check() -> Dict[str, Any]:
    """Verify backend operational readiness."""
    return {
        "status": "healthy",
        "app_name": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "environment": settings.ENVIRONMENT,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
