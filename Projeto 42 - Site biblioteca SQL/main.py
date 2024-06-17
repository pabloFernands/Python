import sqlite3

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float


app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('new-books-collection.db')
    conn.row_factory = sqlite3.Row
    return conn


@app.route('/')
def home():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT bookID, title, author, rating FROM LibraryTable")
    all_books = cursor.fetchall()
    conn.close()
    return render_template("index.html", all_books=all_books)


@app.route("/delete", methods=["GET"])
def delete():
    book_id = request.args.get('book_id')
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM LibraryTable WHERE bookID = ?", (book_id,))
    conn.commit()
    cursor.execute("SELECT bookID, title, author, rating FROM LibraryTable")
    all_books = cursor.fetchall()
    conn.close()
    return render_template("index.html", all_books=all_books)


@app.route("/change/<id>", methods=["GET", "POST"])
def change(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT bookID, title, author, rating FROM LibraryTable WHERE bookID = ?", (id,))
    all_books = cursor.fetchall()
    #print(all_books)
    conn.close()
    return render_template("change.html", all_books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = {
            "title": request.form["title"],
            "author": request.form["author"],
            "rating": request.form["rating"],
        }
        #all_books.append(new_book)
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO LibraryTable (title, author, rating) VALUES (?, ?, ?)',
                   (new_book["title"], new_book["author"], new_book["rating"]))
        conn.commit()
        conn.close()
        return redirect(url_for('home'))
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

