#!/usr/bin/python3
""" Write a script that starts a Flask web application """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
import sys

app = Flask(__name__)


@app.teardown_appcontext()
def list_of_states():
    """ Declare a method to handle
        @app.teardown_appcontext
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def print_states_list():
    """ display a HTML page: (inside the tag BODY) """
    states_list = []
    for key, value in states_list.items():
        states_list.append(value)
    return render_template('7-states_list.html', states_list=states_list)


if __name__ == '__main__':
    """ Web app must be listening on 0.0.0.0 port 5000 """
    app.run(host='0.0.0.0', port=5000)
