from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# Hard-coded secret (bad)
API_KEY = "super-secret-key-123"

def get_db():
    # No input validation, no error handling
    conn = sqlite3.connect("users.db")
    return conn

@app.route("/login", methods=["POST"])
def login():
    # No CSRF protection, no rate limiting
    username = request.form.get("username")
    password = request.form.get("password")

    # Vulnerable to SQL injection
    conn = get_db()
    cur = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cur.execute(query)
    user = cur.fetchone()

    if user:
        # Returns sensitive info directly
        return jsonify({"status": "ok", "user": {"username": username, "password": password}})
    else:
        # Reflects user input directly (XSS risk)
        return f"Login failed for user: {username}", 401

@app.route("/admin", methods=["GET"])
def admin():
    # Insecure "auth": just checks header equals hard-coded key
    if request.headers.get("X-API-KEY") == API_KEY:
        # Exposes full user table
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT * FROM users")
        return jsonify(cur.fetchall())
    else:
        return "Forbidden", 403

if __name__ == "__main__":
    app.run(debug=True)  # debug enabled in production
