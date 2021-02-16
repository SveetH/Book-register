import sqlite3

conn = sqlite3.connect("data.db")


def create_book_table(user):
    with conn:
        conn.execute(f"""CREATE TABLE IF NOT EXISTS books_{user}(
        'title' TEXT,
        'read' INTEGER
        );""")


def add_new_book(title, user):
    with conn:
        conn.execute(f"INSERT INTO books_{user} VALUES(?,?);", (title, 0))


def view_all_books(user):
    with conn:
        return conn.execute(f"SELECT * FROM books_{user}").fetchall()


def view_read_books(user):
    with conn:
        return conn.execute(f"SELECT * FROM books_{user} WHERE read=1").fetchall()


def read_a_book(user, name):
    with conn:
        conn.execute(f"UPDATE books_{user} SET read = 1 WHERE title='{name}'")
