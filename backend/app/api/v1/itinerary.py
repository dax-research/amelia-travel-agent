"""Trip itinerary generation and scheduling endpoints."""

from fastapi import APIRouter, Depends, status
from app.core.dependencies import get_current_user_id
from app.schemas.common import ApiResponse
from app.schemas.itinerary import (
    ItineraryGenerateRequest,
    ItineraryItemCreate,
    ItineraryResponse,
)
from app.services.itinerary_service import itinerary_service

router = APIRouter(prefix="/itinerary", tags=["Itinerary"])


@router.post(
    "/generate",
    response_model=ApiResponse[ItineraryResponse],
    summary="Auto-generate optimized multi-day itinerary with AI Concierge",
)
async def generate_itinerary(
    payload: ItineraryGenerateRequest,
    user_id: str = Depends(get_current_user_id),
) -> ApiResponse[ItineraryResponse]:
    """Generate curated schedule matching destination, duration, and traveler style."""
    itinerary = itinerary_service.generate_itinerary(payload)
    return ApiResponse(
        success=True,
        message="Itinerary generated successfully.",
        data=itinerary,
    )


@router.get(
    "/{trip_id}",
    response_model=ApiResponse[ItineraryResponse],
    summary="Get detailed daily itinerary for a trip",
)
async def get_itinerary(
    trip_id: str,
    user_id: str = Depends(get_current_user_id),
) -> ApiResponse[ItineraryResponse]:
    """Retrieve day-by-day itemized schedule."""
    itinerary = itinerary_service.get_itinerary(trip_id)
    return ApiResponse(
        success=True,
        message="Itinerary retrieved successfully.",
        data=itinerary,
    )


@router.post(
    "/{trip_id}/days/{day_number}/items",
    response_model=ApiResponse[ItineraryResponse],
    status_code=status.HTTP_201_CREATED,
    summary="Add a custom activity item to an itinerary day",
)
async def add_item_to_day(
    trip_id: str,
    day_number: int,
    item: ItineraryItemCreate,
    user_id: str = Depends(get_current_user_id),
) -> ApiResponse[ItineraryResponse]:
    """Insert an activity, dining experience, or stop into a specific day's schedule."""
    updated = itinerary_service.add_item_to_day(trip_id, day_number, item)
    return ApiResponse(
        success=True,
        message=f"Added '{item.title}' to Day {day_number}.",
        data=updated,
    )
