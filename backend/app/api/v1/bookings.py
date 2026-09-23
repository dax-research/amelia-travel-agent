"""Unified travel bookings management endpoints."""

from typing import List
from fastapi import APIRouter, Depends, status
from app.core.dependencies import get_current_user_id
from app.schemas.booking import BookingCreate, BookingResponse
from app.schemas.common import ApiResponse
from app.services.booking_service import booking_service

router = APIRouter(prefix="/bookings", tags=["Bookings"])


@router.post(
    "",
    response_model=ApiResponse[BookingResponse],
    status_code=status.HTTP_201_CREATED,
    summary="Create a new booking (flight, hotel, or activity)",
)
async def create_booking(
    payload: BookingCreate,
    user_id: str = Depends(get_current_user_id),
) -> ApiResponse[BookingResponse]:
    """Reserve travel item and issue instant confirmation code."""
    booking = booking_service.create_booking(user_id=user_id, payload=payload)
    return ApiResponse(
        success=True,
        message="Booking confirmed successfully.",
        data=booking,
    )


@router.get(
    "",
    response_model=ApiResponse[List[BookingResponse]],
    summary="List all bookings for authenticated traveler",
)
async def list_my_bookings(
    user_id: str = Depends(get_current_user_id),
) -> ApiResponse[List[BookingResponse]]:
    """Retrieve history of active and completed travel reservations."""
    bookings = booking_service.list_user_bookings(user_id=user_id)
    return ApiResponse(
        success=True,
        message=f"Retrieved {len(bookings)} bookings.",
        data=bookings,
    )


@router.delete(
    "/{booking_id}",
    response_model=ApiResponse[BookingResponse],
    summary="Cancel a booking",
)
async def cancel_booking(
    booking_id: str,
    user_id: str = Depends(get_current_user_id),
) -> ApiResponse[BookingResponse]:
    """Cancel confirmed reservation."""
    cancelled = booking_service.cancel_booking(user_id=user_id, booking_id=booking_id)
    return ApiResponse(
        success=True,
        message="Booking cancelled successfully.",
        data=cancelled,
    )
