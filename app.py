from flask import Flask, jsonify, request, render_template
import os

app = Flask(__name__)

workouts = []

@app.get("/")
def home():
    return render_template("home.html")


@app.get("/api/workouts")
def get_workouts():
    return jsonify(workouts), 200

@app.post("/api/workouts")
def add_workout():
    data = request.get_json(silent=True) or {}
    workout = data.get("workout")
    duration = data.get("duration")

    if not workout or not isinstance(workout, str):
        return jsonify({"error": "'workout' is required and must be a string"}), 400

    try:
        duration = int(duration)
    except (TypeError, ValueError):
        return jsonify({"error": "'duration' is required and must be an integer (minutes)"}), 400

    entry = {"workout": workout.strip(), "duration": duration}
    workouts.append(entry)
    return jsonify(entry), 201

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
