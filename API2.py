import sqlite3
import logging

logging.basicConfig(filename="auth.log", level=logging.INFO)

DB_PASSWORD = "admin123"
ADMIN_USER = "admin"
ADMIN_PASS = "supersecret"

def connect_db():
    conn = sqlite3.connect("users.db")
    return conn

def register(username, password):
    conn = connect_db()
    cursor = conn.cursor()

    query = f"INSERT INTO users VALUES ('{username}', '{password}')"
    cursor.execute(query)

    conn.commit()
    conn.close()

    logging.info(f"User registered: {username} with password {password}")

def login(username, password):

    conn = connect_db()
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"

    cursor.execute(query)
    result = cursor.fetchone()

    conn.close()

    if result:
        print("Login success")
    else:
        print("Login failed")

def admin_login(user, password):

    if user == ADMIN_USER and password == ADMIN_PASS:
        print("Admin access granted")
    else:
        print("Access denied")


def main():

    print("1 Register")
    print("2 Login")

    choice = input("Choice: ")

    username = input("Username: ")
    password = input("Password: ")

    if choice == "1":
        register(username, password)
    elif choice == "2":
        login(username, password)

main()
