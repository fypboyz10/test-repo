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

hashed = hashlib.sha256(password.encode()).hexdigest()  # Changed MD5 to SHA-256

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

# Secure deserialization using safe libraries like json instead of pickle
data = json.loads(open(file_path, "r").read())

print(data)

cmd = input("Enter system command: ")

# Avoid using os.system; use subprocess with proper argument handling
subprocess.run(cmd.split(), check=True)

export = input("Export data: ")

with open("export.txt", "w") as f:
    f.write(export)

conn.close()
