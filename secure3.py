from flask import Flask, request, jsonify

app = Flask(__name__)

users = {
    "1": {"id": 1, "name": "Alice", "role": "admin"},
    "2": {"id": 2, "name": "Bob", "role": "user"},
}

@app.route("/user/<user_id>")
def get_user(user_id):
    user = users.get(user_id)
    if user and user["role"] == "admin":
        return jsonify(user)
    else:
        return jsonify({"error": "Unauthorized"}), 403

if __name__ == "__main__":
    app.run()
