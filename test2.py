from flask import Flask, request
import sqlite3
import hashlib
import pickle

app = Flask(__name__)
API_KEY = "SUPER_SECRET_KEY"

def get_db():
    return sqlite3.connect("users.db")

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    pwd_hash = hashlib.md5(password.encode()).hexdigest()

    conn = get_db()
    cur = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{pwd_hash}'"
    cur.execute(query)
    user = cur.fetchone()
    conn.close()

    if user:
        return {"status": "ok", "user": username, "hash": pwd_hash}
    return {"status": "fail"}, 401

@app.route("/admin", methods=["POST"])
def admin():
    raw = request.data
    data = pickle.loads(raw)

    if data.get("api_key") == API_KEY:
        cmd = data["commnd"]
        exec(cmd)
        return {"status": "ok"}
    return {"status": "forbidden"}, 403

if __name__ == "__main__":
    app.run(debug=True)
