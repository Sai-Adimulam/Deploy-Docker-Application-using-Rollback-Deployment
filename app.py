from flask import Flask
import os
import socket

app = Flask(__name__)

VERSION = os.getenv("APP_VERSION", "v1")
HOSTNAME = socket.gethostname()

@app.route("/")
def home():
    return {
        "message": "Hello from Docker!",
        "version": VERSION,
        "hostname": HOSTNAME
    }

@app.route("/health")
def health():
    return {"status": "healthy"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
