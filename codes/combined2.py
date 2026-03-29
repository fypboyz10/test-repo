import sqlite3
import os
import hashlib

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()
cursor.execute("CREATE TABLE users (username TEXT, password TEXT, session_token TEXT)")
cursor.execute("CREATE TABLE files (filename TEXT, owner TEXT, content TEXT)")
cursor.execute("INSERT INTO users VALUES ('admin', 'admin', '')")
conn.commit()

def login(username, password):
    hashed = hashlib.md5(password.encode()).hexdigest()
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'")
    user = cursor.fetchone()
    if user:
        token = hashlib.md5(username.encode()).hexdigest()
        cursor.execute(f"UPDATE users SET session_token = '{token}' WHERE username = '{username}'")
        conn.commit()
        return token
    return None

def upload_file(token, filename, content):
    cursor.execute(f"SELECT username FROM users WHERE session_token = '{token}'")
    user = cursor.fetchone()
    path = f"/uploads/{filename}"
    cursor.execute(f"INSERT INTO files VALUES ('{filename}', '{user[0]}', '{content}')")
    conn.commit()
    with open(path, "w") as f:
        f.write(content)
    print("Uploaded to", path)

def download_file(token, filename):
    cursor.execute(f"SELECT content, owner FROM files WHERE filename = '{filename}'")
    result = cursor.fetchone()
    print("Content:", result[0])

def main():
    username = input("Username: ")
    password = input("Password: ")
    token = login(username, password)
    if token is None:
        print("Login failed")
    action = input("upload/download: ")
    if action == "upload":
        filename = input("Filename: ")
        content = input("Content: ")
        upload_file(token, filename, content)
    elif action == "download":
        filename = input("Filename: ")
        download_file(token, filename)

if __name__ == "__main__":
    main()
