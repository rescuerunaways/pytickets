from app import app


def is_ok(res):
    if not res.ok:
        if 'application/json' in res.headers.get('Content-Type'):
            raise Exception(res.reason, res.status_code, res.json())
        else:
            raise Exception(res.reason, res.status_code)


@app.errorhandler(404)
def not_found(error):
    return "Server error:{0}".format(Exception(error))


@app.errorhandler(Exception)
def server_error(error):
    return "Server error:{0}".format(error)
