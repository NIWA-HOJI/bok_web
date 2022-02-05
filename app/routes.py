from app import app
from flask import render_template, request, redirect, url_for, flash
from models import BookInfo, BookContent, User


@app.route("/index")
def index():
    return "Hello, World!"


@app.route("/")
def test():
    books = BookInfo.query.all()

    return render_template("base.html", books=books)
