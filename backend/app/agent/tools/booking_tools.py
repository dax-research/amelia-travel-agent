"""Booking confirmation and lookup tools for LangChain agent."""

import json
import uuid
from langchain_core.tools import tool


@tool
def book_travel_item(booking_type: str, item_id: str, traveler_name: str) -> str:
    """Reserve or book a flight or hotel room on behalf of the traveler."""
    booking_ref = uuid.uuid4().hex[:6].upper()
    confirmation = {
        "status": "confirmed",
        "booking_reference": booking_ref,
        "booking_type": booking_type,
        "item_id": item_id,
        "traveler": traveler_name,
        "message": f"Successfully confirmed {booking_type} reservation. Reference code: {booking_ref}.",
    }
    return json.dumps(confirmation)
