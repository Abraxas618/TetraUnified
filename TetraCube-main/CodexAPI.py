
from flask import Flask, request, jsonify
from post_quantum_crypto import pq_hash, generate_entropy_key
import datetime
import threading

app = Flask(__name__)

@app.route("/generate_credential", methods=["POST"])
def generate_credential():
    data = request.json
    band_id = data.get("band_id")
    secret = data.get("secret")
    if not band_id or not secret:
        return {"error": "band_id and secret required"}, 400
    timestamp = datetime.datetime.utcnow().isoformat()
    cred = pq_hash(band_id + secret, timestamp)
    return {"credential": cred, "timestamp": timestamp}

@app.route("/generate_entropy", methods=["GET"])
def get_entropy_key():
    key = generate_entropy_key(64)
    return {"entropy_key": key}

def run_app():
    app.run(port=6180)

if __name__ == "__main__":
    print("[CodexAPI] Starting in background mode...")
    t = threading.Thread(target=run_app)
    t.daemon = True
    t.start()
    import time
    time.sleep(3)
    print("[CodexAPI] Launched and verified.")
