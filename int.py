from flask import Flask, request, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "name": "Ali", "role": "user"},
    {"id": 2, "name": "Sara", "role": "admin"}
]


@app.route("/delete_user", methods=["POST"])
def delete_user():
    user_id = request.json.get("id")

    global users
    users = [u for u in users if u["id"] != user_id]

    return jsonify({"message": "User deleted"})


if __name__ == "__main__":
    app.run()
