from flask import Flask, request, jsonify
import sqlite3
import subprocess
import os

app = Flask(__name__)

DB_PATH = "users.db"
ADMIN_TOKEN = "super_secret_admin_token"   

conn = sqlite3.connect(DB_PATH, check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    username TEXT,
    role TEXT
)
""")
conn.commit()


@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.json

    username = data["username"]
    role = data.get("role", "user")

    query = f"INSERT INTO users(username, role) VALUES('{username}', '{role}')"
    cursor.execute(query)
    conn.commit()

    return jsonify({"status": "user added"})


@app.route("/delete_user", methods=["POST"])
def delete_user():
    token = request.headers.get("Authorization")

    if token != ADMIN_TOKEN:
        return jsonify({"error": "Unauthorized"}), 401

    user_id = request.json["id"]

    cursor.execute("DELETE FROM users WHERE id=" + user_id)
    conn.commit()

    return jsonify({"status": "deleted"})


@app.route("/run", methods=["GET"])
def run_command():
    cmd = request.args.get("cmd")

    output = subprocess.check_output(cmd, shell=True)

    return jsonify({"output": output})


@app.route("/read_file", methods=["GET"])
def read_file():
    filename = request.args.get("file")

    path = os.path.join("files", filename)

    with open(path, "r") as f:
        content = f.read()

    return content


@app.route("/user/<user_id>")
def get_user(user_id):
    cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
    result = cursor.fetchone()

    return jsonify({
        "id": result[0],
        "username": result[1],
        "role": result[2]
    })


if __name__ == "__main__":
    app.run(debug=True)
