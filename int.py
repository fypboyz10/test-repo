import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    result = cursor.fetchone()

    print("Welcome,", result[1])


login()
