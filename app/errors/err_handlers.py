from app import app


@app.errorhandler(401)
def not_found(error):
    app.logger.error('Server Error: %s', (error))
    return "Could not authenticate user"


@app.errorhandler(404)
def not_found(error):
    app.logger.error('Server Error: %s', (error))
    return "File not found"


@app.errorhandler(Exception)
def server_error(error):
    app.logger.error('Server Error: %s', (error))
    return "Internal server error"
