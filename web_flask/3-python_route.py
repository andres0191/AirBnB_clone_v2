#!/usr/bin/python3
""" Write a script that starts a Flask web application """
from flask import Flask
import sys

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def print_hello_flask():
    """ print in display "Hello HBNB!" """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def print_hbnb():
    """ print in display "Hello HBNB!" """
    return "Hello HBNB!"


@app.route('/c/<text>', strict_slashes=False)
def print_c_is_fun(text):
    """ print in display "Hello HBNB!" """
    return "C %s" % text.replace('_', ' ')


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def print_python_is_cool(text='is_cool'):
    """ print in display "Hello HBNB!" """
    return "Python %s" % text.replace('_', ' ')


if __name__ == '__main__':
    """ Web app must be listening on 0.0.0.0 port 5000 """
    app.run(host='0.0.0.0', port=5000)
