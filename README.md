# pytickets

install dependencies: 
pip install -r requirements.txt

run tests:
python -m unittest discover app.tests

run a server:
export FLASK_APP=app/__init__.py; flask run
