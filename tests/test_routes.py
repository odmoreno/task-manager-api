import os
import pytest
from app import create_app

from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("API_KEY")


@pytest.fixture
def client():
    os.environ["API_KEY"] = API_KEY
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()

def test_get_tasks(client):
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_post_task_auth_success(client):
    response = client.post(
        "/tasks",
        headers={"Authorization":  f"Bearer {API_KEY}"},
        json={"title": "Test tarea", "description": "Test de tarea de prueba"}
    )
    assert response.status_code == 201
    data = response.get_json()
    assert data["title"] == "Test tarea"
    assert "_id" in data

def test_post_task_auth_fail(client):
    response = client.post(
        "/tasks",
        json={"title": "Tarea sin auth"}
    )
    assert response.status_code == 401

def test_put_invalid_status(client):
    post = client.post(
        "/tasks",
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={"title": "Tarea editada", "description": "En proceso"}
    )
    task_id = post.get_json()["_id"]

    put = client.put(
        f"/tasks/{task_id}",
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={"status": "no es valido"}
    )
    assert put.status_code == 422
