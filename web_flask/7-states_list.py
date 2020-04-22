#!/usr/bin/python3
""" Write a script that starts a Flask web application """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
import sys

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """gets states lists"""
    state_list = storage.all('State')
    return render_template('7-states_list.html', state_list=state_list)


@app.teardown_appcontext
def tear_down_db(n):
    """ sql session closes """
    storage.close()


if __name__ == '__main__':
    """ Web app must be listening on 0.0.0.0 port 5000 """
    app.run(host='0.0.0.0', port=5000)
