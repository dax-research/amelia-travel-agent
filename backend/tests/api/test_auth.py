"""Tests for authentication and registration endpoints."""


def test_user_registration_and_login(client):
    """Verify traveler registration and login with JWT issuance."""
    test_email = "auth_traveler@test.com"
    reg_payload = {
        "email": test_email,
        "password": "SecurePassword123!",
        "full_name": "Auth Traveler",
    }
    reg_res = client.post("/api/auth/register", json=reg_payload)
    assert reg_res.status_code == 201
    assert reg_res.json()["data"]["email"] == test_email

    login_res = client.post(
        "/api/auth/login",
        json={"email": test_email, "password": "SecurePassword123!"},
    )
    assert login_res.status_code == 200
    token_data = login_res.json()
    assert "access_token" in token_data
    assert token_data["token_type"] == "bearer"
