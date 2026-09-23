"""Hotel search and accommodations endpoints."""

from datetime import date
from typing import Any, Dict, List
from fastapi import APIRouter, Query
from app.schemas.common import ApiResponse
from app.schemas.hotel import HotelSearchQuery
from app.services.hotel_service import hotel_service

router = APIRouter(prefix="/hotels", tags=["Hotels"])


@router.get(
    "/search",
    response_model=ApiResponse[List[Dict[str, Any]]],
    summary="Search hotel accommodations",
)
async def search_hotels(
    city: str = Query(..., description="Destination city name"),
    check_in: date = Query(..., description="Check-in date YYYY-MM-DD"),
    check_out: date = Query(..., description="Check-out date YYYY-MM-DD"),
    guests: int = Query(default=1, ge=1),
) -> ApiResponse[List[Dict[str, Any]]]:
    """Search hotels by city, dates, and number of guests."""
    query = HotelSearchQuery(city=city, check_in=check_in, check_out=check_out, guests=guests)
    hotels = await hotel_service.search_hotels(query)
    return ApiResponse(
        success=True,
        message=f"Found {len(hotels)} hotels in {city}.",
        data=hotels,
    )
