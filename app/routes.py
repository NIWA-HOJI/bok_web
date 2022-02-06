from app import app
from flask import render_template, request, redirect, url_for, flash
from app.models import BookInfo, BookContent, User
from flask_login import current_user, login_user


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

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    # # form = LoginForm()
    # if form.validate_on_submit():
    #     user = User.query.filter_by(username=form.username.data).first()
    #     if user is None or not user.check_password(form.password.data):
    #         flash('Invalid username or password')
    #         return redirect(url_for('login'))
    #     login_user(user, remember=form.remember_me.data)
    #     return redirect(url_for('index'))
    # return render_template('login.html', title='Sign In', form=form)
@app.route('/search')
def search():
    keyword=request.args.get('keyword')
    books=BookInfo.query.filter(BookInfo.title.like('%'+keyword+'%')).all()
    return render_template('search.html',books=books)