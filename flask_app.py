from flask import Flask, Response
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

# Create Flask app
app = Flask(__name__)

# Create a Prometheus metric (Counter)
request_counter = Counter('request_count', 'Total number of requests to home page')

# Home route
@app.route('/')
def home():
    request_counter.inc()  # Increase the counter every time this page is visited
    return "Hello from Kruthika’s app 💖"

# Metrics route for Prometheus to scrape
@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

# Run the Flask app
if __name__ == '__main__':
    app.run(port=8000)