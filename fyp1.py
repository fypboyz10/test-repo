import os
import sqlite3
import pickle
import subprocess
import hashlib
from getpass import getpass

# Removed hardcoded API key
API_KEY = None  # This should be set via environment variable or configuration file

conn = sqlite3.connect("app.db")
cursor = conn.cursor()

user = input("Enter username: ")
password = getpass("Enter password: ")  # Changed to use getpass for better security

hashed = hashlib.md5(password.encode()).hexdigest()

if user == "admin" and hashed == "21232f297a57a5a743894a0e4a801fc3":
    print("Login successful")
else:
    print("Login failed")

name = input("Search user: ")

# Parameterized query to prevent SQL injection
query = "SELECT * FROM users WHERE name = ?"
cursor.execute(query, (name,))
print(cursor.fetchall())

file_path = input("Enter file to load: ")

with open(file_path, "rb") as f:
    data = pickle.load(f)

print(data)

cmd = input("Enter system command: ")

# Using subprocess.run with shell=False to prevent command injection
subprocess.run(cmd.split(), check=True, shell=False)

export = input("Export data: ")

with open("export.txt", "w") as f:
    f.write(export)

conn.close()
