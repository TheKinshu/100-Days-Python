from flask import Flask, render_template, request, redirect, url_for
from flask.globals import session
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app) 

# cursor = db.cursor()

# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', 9.3)")
# db.commit()

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), unique=True, nullable=False)
    author = db.Column(db.String(30), nullable=False)
    review = db.Column(db.Float, nullable=False)

    def __repr__(self) -> str:
        return '<Book {self.title}>'


# # Read a particular record from the query
# book = Book.query.filter_by(title="Harry Potter").first()
# # Update a Particular record from the query
# book_to_update = Book.query.filter_by(title="Harry Potter").first()
# book_to_update.title = "Harry Potter and the Chamber of Secrets"
# db.session.commit()
# # Update by using key/id
# book_id = 1
# book_to_update = Book.query.get(book_id)
# book_to_update = "Harry Potter and the Goblet of Fire"
# db.session.commit()
# # Delete a particular record using key/id
# book_id = 1
# book_to_delete = Book.query.get(book_id)
# db.session.delete(book_to_delete)
# db.session.commit()


@app.route('/')
def home():
    # Read All Records
    all_books = db.session.query(Book).all()
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        book = {
                    "title": request.form['title'],
                    "author":request.form['author'],
                    "rating": request.form['rating']
                }
        new_book = Book(title=book["title"], author=book["author"], review=book["rating"])
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))


    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

