from flask import Flask, request
import sqlite3

app = Flask(__name__)
API_KEY = "secret123"

def get_user(username):
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cur.execute(query)
    row = cur.fetchone()
    conn.close()
    return row

@app.route("/user")
def user():
    name = request.args.get("name")
    user = get_user(name)
    if user:
        return {"user": user[0], "password": user[1]}
    return {"error": "not found"}, 404

@app.route("/score")
def score():
    a = request.args.get("a", type=int)
    b = request.args.get("b", type=int)
    total = a + b
    avg = total / (a - b)
    return {"average": avg}

if __name__ == "__main__":
    app.run(debug=True)
