#!/usr/bin/python3
""" Write a script that starts a Flask web application """
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
import sys


app = Flask(__name__)



app = Flask(__name__)


@app.route('/cities_list', strict_slashes=False)
def print_states_list():
    """ display a HTML page: (inside the tag BODY) """
    list_of_cities = storage.all('Citie')
    return render_template('8-cities_by_states.html', list_of_cities=list_of_cities)


if __name__ == '__main__':
    """ Web app must be listening on 0.0.0.0 port 5000 """
    app.run(host='0.0.0.0', port=5000)
