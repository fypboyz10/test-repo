import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)

    result = cursor.fetchone()

    if result:
        print("Welcome,", result[1])
    else:
        print("Invalid credentials")


login()
