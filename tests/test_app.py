import pytest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app, workouts  

@pytest.fixture(autouse=True)
def clear_workouts():
    workouts.clear()
    yield
    workouts.clear()

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    r = client.get("/")
    assert r.status_code == 200
    assert b"ACEest Fitness and Gym" in r.data

def test_get_workouts_empty(client):
    r = client.get("/api/workouts")
    assert r.status_code == 200
    assert r.get_json() == []

def test_add_workout_success(client):
    r = client.post("/api/workouts", json={"workout": "Running", "duration": 30})
    assert r.status_code == 201
    assert r.get_json() == {"workout": "Running", "duration": 30}

    r2 = client.get("/api/workouts")
    assert r2.status_code == 200
    assert r2.get_json() == [{"workout": "Running", "duration": 30}]

def test_add_workout_validation(client):
    r = client.post("/api/workouts", json={})
    assert r.status_code == 400

    r = client.post("/api/workouts", json={"workout": "Yoga", "duration": "thirty"})
    assert r.status_code == 400
