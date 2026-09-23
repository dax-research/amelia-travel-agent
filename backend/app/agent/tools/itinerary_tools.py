"""Itinerary schedule construction and item management tools for LangChain agent."""

import json
from langchain_core.tools import tool


@tool
def add_itinerary_activity(trip_id: str, day_number: int, time: str, title: str, location: str) -> str:
    """Add a new scheduled activity to a traveler's day itinerary."""
    result = {
        "status": "added",
        "trip_id": trip_id,
        "day_number": day_number,
        "activity": {
            "time": time,
            "title": title,
            "location": location,
        },
        "message": f"Added '{title}' at {time} on Day {day_number}.",
    }
    return json.dumps(result)
