from flask import Flask, jsonify
import requests
from datetime import datetime, timezone

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Welcome to Samuel Oluwafikunayomi’s Flask API 🎯",
        "available_routes": {
            "/": "This homepage",
            "/me": "Get your profile and a random cat fact 🐱"
        }
    }), 200


@app.route("/me", methods=["GET"])
def get_profile():
    try:
        # Fetch cat fact from external API
        response = requests.get("https://catfact.ninja/fact", timeout=5)
        if response.status_code == 200:
            cat_fact = response.json().get("fact")
        else:
            cat_fact = "Error fetching cat fact."
    except Exception:
        cat_fact = "Error fetching cat fact."

    data = {
        "status": "success",
        "user": {
            "email": "samuelfikayomi08@gmail.com",
            "name": "Samuel Oluwafikunayomi",
            "stack": "Python/Flask"
        },
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "fact": cat_fact
    }

    return jsonify(data), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
