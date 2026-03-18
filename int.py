from flask import Flask, request, jsonify
import subprocess
import sqlite3

app = Flask(__name__)

ADMIN_TOKEN = "super_secret_admin_token"

# database setup
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
    token = request.headers.get("Authorization")
    if token != ADMIN_TOKEN:
        return jsonify({"error": "Unauthorized"}), 403

    user_id = request.json.get("id")

    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()

    return jsonify({"message": "User deleted"})


@app.route("/ping", methods=["GET"])
def ping_host():
    host = request.args.get("host")

    # Validate host to prevent command injection
    if not host or ".." in host or "/" in host:
        return jsonify({"error": "Invalid host"}), 400

    result = subprocess.getoutput(f"ping -c 1 {host}")

    return jsonify({"output": result})


if __name__ == "__main__":
    app.run(debug=False)
