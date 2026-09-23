"""Pytest shared fixtures and test client configuration."""

import pytest
from starlette.testclient import TestClient
from app.main import app


@pytest.fixture(scope="session")
def client():
    """Shared TestClient instance for API tests."""
    with TestClient(app) as test_client:
        yield test_client
