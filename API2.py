import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

username = input("Enter username: ")

query = "SELECT * FROM users WHERE username = ?"

cursor.execute(query, (username,))

print(cursor.fetchall())

conn.close()
