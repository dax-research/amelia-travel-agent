"""Notifications integration package exports."""

from app.integrations.notifications.notification_provider import (
    NotificationProvider,
    notification_provider,
)

__all__ = ["NotificationProvider", "notification_provider"]
