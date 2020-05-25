#!/usr/bin/python3
"""First Task"""
from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close(error):
    storage.close()


@app.route("/states", strict_slashes=False)
def task9():
    return render_template(
            "9-states.html",
            state=storage.all(State),
            t="v")


@app.route("/states/<id>", strict_slashes=False)
def task9o(id):
    objr = None
    obj = storage.all(State)
    for k, v in obj.items():
        if v.id == id:
            objr = v
    if objr is None:
        return render_template(
                "9-states.html",
                t="n",
                msg="Not found!")
    return render_template(
            "/9-states.html",
            state=objr,
            t="u")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
