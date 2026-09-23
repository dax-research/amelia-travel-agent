"""Business logic service for traveler notifications and guardian alerts."""

from typing import Dict, List
from app.integrations.notifications import notification_provider
from app.schemas.notification import (
    NotificationChannel,
    NotificationCreate,
    NotificationPriority,
    NotificationResponse,
)
from app.services.base import BaseService
from app.utils.helpers import generate_id, utc_now


class NotificationService(BaseService):
    """Manages creation, routing, and history of guardian notifications."""

    _notifications: Dict[str, dict] = {}

    async def send_notification(self, payload: NotificationCreate) -> NotificationResponse:
        """Route notification to appropriate delivery provider and log record."""
        notification_id = generate_id("ntf")
        now = utc_now()

        # If priority is critical or channel is push/sms, trigger integration client
        if payload.channel == NotificationChannel.PUSH or payload.priority == NotificationPriority.CRITICAL:
            await notification_provider.send_push_alert(
                user_id=payload.user_id,
                title=payload.title,
                message=payload.message,
            )

        record = {
            "id": notification_id,
            "user_id": payload.user_id,
            "title": payload.title,
            "message": payload.message,
            "priority": payload.priority,
            "channel": payload.channel,
            "is_read": False,
            "created_at": now,
        }
        self._notifications[notification_id] = record
        self.log_action("notification_dispatched", {"id": notification_id, "user_id": payload.user_id})
        return NotificationResponse(**record)

    def list_user_notifications(self, user_id: str) -> List[NotificationResponse]:
        """List notifications for a specific user ordered by timestamp."""
        user_ntfs = [
            NotificationResponse(**record)
            for record in self._notifications.values()
            if record["user_id"] == user_id
        ]
        user_ntfs.sort(key=lambda n: n.created_at, reverse=True)
        return user_ntfs


notification_service = NotificationService()
