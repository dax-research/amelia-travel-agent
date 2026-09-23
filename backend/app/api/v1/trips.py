"""Trip planning and itinerary endpoints."""

from typing import List
from fastapi import APIRouter, Depends, status

from app.core.dependencies import get_current_user_id
from app.schemas.common import ApiResponse
from app.schemas.trip import TripCreate, TripResponse
from app.services.trip_service import trip_service

router = APIRouter(prefix="/trips", tags=["Trips"])


@router.post(
    "",
    response_model=ApiResponse[TripResponse],
    status_code=status.HTTP_201_CREATED,
    summary="Create a new trip",
)
async def create_trip(
    payload: TripCreate,
    user_id: str = Depends(get_current_user_id),
) -> ApiResponse[TripResponse]:
    """Create a new trip with initial itinerary for the authenticated user."""
    trip = trip_service.create_trip(user_id=user_id, payload=payload)
    return ApiResponse(
        success=True,
        message="Trip created successfully.",
        data=trip,
    )


@router.get(
    "",
    response_model=ApiResponse[List[TripResponse]],
    summary="List all trips for the authenticated user",
)
async def list_trips(
    user_id: str = Depends(get_current_user_id),
) -> ApiResponse[List[TripResponse]]:
    """Retrieve all trips associated with the current user."""
    trips = trip_service.list_user_trips(user_id=user_id)
    return ApiResponse(
        success=True,
        message=f"Retrieved {len(trips)} trips.",
        data=trips,
    )


@router.get(
    "/{trip_id}",
    response_model=ApiResponse[TripResponse],
    summary="Get trip details and itinerary",
)
async def get_trip(
    trip_id: str,
    user_id: str = Depends(get_current_user_id),
) -> ApiResponse[TripResponse]:
    """Retrieve full details of a specific trip."""
    trip = trip_service.get_trip(user_id=user_id, trip_id=trip_id)
    return ApiResponse(
        success=True,
        message="Trip retrieved successfully.",
        data=trip,
    )
