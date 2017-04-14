from flask import Flask

app = Flask(__name__)
from app.controllers import ticket
from app.errors import err_handlers
