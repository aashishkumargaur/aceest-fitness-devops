import json
import pytest
from app import create_app

@pytest.fixture()
def client():
    app = create_app()
    app.config.update({"TESTING": True})
    return app.test_client()

def test_health(client):
    res = client.get("/")
    assert res.status_code == 200
    data = res.get_json()
    assert data["status"] == "ok"

def test_list_classes(client):
    res = client.get("/classes")
    assert res.status_code == 200
    data = res.get_json()
    assert isinstance(data["classes"], list)
    assert len(data["classes"]) >= 1

def test_add_and_get_member(client):
    payload = {"member_id": "101", "name": "Ashish"}
    res = client.post("/members", data=json.dumps(payload), content_type="application/json")
    assert res.status_code == 201

    res2 = client.get("/members/101")
    assert res2.status_code == 200
    member = res2.get_json()
    assert member["name"] == "Ashish"

def test_add_member_validation(client):
    res = client.post("/members", json={"name": "NoId"})
    assert res.status_code == 400
