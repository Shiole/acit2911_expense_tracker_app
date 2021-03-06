from app import *
import pytest
import sqlite3
import modules.user_module as user_module


@pytest.fixture
def client():
    # Creates the test environment
    client = app.test_client()

    with client.session_transaction(subdomain="blue") as session:
        # assume that a user is signed in to user 1
        session["uid"] = "1"

    return client


def test_data_to_dict():
    assert data_to_dict(("1", "1", "Coffee", "2022-04-29", "Food", 4.5)) == {
        "amount": 4.5,
        "category": "Food",
        "date": "2022-04-29",
        "eid": "1",
        "name": "Coffee",
    }


def test_signup(client):
    assert (
        client.post(
            "/signup",
            data={
                "name": "test test",
                "username": "tester123",
                "email": "test@gmail.com",
                "password": "Password123!",
            },
        ).status_code
        == 200
    )
    client.get("signup") == 200


def test_login(client):
    assert (
        client.post(
            "/", data={"username": "testdummy", "password": "Testing123@"}
        ).status_code
        == 200
    )


def test_homepage(client):
    assert client.get("/home").status_code == 200


def test_add_page(client):
    assert client.get("/add").status_code == 200
    assert (
        client.post(
            "/add",
            data={
                "name": "Hot Dog",
                "category": "Food",
                "amount": "1.50",
                "date": "2022-01-01",
            },
        ).status_code
        == 301
    )
    assert client.post("/add", data={"1": "2"}).status_code == 400


def test_get_expense(client):
    assert client.get("/edit/1").status_code == 200
    assert (
        client.post(
            "/edit/1",
            data={
                "name": "Hot Dog",
                "category": "Food",
                "amount": "1.50",
                "date": "2022-01-01",
            },
        ).status_code
        == 301
    )


def test_profile(client):
    assert client.get("/profile").status_code == 200
    # assert client.post("/profile").status_code == 301


def test_profile_edit(client):
    assert (
        client.post(
            "/profile/edit",
            data={
                "name": "myname name",
                "username": "myname123",
                "email": "balls@gmail.com",
            },
        ).status_code
        == 301
    )


def test_reset_password(client):
    assert (
        client.post(
            "/profile/resetpassword",
            data={"old_password": "Oldpass123!", "new_password": "Newpass123!"},
        ).status_code
        == 200
    )
