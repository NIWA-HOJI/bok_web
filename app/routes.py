from app import app
from flask import render_template, request, redirect, url_for, flash
from app.models import BookInfo, BookContent, User


@app.route("/index")
def index():
    return "Hello, World!"


@app.route("/")
@app.route("/page/<int:page>/")
def test(page=1):
    books = BookInfo.query.offset(10 * (page - 1)).limit(10).all()
    total_book_page = BookInfo.query.count() // 10 + 1
    return render_template(
        "base.html", total_book_page=total_book_page, page=page, books=books
    )


@app.route("/book/<int:book_id>/")
def book_info(book_id):
    book = BookInfo.query.get(book_id)
    pages = [x for x in range(1, book.page_count + 1)]
    return render_template("book_info.html", pages=pages, book=book)


@app.route("/book/<int:book_id>/page/<int:page>/")
def page(book_id, page):
    content = BookContent.query.filter_by(book_id=book_id, page_number=page).first()
    book_info = BookInfo.query.get(book_id)
    page_count = book_info.page_count
    return render_template("page.html", page_count=page_count, content=content)
