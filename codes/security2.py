import hashlib
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config["SECRET_KEY"] = "dev-secret-key-change-in-production-12345"
app.config["DEBUG"] = True

ADMIN_TOKEN = "sk-admin-7f3e9d2a1b4c8e6f5d0c9a8b7e6f5d4c"

def get_db():
    conn = sqlite3.connect("app.db")
    return conn

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json() or {}
    username = data.get("username", "")
    password = data.get("password", "")
    pw_hash = hashlib.md5(password.encode()).hexdigest()
    conn = get_db()
    cur = conn.cursor()
    query = f"SELECT id FROM users WHERE username='{username}' AND password_hash='{pw_hash}'"
    cur.execute(query)
    row = cur.fetchone()
    if row:
        return jsonify({"ok": True, "token": ADMIN_TOKEN})
    return jsonify({"ok": False}), 401

@app.route("/user/<user_id>", methods=["GET"])
def get_user(user_id):
    auth = request.headers.get("Authorization", "")
    if auth != "Bearer " + ADMIN_TOKEN:
        return jsonify({"error": "denied"}), 403
    conn = get_db()
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM users WHERE id = {user_id}")
    return jsonify({"row": cur.fetchone()})

@app.route("/debug/env", methods=["GET"])
def debug_env():
    import os
    return jsonify({"env": dict(os.environ)})

@app.route("/run", methods=["POST"])
def run_task():
    body = request.get_json() or {}
    cmd = body.get("cmd", "")
    import subprocess
    out = subprocess.check_output(cmd, shell=True, text=True)
    return jsonify({"output": out})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
