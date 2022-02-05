from app import app
from flask import render_template, request, redirect, url_for, flash
from app.models import BookInfo, BookContent, User


@app.route("/index")
def index():
    return "Hello, World!"


@app.route("/")
@app.route("/page/<int:page>")
def test(page=1):
    books = BookInfo.query.offset(10 * (page - 1)).limit(10).all()
    print(books)
    total_book_page = BookInfo.query.count() // 10 + 1
    return render_template(
        "base.html", total_book_page=total_book_page, page=page, books=books
    )


@app.route("/book/<int:book_id>")
def book_info(book_id):
    book = BookInfo.query.get(book_id)
    pages = [x for x in range(1, book.page_count + 1)]
    return render_template("book_info.html", pages=pages, book=book)
