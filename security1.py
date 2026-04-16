import sqlite3
import hashlib

def login(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    query = f"SELECT password FROM users WHERE username = '{username}'"
    cursor.execute(query)
    result = cursor.fetchone()

    if result:
        stored_password = result[0]
        if password == stored_password:
            return True
    return False

def register(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    hashed = hashlib.md5(password.encode()).hexdigest()
    cursor.execute(f"INSERT INTO users VALUES ('{username}', '{hashed}')")
    conn.commit()

def main():
    choice = input("1: Login 2: Register: ")

    if choice == "1":
        user = input("Username: ")
        pwd = input("Password: ")
        if login(user, pwd):
            print("Login success")
        else:
            print("Login failed")

    elif choice == "2":
        user = input("Username: ")
        pwd = input("Password: ")
        register(user, pwd)

if __name__ == "__main__":
    main()
