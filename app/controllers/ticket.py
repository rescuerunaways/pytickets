from app import app
from flask import request as req
import requests


@app.route('/tickets/<int:id>')
def get(id):
    res = requests.get('https://ermolaeva.tania@gmail.com:12345@tatiana-ermolaeva.zendesk.com/api/v2/tickets/{0}.json'.format(id))
    return res.text


@app.route('/tickets')
def list():
    res = requests.get('https://ermolaeva.tania@gmail.com:12345@tatiana-ermolaeva.zendesk.com/api/v2/tickets.json', req.args)
    return res.text




