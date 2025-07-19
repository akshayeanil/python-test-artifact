from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Flask!"

def add(a, b):
    return a + b

if __name__ == "__main__":
    # Run the Flask app on all network interfaces on port 5000
    app.run(host="0.0.0.0", port=5000, debug=True)
