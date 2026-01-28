def test_register_and_login(client):
    # Register
    r = client.post("/api/v1/auth/register", json={
        "email": "gabriel@test.com",
        "password": "Password123!"
    })
    assert r.status_code == 200
    data = r.json()
    assert "id" in data
    assert data["email"] == "gabriel@test.com"

    # Login
    r = client.post("/api/v1/auth/login", json={
        "email": "gabriel@test.com",
        "password": "Password123!"
    })
    assert r.status_code == 200
    token_data = r.json()
    assert "access_token" in token_data
    assert token_data["token_type"] == "bearer"


def test_register_duplicate_email(client):
    client.post("/api/v1/auth/register", json={
        "email": "dup@test.com",
        "password": "Password123!"
    })
    r = client.post("/api/v1/auth/register", json={
        "email": "dup@test.com",
        "password": "Password123!"
    })
    assert r.status_code == 400
