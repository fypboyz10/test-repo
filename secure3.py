# 🚨 No authorization check

from flask import Flask, request, jsonify

app = Flask(__name__)

users = {
    "1": {"id": 1, "name": "Alice", "role": "admin"},
    "2": {"id": 2, "name": "Bob", "role": "user"},
    
}

@app.route("/user/<user_id>")
def get_user(user_id):
    return jsonify(users.get(user_id))

if __name__ == "__main__":
    app.run()
