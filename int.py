from flask import Flask, request, jsonify
import sqlite3
import subprocess
import os
import shlex

app = Flask(__name__)

DB_PATH = "users.db"

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

    query = "INSERT INTO users(username, role) VALUES(?, ?)"
    cursor.execute(query, (username, role))
    conn.commit()

    return jsonify({"status": "user added"})


@app.route("/delete_user", methods=["POST"])
def delete_user():
    token = request.headers.get("Authorization")

    if token != os.environ.get("ADMIN_TOKEN"):
        return jsonify({"error": "Unauthorized"}), 401

    user_id = request.json["id"]

    query = "DELETE FROM users WHERE id=?"
    cursor.execute(query, (user_id,))
    conn.commit()

    return jsonify({"status": "deleted"})


@app.route("/run", methods=["GET"])
def run_command():
    cmd = request.args.get("cmd")

    if not cmd:
        return jsonify({"error": "Command required"}), 400

    try:
        args = shlex.split(cmd)
        output = subprocess.check_output(args, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        return jsonify({"error": e.output.decode()}), 500

    return jsonify({"output": output.decode()})


@app.route("/read_file", methods=["GET"])
def read_file():
    filename = request.args.get("file")

    if not filename:
        return jsonify({"error": "Filename required"}), 400

    allowed_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-. "
    if not all(c in allowed_chars for c in filename):
        return jsonify({"error": "Invalid filename"}), 400

    path = os.path.join("files", os.path.basename(filename))

    try:
        with open(path, "r") as f:
            content = f.read()
    except FileNotFoundError:
        return jsonify({"error": "File not found"}), 404

    return content


@app.route("/user/<int:user_id>")
def get_user(user_id):
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    result = cursor.fetchone()

    if result is None:
        return jsonify({"error": "User not found"}), 404

    return jsonify({
        "id": result[0],
        "username": result[1],
        "role": result[2]
    })


if __name__ == "__main__":
    app.run(debug=False)
