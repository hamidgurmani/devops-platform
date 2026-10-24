from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "application": "devops-platform",
        "message": "Application is running!",
        "hostname": socket.gethostname(),
        "environment": os.getenv("APP_ENV", "development")
    })


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
