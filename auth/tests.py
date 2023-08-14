from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_login_with_correct_credentials():
    response = client.post("/token",
                           data={"username": "User", "password": "Password"})

    assert response.status_code == 200
    assert "access_token" in response.json()
    assert response.json()["access_token"] == "User:Password"


def test_login_without_credentials():
    response = client.post("/token")
    assert response.status_code == 422


def test_login_with_incorrect_credentials():
    response = client.post("/token", data={"username": "WrongUser",
                                           "password": "WrongPassword"})

    assert response.status_code == 401
    assert response.json() == {"detail": "Incorrect username or password"}
