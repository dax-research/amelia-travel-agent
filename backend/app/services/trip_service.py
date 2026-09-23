"""Business logic service for trip and itinerary management."""

from datetime import datetime, timezone
from typing import Dict, List, Optional
from fastapi import HTTPException, status

from app.schemas.trip import (
    ItineraryDay,
    ItineraryItem,
    TripCreate,
    TripResponse,
    TripUpdate,
)
from app.services.base import BaseService


class TripService(BaseService):
    """Manages creation, itinerary generation, and tracking of trips."""

    _mock_trips: Dict[str, dict] = {}

    def create_trip(self, user_id: str, payload: TripCreate) -> TripResponse:
        """Create a new trip with an initial auto-scaffolded itinerary day."""
        trip_id = f"trip_{len(self._mock_trips) + 1:04d}"
        now = datetime.now(timezone.utc)

        # Initial placeholder itinerary day
        initial_day = ItineraryDay(
            day_number=1,
            date=payload.start_date,
            theme="Arrival & Settling In",
            items=[
                ItineraryItem(
                    time="14:00",
                    title=f"Arrive in {payload.destination}",
                    description="Check-in to accommodation and unpack.",
                    category="hotel",
                ),
                ItineraryItem(
                    time="18:30",
                    title="Welcome Dinner",
                    description="Enjoy local culinary specialty downtown.",
                    category="dining",
                ),
            ],
        )

        trip_record = {
            "id": trip_id,
            "user_id": user_id,
            "destination": payload.destination,
            "origin": payload.origin,
            "start_date": payload.start_date,
            "end_date": payload.end_date,
            "budget": payload.budget,
            "travelers_count": payload.travelers_count,
            "preferences": payload.preferences,
            "status": "planned",
            "itinerary": [initial_day.model_dump()],
            "created_at": now,
            "updated_at": now,
        }

        self._mock_trips[trip_id] = trip_record
        self.log_action("trip_created", {"trip_id": trip_id, "destination": payload.destination})
        return TripResponse(**trip_record)

    def list_user_trips(self, user_id: str) -> List[TripResponse]:
        """List all trips belonging to the authenticated user."""
        trips = [
            TripResponse(**record)
            for record in self._mock_trips.values()
            if record["user_id"] == user_id
        ]
        return trips

    def get_trip(self, user_id: str, trip_id: str) -> TripResponse:
        """Retrieve a single trip by ID."""
        record = self._mock_trips.get(trip_id)
        if not record or record["user_id"] != user_id:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Trip '{trip_id}' not found.",
            )
        return TripResponse(**record)


trip_service = TripService()
