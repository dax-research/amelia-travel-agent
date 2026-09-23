"""Hotel accommodations search tools for LangChain agent."""

import json
from langchain_core.tools import tool


@tool
def search_hotels(city: str, check_in: str, check_out: str) -> str:
    """Search for hotels in a specified city with check-in and check-out dates."""
    hotels = [
        {
            "hotel_id": f"HTL_{city.lower().replace(' ', '_')}_1",
            "name": f"Grand Central {city.title()}",
            "city": city.title(),
            "star_rating": 4.8,
            "price_per_night_usd": 210.0,
            "amenities": ["Free High-Speed WiFi", "Breakfast Included", "Fitness Center"],
        },
        {
            "hotel_id": f"HTL_{city.lower().replace(' ', '_')}_2",
            "name": f"Heritage Boutique Hotel {city.title()}",
            "city": city.title(),
            "star_rating": 4.5,
            "price_per_night_usd": 150.0,
            "amenities": ["City Center", "Rooftop Restaurant", "Free WiFi"],
        },
    ]
    return json.dumps(hotels)
