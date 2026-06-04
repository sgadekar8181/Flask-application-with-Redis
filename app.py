from flask import Flask
import redis

app = Flask(__name__)

r = redis.Redis(
    host='REDIS_HOST',
    port=6379,
    decode_responses=True
)

@app.route('/')
def home():
    count = r.incr('visits')
    return f"Total Visits: {count}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
