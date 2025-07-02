from flask import Flask
import os
app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello world', 200
    print("Sekret:", os.environ.get("SECRET", "brak sekretu"))


@app.route('/health')
def health():
    return 'OK', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
