import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

username = input("Username: ")
password = input("Password: ")

query = "SELECT * FROM users WHERE username = ? AND password = ?"
cursor.execute(query, (username, password))

result = cursor.fetchone()

if result:
    print("Login successful")
else:
    print("Invalid credentials")
