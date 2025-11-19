from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data store
users = {
    1: {"name": "Alice", "email": "alice@example.com"},
    2: {"name": "Bob", "email": "bob@example.com"}
}

# GET all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

# GET single user by ID
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# Create new user (POST)
@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "Invalid data"}), 400

    new_id = max(users.keys()) + 1 if users else 1
    users[new_id] = {"name": data["name"], "email": data["email"]}

    return jsonify({"message": "User created", "id": new_id}), 201

# Update user (PUT)
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    data = request.json
    users[user_id].update(data)

    return jsonify({"message": "User updated", "user": users[user_id]})

# Remove user (DELETE)
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id not in users:
        return jsonify({"error": "User not found"}), 404

    del users[user_id]
    return jsonify({"message": "User deleted"})

if __name__ == "__main__":
    app.run(debug=True)
