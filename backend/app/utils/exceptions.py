"""Domain exceptions for AI Travel Concierge & Smart Travel Guardian."""

from typing import Any, Dict, Optional


class TravelGuardianException(Exception):
    """Base exception for application domain errors."""

    def __init__(self, message: str, code: str = "GUARDIAN_ERROR", details: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(message)
        self.message = message
        self.code = code
        self.details = details or {}


class BookingException(TravelGuardianException):
    """Raised when a reservation or booking transaction fails."""

    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(message, code="BOOKING_FAILED", details=details)


class DisruptionException(TravelGuardianException):
    """Raised when an unrecoverable travel disruption occurs."""

    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None) -> None:
        super().__init__(message, code="DISRUPTION_DETECTED", details=details)


class IntegrationException(TravelGuardianException):
    """Raised when an external travel API provider fails."""

    def __init__(self, message: str, provider: str, details: Optional[Dict[str, Any]] = None) -> None:
        merged_details = details or {}
        merged_details["provider"] = provider
        super().__init__(message, code="PROVIDER_ERROR", details=merged_details)
