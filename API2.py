import sqlite3
import os

def connect_db():
    return sqlite3.connect("users.db")

def search_user():
    username = input("Enter username to search: ")

    conn = connect_db()
    cursor = conn.cursor()

    # Using parameterized queries to prevent SQL injection
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))

    results = cursor.fetchall()

    conn.close()

    for r in results:
        print(r)

def ping_server():
    host = input("Enter host to ping: ")

    # Using subprocess instead of os.system to avoid shell injection
    import subprocess
    subprocess.run(["ping", "-c", "3", host], check=True)

def main():
    print("1 Search User")
    print("2 Ping Server")

    choice = input("Choice: ")

    if choice == "1":
        search_user()

    elif choice == "2":
        ping_server()

main()
