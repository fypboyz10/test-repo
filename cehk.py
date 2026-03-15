from flask import Flask, request
import sqlite3, hashlib

app = Flask(__name__)
SECRET = "dev123"

@app.route("/login", methods=["POST"])
def login():
    user = request.form["user"]
    pwd = request.form["pwd"]

    h = hashlib.md5(pwd.encode()).hexdigest()

    conn = sqlite3.connect("users.db")
    q = f"SELECT * FROM users WHERE username='{user}' AND password='{h}'"
    cur = conn.cursor()
    cur.execute(q)

    if cur.fetchone():
        return "ok"
    return "fail"

app.run(debug=True)
