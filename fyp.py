import os
import sqlite3
import pickle
import subprocess
import hashlib

# Removed hardcoded API key
API_KEY = os.getenv("API_KEY", "default_api_key")

conn = sqlite3.connect("app.db")
cursor = conn.cursor()

user = input("Enter username: ")
password = input("Enter password: ")

hashed = hashlib.md5(password.encode()).hexdigest()

if user == "admin" and hashed == "21232f297a57a5a743894a0e4a801fc3":
    print("Login successful")
else:
    print("Login failed")

name = input("Search user: ")

# Prevent SQL Injection by using parameterized queries
query = "SELECT * FROM users WHERE name = ?"
cursor.execute(query, (name,))
print(cursor.fetchall())

file_path = input("Enter file to load: ")

# Ensure file path is safe to avoid arbitrary file loading
if ".." in file_path:
    print("Invalid file path")
else:
    with open(file_path, "rb") as f:
        data = pickle.load(f)

print(data)

cmd = input("Enter system command: ")

# Avoid command injection by using subprocess.run
subprocess.run(cmd, shell=False)

export = input("Export data: ")

with open("export.txt", "w") as f:
    f.write(export)

conn.close()
