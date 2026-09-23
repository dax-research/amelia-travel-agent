"""Hotel lodging provider integration client."""

from typing import Any, Dict, List
from app.integrations.base import BaseIntegrationClient


class HotelProvider(BaseIntegrationClient):
    """External client for hotel accommodations search and room availability."""

    def __init__(self) -> None:
        super().__init__(base_url="https://api.travel-hotels.example.com/v1")

    async def search_hotels(
        self,
        city: str,
        check_in: str,
        check_out: str,
        guests: int = 1,
    ) -> List[Dict[str, Any]]:
        """Search hotels matching location criteria."""
        return [
            {
                "id": f"htl_{city.lower().replace(' ', '_')}_001",
                "name": f"Grand Royal {city.title()}",
                "city": city.title(),
                "address": f"100 Central Avenue, {city.title()}",
                "star_rating": 4.8,
                "review_score": 9.2,
                "price_per_night": 220.0,
                "currency": "USD",
                "amenities": ["Spa", "Free WiFi", "Pool", "Buffet Breakfast", "Airport Shuttle"],
            },
            {
                "id": f"htl_{city.lower().replace(' ', '_')}_002",
                "name": f"Urban Boutique Stay {city.title()}",
                "city": city.title(),
                "address": f"45 Heritage Boulevard, {city.title()}",
                "star_rating": 4.4,
                "review_score": 8.8,
                "price_per_night": 140.0,
                "currency": "USD",
                "amenities": ["Free WiFi", "Gym", "Rooftop Lounge"],
            },
        ]


hotel_provider = HotelProvider()
