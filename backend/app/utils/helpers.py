"""General utility helper functions."""

import uuid
from datetime import datetime, timezone
from typing import Any, Dict


def generate_id(prefix: str) -> str:
    """Generate a prefixed unique identifier."""
    return f"{prefix}_{uuid.uuid4().hex[:12]}"


def generate_booking_reference() -> str:
    """Generate a traveler-friendly 6-character alphanumeric booking code."""
    return uuid.uuid4().hex[:6].upper()


def utc_now() -> datetime:
    """Return timezone-aware current UTC timestamp."""
    return datetime.now(timezone.utc)


def format_currency(amount: float, currency: str = "USD") -> str:
    """Format numeric amount into standard currency string."""
    return f"{currency} {amount:,.2f}"
