from app import db,app


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return "<User {}>".format(self.username)


class BookInfo(db.Model):
    __tablename__ = "book_info"
    book_id = db.Column(db.String(64), primary_key=True)
    book_name = db.Column(db.String(64))
    description = db.Column(db.Text)
    page_count = db.Column(db.Integer)


class BookContent(db.Model):
    __tablename__ = "book_content"
    book_id = db.Column(db.String(64), primary_key=True)
    content = db.Column(db.Text)
    page_number = db.Column(db.Integer)
