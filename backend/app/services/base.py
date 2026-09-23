"""Base service with common operational utilities."""

import logging
from typing import Any, Dict


class BaseService:
    """Abstract base class for domain business services."""

    def __init__(self) -> None:
        self.logger = logging.getLogger(self.__class__.__name__)

    def log_action(self, action: str, details: Dict[str, Any]) -> None:
        """Structured audit/diagnostic logging."""
        self.logger.info("Action: %s | Details: %s", action, details)
