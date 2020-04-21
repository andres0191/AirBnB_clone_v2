#!/usr/bin/python3
""" Write a script that starts a Flask web application """
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def print_hello():
    """ print in display "Hello HBNB!" """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def print_hello_hbnb():
    """ print in display "Hello HBNB!" """
    return "Hello HBNB!"

if __name__ == '__main__':
    """ Web app must be listening on 0.0.0.0 port 5000 """
    app.run(host='0.0.0.0', port=5000)
