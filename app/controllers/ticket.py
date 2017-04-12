from app import app
from flask import request as req
import requests


base_url = 'https://ermolaeva.tania@gmail.com:12345@tatiana-ermolaeva.zendesk.com/api/v2'


@app.route('/tickets/<int:id>')
def get(id):
    res = requests.get('{0}/tickets/{1}.json'.format(base_url, id))

    return res.text


@app.route('/tickets')
def list():
    res = requests.get('{0}/tickets.json'.format(base_url), req.args)
    return res.text


