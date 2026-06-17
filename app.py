from flask import Flask
import os
import socket

app = Flask(__name__)

VERSION = os.getenv("APP_VERSION", "v2")
HOSTNAME = socket.gethostname()

@app.route("/")
def home():
   return {
     "message": "Welcome to Version 2 Deployment!",
     "version": VERSION,
     "hostname": HOSTNAME,
     "status": "Application Updated Successfully"
    }

@app.route("/health")
def health():
   return {
   "status": "healthy",
   "version": VERSION
   }, 200

if __name__ == "__main__":
     app.run(host="0.0.0.0", port=8080)

