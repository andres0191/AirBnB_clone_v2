#!/usr/bin/python3
""" Write a script that starts a Flask web application """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
import sys


app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_and_state():
    """ display a HTML page: (inside the tag BODY) """
    list_states = storage.all('State')
    return render_template('9-states.html', list_states=list_states)
    

@app.route('/states/<int:id>', strict_slashes=False)
def states_id():
    """ display a HTML page: (inside the tag BODY) """
    dict_states = storage.all(State)
    list_states = []
    list_states_id = []
    return render_template('9-states.html', list_states=list_states,
                           list_states_id=list_states_id, id=id)


@app.teardown_appcontext
def close_storage(self):
    """ Declare a method to handle
        @app.teardown_appcontext
    """
    storage.close()


if __name__ == '__main__':
    """ Web app must be listening on 0.0.0.0 port 5000 """
    app.run(host='0.0.0.0', port=5000)
