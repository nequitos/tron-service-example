
from fastapi.testclient import TestClient
from fastapi import status

from src.app import app


client = TestClient(app)


def test_read():
    payload = (('page', 1), ('per_page', 10))
    response = client.get("/request", params=payload)

    assert response.status_code == status.HTTP_200_OK


def test_create():
    data = {"address": "TTzPiwbBedv7E8p4FkyPyeqq4RVoqRL3TW"}
    response = client.post("/request", data=data)

    assert response.status_code == status.HTTP_200_OK