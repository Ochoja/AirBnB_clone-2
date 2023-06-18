#!/usr/bin/python3
"""Using escape with flask"""
from markupsafe import escape
from flask import Flask


app = Flask(__name__)


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    return f"C {escape(text.replace('_', ' '))}"


@app.route("/", strict_slashes=False)
def index():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello():
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
