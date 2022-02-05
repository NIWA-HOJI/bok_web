from app import app
from flask import render_template, request, redirect, url_for, flash


@app.route("/index")
def index():
    return "Hello, World!"


@app.route("/", methods=["GET", "POST"])
def test():
    return render_template("base.html")
