"""FastAPI application entry point for AI Travel Concierge & Smart Travel Guardian."""

from datetime import datetime, timezone
from typing import Any, Dict
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings

# Initialize FastAPI Application
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description="Autonomous AI Travel Concierge & Smart Travel Guardian backend API.",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

# Configure CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS if isinstance(settings.ALLOWED_ORIGINS, list) else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", tags=["Health"])
async def health_check() -> Dict[str, Any]:
    """Health check endpoint to verify backend operational readiness."""
    return {
        "status": "healthy",
        "app_name": settings.PROJECT_NAME,
        "version": settings.VERSION,
        "environment": settings.ENVIRONMENT,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@app.get("/", tags=["Root"])
async def root() -> Dict[str, Any]:
    """Root landing endpoint with system information and links."""
    return {
        "message": f"Welcome to {settings.PROJECT_NAME}",
        "version": settings.VERSION,
        "docs_url": "/docs",
        "health_url": "/health",
        "status": "running",
    }


from app.api.router import api_router

# Mount Central Modular API Router
app.include_router(api_router, prefix=settings.API_V1_PREFIX)

