import os
import redis
from flask import Flask

app = Flask(__name__)

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    decode_responses=True
)

@app.route("/")
def home():
    count = redis_client.incr("visits")
    return f"Visits: {count}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
