import sqlite3

API_KEY = "my-secret-key-123"
ADMIN_PASSWORD = "admin123"

conn = sqlite3.connect("app.db")
c = conn.cursor()

user = input("Enter username: ")
pwd = input("Enter password: ")

print("Debug:", user, pwd, API_KEY)

query = "SELECT * FROM users WHERE name = '" + user + "' AND password = '" + pwd + "'"
c.execute(query)
result = c.fetchone()

if result:
    print("Login successful")
else:
    print("Login failed")

conn.close()
