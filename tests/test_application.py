def register_and_login(client, email: str, password: str) -> str:
    client.post("/api/v1/auth/register", json={"email": email, "password": password})
    r = client.post("/api/v1/auth/login", json={"email": email, "password": password})
    return r.json()["access_token"]


def test_applications_are_user_scoped(client):
    token_a = register_and_login(client, "a@test.com", "Password123!")
    token_b = register_and_login(client, "b@test.com", "Password123!")

    headers_a = {"Authorization": f"Bearer {token_a}"}
    headers_b = {"Authorization": f"Bearer {token_b}"}

    # User A creates one application
    r = client.post("/api/v1/applications", headers=headers_a, json={
        "company": "Google",
        "role": "Backend Dev",
        "status": "applied"
    })
    assert r.status_code == 200
    app_id = r.json()["id"]

    # User A can see it
    r = client.get("/api/v1/applications", headers=headers_a)
    assert r.status_code == 200
    assert len(r.json()) == 1

    # User B sees none
    r = client.get("/api/v1/applications", headers=headers_b)
    assert r.status_code == 200
    assert len(r.json()) == 0

    # User B cannot fetch A's application by id
    r = client.get(f"/api/v1/applications/{app_id}", headers=headers_b)
    assert r.status_code == 404
