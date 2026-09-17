def test_signup_and_login_happy_path(client):
    signup_res = client.post("/signup", json={"email": "alice@example.com", "password": "hunter2"})
    assert signup_res.status_code == 201
    assert signup_res.json()["email"] == "alice@example.com"

    login_res = client.post("/login", json={"email": "alice@example.com", "password": "hunter2"})
    assert login_res.status_code == 200
    body = login_res.json()
    assert body["token_type"] == "bearer"
    assert len(body["access_token"]) > 0


def test_login_with_wrong_password_fails(client):
    client.post("/signup", json={"email": "bob@example.com", "password": "correct-horse"})

    login_res = client.post(
        "/login", json={"email": "bob@example.com", "password": "wrong-password"}
    )
    assert login_res.status_code == 401


def test_decode_access_token_round_trip():
    from app.auth import create_access_token, decode_access_token

    token = create_access_token(subject="carol@example.com")
    assert decode_access_token(token) == "carol@example.com"
    assert decode_access_token("not-a-real-token") is None
