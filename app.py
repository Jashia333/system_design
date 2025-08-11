from flask import Flask, request, jsonify
import time

app = Flask(__name__)
CACHE = {}  # { key: (value, expires_at or None) }

@app.put("/cache")
def put_value():
    data = request.get_json(force=True)
    key = data.get("key")
    value = data.get("value")
    ttl_seconds = data.get("ttl")  # Optional TTL in seconds

    if key is None:
        return jsonify(error="key is required"), 400

    expires_at = time.time() + ttl_seconds if ttl_seconds else None
    CACHE[key] = (value, expires_at)
    return jsonify(key=key, stored=True, ttl=ttl_seconds or "none")

@app.get("/cache/<key>")
def get_value(key):
    if key not in CACHE:
        return jsonify(error="key not found"), 404

    value, expires_at = CACHE[key]
    if expires_at and time.time() > expires_at:
        del CACHE[key]
        return jsonify(error="key expired"), 404

    ttl_remaining = round(expires_at - time.time(), 2) if expires_at else None
    return jsonify(key=key, value=value, ttl_remaining=ttl_remaining)

@app.get("/cache/_size")
def size():
    cleanup_expired()
    return jsonify(size=len(CACHE))

@app.get("/cache/_show")
def show():
    cleanup_expired()
    now = time.time()
    # Include TTL for each key
    result = {
        k: {
            "value": v,
            "ttl_remaining": round(exp - now, 2) if exp else None
        }
        for k, (v, exp) in CACHE.items()
    }
    return jsonify(cache_list=result)

def cleanup_expired():
    now = time.time()
    expired_keys = [k for k, (_, exp) in CACHE.items() if exp and now > exp]
    for k in expired_keys:
        del CACHE[k]

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
