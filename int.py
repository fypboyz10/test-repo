from flask import Flask, request, jsonify
import subprocess
import sqlite3
import os

app = Flask(__name__)

# Removed hardcoded admin token
ADMIN_TOKEN = os.getenv("ADMIN_TOKEN", "default_admin_token")

conn = sqlite3.connect("users.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT
)
""")
conn.commit()

@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.json

    username = data.get("username")

    cursor.execute("INSERT INTO users(username) VALUES (?)", (username,))
    conn.commit()

    return jsonify({"message": "User added"})

@app.route("/delete_user", methods=["POST"])
def delete_user():
    if token != ADMIN_TOKEN:
        return jsonify({"error": "Unauthorized"}), 403

    user_id = request.json.get("id")

    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()

    return jsonify({"message": "User deleted"})

@app.route("/ping", methods=["GET"])
def ping_host():
    host = request.args.get("host")

    if not host or len(host) > 255:
        return jsonify({"error": "Invalid host"}), 400

    result = subprocess.getoutput(f"ping -c 1 {host}")

    return jsonify({"output": result})

if __name__ == "__main__":
    app.run(debug=False)  # Production should run with debug=False
