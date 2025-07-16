from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello from Flask!'

def add(a, b):
    return a + b

if __name__ == '__main__':
    app.run(debug=True)
