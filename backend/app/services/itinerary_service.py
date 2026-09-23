"""Business logic service for itinerary planning, schedule adjustments, and activity inserts."""

from datetime import datetime
from typing import Dict, List
from fastapi import HTTPException, status

from app.schemas.itinerary import (
    ItineraryDayDetail,
    ItineraryGenerateRequest,
    ItineraryItemBase,
    ItineraryItemCreate,
    ItineraryResponse,
)
from app.services.base import BaseService
from app.utils.helpers import utc_now


class ItineraryService(BaseService):
    """Orchestrates multi-day itinerary generation and item operations."""

    _itineraries: Dict[str, dict] = {}

    def generate_itinerary(self, req: ItineraryGenerateRequest) -> ItineraryResponse:
        """Generate a tailored multi-day itinerary matching traveler interests."""
        days: List[ItineraryDayDetail] = []
        for day_idx in range(1, req.days + 1):
            day_items = [
                ItineraryItemBase(
                    time="09:30",
                    title=f"Morning Cultural Walk & Architecture Tour in {req.destination}",
                    description=f"Explore historic landmarks matching interests: {', '.join(req.interests) if req.interests else 'General highlights'}.",
                    category="activity",
                    estimated_duration_mins=120,
                    cost_estimate=25.0,
                ),
                ItineraryItemBase(
                    time="12:30",
                    title="Authentic Local Cuisine Lunch",
                    description="Recommended artisan culinary dining in downtown district.",
                    category="dining",
                    estimated_duration_mins=75,
                    cost_estimate=35.0,
                ),
                ItineraryItemBase(
                    time="15:00",
                    title=f"Afternoon Excursion & Scenic Views",
                    description="Guided experience with photo stops and local artisan market.",
                    category="activity",
                    estimated_duration_mins=90,
                    cost_estimate=20.0,
                ),
            ]
            days.append(
                ItineraryDayDetail(
                    day_number=day_idx,
                    theme=f"Day {day_idx}: Discovering {req.destination}",
                    items=day_items,
                )
            )

        itinerary_data = {
            "trip_id": req.trip_id,
            "destination": req.destination,
            "total_days": req.days,
            "days": [d.model_dump() for d in days],
            "generated_at": utc_now(),
        }
        self._itineraries[req.trip_id] = itinerary_data
        self.log_action("itinerary_generated", {"trip_id": req.trip_id, "days": req.days})
        return ItineraryResponse(**itinerary_data)

    def get_itinerary(self, trip_id: str) -> ItineraryResponse:
        """Retrieve itinerary for a specific trip."""
        data = self._itineraries.get(trip_id)
        if not data:
            # Generate default 3-day itinerary on the fly if not yet persisted
            return self.generate_itinerary(
                ItineraryGenerateRequest(trip_id=trip_id, destination="Destination", days=3)
            )
        return ItineraryResponse(**data)

    def add_item_to_day(self, trip_id: str, day_number: int, item: ItineraryItemCreate) -> ItineraryResponse:
        """Add an activity item to a specific day of the itinerary."""
        itinerary = self.get_itinerary(trip_id)
        data = itinerary.model_dump()
        day_found = False
        for day in data["days"]:
            if day["day_number"] == day_number:
                day["items"].append(item.model_dump())
                day_found = True
                break
        if not day_found:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Day {day_number} not found in trip itinerary.",
            )
        self._itineraries[trip_id] = data
        return ItineraryResponse(**data)


itinerary_service = ItineraryService()
