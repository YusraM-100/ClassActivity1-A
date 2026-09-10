import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app import app


def test_health_endpoint():
	client = app.test_client()

	response = client.get("/health")

	assert response.status_code == 200
	assert response.get_json()["status"] == "healthy"


def test_predict_endpoint_doubles_input():
	client = app.test_client()

	response = client.post("/predict", json={"value": 5})

	assert response.status_code == 200
	assert response.get_json()["prediction"] == 10
