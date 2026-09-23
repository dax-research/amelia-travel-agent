"""Notification delivery provider integration client."""

import logging
from typing import Any, Dict
from app.integrations.base import BaseIntegrationClient

logger = logging.getLogger("NotificationProvider")


class NotificationProvider(BaseIntegrationClient):
    """Client for dispatching push notifications, SMS alerts, and traveler emails."""

    def __init__(self) -> None:
        super().__init__(base_url="https://api.notifications.example.com/v1")

    async def send_push_alert(self, user_id: str, title: str, message: str) -> Dict[str, Any]:
        """Dispatch a high-priority push notification to traveler mobile app."""
        logger.info("Dispatching PUSH to user %s: [%s] %s", user_id, title, message)
        return {
            "status": "delivered",
            "channel": "push",
            "user_id": user_id,
            "title": title,
        }

    async def send_sms_alert(self, phone_number: str, message: str) -> Dict[str, Any]:
        """Dispatch an SMS text alert for urgent travel disruptions."""
        logger.info("Dispatching SMS to %s: %s", phone_number, message)
        return {
            "status": "delivered",
            "channel": "sms",
            "recipient": phone_number,
        }


notification_provider = NotificationProvider()
