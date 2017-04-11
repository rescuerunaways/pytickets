from flask import Flask

app = Flask(__name__)

from app import t


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, debug=True)
    app.config.from_pyfile('config.py')
