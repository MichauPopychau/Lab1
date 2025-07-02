from flask import Flask
import os
app = Flask(__name__)


@app.route('/')
def home():
    secret = os.environ.get("SECRET", "brak sekretu")
    return f'Hello world – Sekret: {secret}', 200


@app.route('/health')
def health():
    return 'OK', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
