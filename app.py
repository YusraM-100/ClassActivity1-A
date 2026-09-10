from pathlib import Path

from flask import Flask, jsonify, request


app = Flask(__name__)
MODEL_VERSION = "1.0"
VERSION_FILE = Path(__file__).with_name("VERSION")


def get_application_version():
	version = VERSION_FILE.read_text(encoding="utf-8").strip()
	return version if version and not version.startswith("#") else "0.0.0"


@app.get("/")
def service_info():
	return jsonify({
		"service": "mlops-cd-demo",
		"application_version": get_application_version(),
		"model_version": MODEL_VERSION,
	})


@app.get("/health")
def health():
	return jsonify({
		"status": "healthy",
		"application_version": get_application_version(),
		"model_version": MODEL_VERSION,
	})


@app.post("/predict")
def predict():
	payload = request.get_json(silent=True) or {}
	value = payload.get("value")

	if not isinstance(value, (int, float)) or isinstance(value, bool):
		return jsonify({"error": "value must be a number"}), 400

	return jsonify({"prediction": value * 2})


if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5000)
