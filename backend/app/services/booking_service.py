"""Business logic service for unified travel bookings (flight, hotel, activities)."""

from typing import Dict, List, Optional
from fastapi import HTTPException, status

from app.schemas.booking import BookingCreate, BookingResponse, BookingStatus, BookingType
from app.services.base import BaseService
from app.utils.helpers import generate_booking_reference, generate_id, utc_now


class BookingService(BaseService):
    """Manages creation, verification, and cancellation of bookings."""

    _bookings: Dict[str, dict] = {}

    def create_booking(self, user_id: str, payload: BookingCreate) -> BookingResponse:
        """Create a confirmed travel booking record."""
        booking_id = generate_id("bk")
        ref_code = generate_booking_reference()
        now = utc_now()

        booking_record = {
            "id": booking_id,
            "user_id": user_id,
            "trip_id": payload.trip_id,
            "booking_reference": ref_code,
            "booking_type": payload.booking_type,
            "status": BookingStatus.CONFIRMED,
            "total_amount": payload.total_amount,
            "currency": payload.currency,
            "details": payload.details,
            "created_at": now,
            "updated_at": now,
        }
        self._bookings[booking_id] = booking_record
        self.log_action("booking_created", {"booking_id": booking_id, "ref": ref_code})
        return BookingResponse(**booking_record)

    def list_user_bookings(self, user_id: str) -> List[BookingResponse]:
        """List all bookings for a user."""
        return [
            BookingResponse(**record)
            for record in self._bookings.values()
            if record["user_id"] == user_id
        ]

    def cancel_booking(self, user_id: str, booking_id: str) -> BookingResponse:
        """Cancel an existing booking."""
        record = self._bookings.get(booking_id)
        if not record or record["user_id"] != user_id:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Booking '{booking_id}' not found.",
            )
        record["status"] = BookingStatus.CANCELLED
        record["updated_at"] = utc_now()
        self._bookings[booking_id] = record
        self.log_action("booking_cancelled", {"booking_id": booking_id})
        return BookingResponse(**record)


booking_service = BookingService()
