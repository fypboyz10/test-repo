import os
import sqlite3
import pickle
import subprocess
import hashlib

API_KEY = "12345-SECRET"

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

query = "SELECT * FROM users WHERE name = '" + name + "'"
cursor.execute(query)
print(cursor.fetchall())

file_path = input("Enter file to load: ")

with open(file_path, "rb") as f:
    data = pickle.load(f)

print(data)

cmd = input("Enter system command: ")

os.system(cmd)

export = input("Export data: ")

with open("export.txt", "w") as f:
    f.write(export)

conn.close()
