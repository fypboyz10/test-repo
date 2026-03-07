from flask import Flask, request, jsonify
from functools import wraps

app = Flask(__name__)

users = {
    "1": {"id": 1, "name": "Alice", "role": "admin"},
    "2": {"id": 2, "name": "Bob", "role": "user"},
}

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return jsonify({"error": "Unauthorized"}), 401
        token = auth_header.split(' ')[1]
        # Here you would validate the token against your authentication system
        if token != "valid_token":
            return jsonify({"error": "Invalid token"}), 401
        return f(*args, **kwargs)
    return decorated

@app.route("/user/<user_id>")
@requires_auth
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run()
