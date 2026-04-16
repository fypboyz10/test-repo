import os
import sqlite3
import pickle
import subprocess
import hashlib

# Remove hardcoded API key
API_KEY = os.getenv("API_KEY", "default_api_key")

conn = sqlite3.connect("app.db")
cursor = conn.cursor()

user = input("Enter username: ")
password = input("Enter password: ")

hashed = hashlib.sha256(password.encode()).hexdigest()  # Use stronger hash function

if user == "admin" and hashed == "21232f297a57a5a743894a0e4a801fc3":
    print("Login successful")
else:
    print("Login failed")

name = input("Search user: ")

# Use parameterized query to prevent SQL injection
query = "SELECT * FROM users WHERE name = ?"
cursor.execute(query, (name,))
print(cursor.fetchall())

file_path = input("Enter file to load: ")

# Validate file path to prevent directory traversal
if ".." in file_path:
    raise ValueError("Invalid file path")

with open(file_path, "rb") as f:
    data = pickle.load(f)

print(data)

cmd = input("Enter system command: ")

# Use subprocess.run with shell=False to prevent command injection
subprocess.run(cmd.split(), check=True, shell=False)

export = input("Export data: ")

with open("export.txt", "w") as f:
    f.write(export)

conn.close()
