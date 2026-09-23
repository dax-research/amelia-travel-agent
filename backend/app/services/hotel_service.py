"""Business logic service for hotel searches and accommodations."""

from typing import Any, Dict, List
from app.integrations.hotels import hotel_provider
from app.schemas.hotel import HotelOffer, HotelSearchQuery
from app.services.base import BaseService


class HotelService(BaseService):
    """Coordinates hotel accommodation querying and room options."""

    async def search_hotels(self, query: HotelSearchQuery) -> List[Dict[str, Any]]:
        """Search hotels in destination city."""
        self.log_action("search_hotels", {"city": query.city, "check_in": str(query.check_in)})
        return await hotel_provider.search_hotels(
            city=query.city,
            check_in=str(query.check_in),
            check_out=str(query.check_out),
            guests=query.guests,
        )


hotel_service = HotelService()
