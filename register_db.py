import sqlite3

conn = sqlite3.connect("data.db")


def create_table():
    with conn:
        conn.execute(
            """CREATE TABLE IF NOT EXISTS accounts('user name' TEXT,
             'first name' TEXT, 'last name' TEXT,'number' INTEGER,'Registered' TEXT);"""
        )


def add_user_to_db(username, first, last, number, time):
    with conn:
        conn.execute(
            "INSERT INTO accounts VALUES (?,?,?,?,?);", (username, first, last, number, time)
        )


def get_entries():
    cursor = conn.execute(
        "SELECT * FROM accounts"
    )
    return cursor.fetchall()


def del_user_from_db(username):
    with conn:
        conn.execute(
            f"DELETE FROM accounts WHERE \"user name\" = '{username}';"
        )
    with conn:
        conn.execute(
            f"DROP TABLE IF EXISTS books_{username};"
        )

