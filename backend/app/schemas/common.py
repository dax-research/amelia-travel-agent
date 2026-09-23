"""Common Pydantic request and response schemas."""

from typing import Any, Dict, Generic, List, Optional, TypeVar
from pydantic import BaseModel, Field

DataT = TypeVar("DataT")


class ApiResponse(BaseModel, Generic[DataT]):
    """Standardized API response wrapper."""

    success: bool = True
    message: str = "Operation completed successfully."
    data: Optional[DataT] = None
    meta: Optional[Dict[str, Any]] = None


class ErrorDetail(BaseModel):
    """Detailed error item representation."""

    field: Optional[str] = None
    message: str
    code: Optional[str] = None


class ErrorResponse(BaseModel):
    """Standardized error payload."""

    success: bool = False
    message: str
    errors: Optional[List[ErrorDetail]] = None


class PaginationParams(BaseModel):
    """Query parameters for pagination."""

    page: int = Field(default=1, ge=1, description="Page number (1-indexed)")
    page_size: int = Field(default=20, ge=1, le=100, description="Items per page")


class PaginatedResponse(BaseModel, Generic[DataT]):
    """Standardized paginated list response."""

    items: List[DataT]
    total: int
    page: int
    page_size: int
    pages: int
