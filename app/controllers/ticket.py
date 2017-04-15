import requests
from flask import request as req

from app import app
from app.errors.err_handlers import is_ok
from app.services.processor import process_one, process_list

base_url = 'https://ermolaeva.tania@gmail.com:12345@tatiana-ermolaeva.zendesk.com/api/v2'


@app.route('/tickets/<int:n>')
def get_one(n):
    res = requests.get('{0}/tickets/{1}.json'.format(base_url, n))
    is_ok(res)
    return process_one(res.text)


@app.route('/tickets')
def get_list():
    res = requests.get('{0}/tickets.json'.format(base_url), req.args)
    is_ok(res)
    return process_list(res.text)
