from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello from Flask!'

if __name__ == '__main__':
    # Run Flask on all interfaces, no debug, no reloader
    app.run(host='0.0.0.0', port=5000, debug=False, use_reloader=False)
