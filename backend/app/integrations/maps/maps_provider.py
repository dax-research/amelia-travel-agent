"""Google Maps and Places provider integration client."""

from typing import Any, Dict, List
from app.core.config import settings
from app.integrations.base import BaseIntegrationClient


class MapsProvider(BaseIntegrationClient):
    """Client for Google Maps, Places, and distance calculation."""

    def __init__(self) -> None:
        super().__init__(
            base_url="https://maps.googleapis.com/maps/api",
            api_key=settings.GOOGLE_MAPS_API_KEY,
        )

    async def search_places(self, query: str, location: str) -> List[Dict[str, Any]]:
        """Find places of interest or points of interest in a city."""
        return [
            {
                "name": f"Historic Old Town of {location.title()}",
                "category": "sightseeing",
                "rating": 4.9,
                "address": f"Center, {location.title()}",
                "recommended_time_mins": 120,
            },
            {
                "name": f"{location.title()} Botanical Gardens & Museum",
                "category": "museum",
                "rating": 4.7,
                "address": f"North District, {location.title()}",
                "recommended_time_mins": 90,
            },
        ]

    async def calculate_transit_time(self, origin: str, destination: str) -> Dict[str, Any]:
        """Estimate transit travel time between two coordinates or landmarks."""
        return {
            "origin": origin,
            "destination": destination,
            "duration_minutes": 25,
            "distance_km": 8.5,
            "transit_mode": "metro",
        }


maps_provider = MapsProvider()
