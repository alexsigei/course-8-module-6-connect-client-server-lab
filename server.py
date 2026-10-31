
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Sample events
events = [
    {"id": 1, "title": "Yoga in the park"},
    {"id": 2, "title": "Lake 5k run"}
]


# Welcome route
@app.route("/", methods=["GET"])
def welcome():
    return jsonify({"message": "Welcome!"}), 200


# Get all events
@app.route("/events", methods=["GET"])
def get_events():
    return jsonify(events), 200


# Create a new event
@app.route("/events", methods=["POST"])
def add_event():
    data = request.get_json(silent=True)

    # Validate the request data
    if not data or not isinstance(data, dict) or not data.get("title"):
        return jsonify({"error": "Title is required"}), 400

    # Generate a unique ID
    new_id = max([event["id"] for event in events]) + 1 if events else 1

    # Create the new event
    new_event = {
        "id": new_id,
        "title": data["title"]
    }

    # Add the event to the list
    events.append(new_event)

    # Return the new event
    return jsonify(new_event), 201


if __name__ == "__main__":
    app.run(debug=True)
