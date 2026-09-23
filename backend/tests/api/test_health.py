"""Tests for operational health and landing endpoints."""

from app.core.config import settings


def test_health_endpoint(client):
    """Verify GET /health returns 200 and healthy status."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["app_name"] == settings.PROJECT_NAME
    assert "timestamp" in data


def test_root_endpoint(client):
    """Verify GET / landing returns welcome payload."""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "running"
    assert "docs_url" in data
