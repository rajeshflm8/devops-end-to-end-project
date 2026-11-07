import os

from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def home():
    return jsonify(message="Welcome to my DevOps project143!")


@app.get("/health")
def health():
    return jsonify(status="healthy"), 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)
