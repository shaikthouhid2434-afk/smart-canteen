from flask import Blueprint, request, jsonify
from db import cursor, db

auth_routes = Blueprint('auth', __name__)

# Register
@auth_routes.route('/register', methods=['POST'])
def register():
    data = request.json

    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    query = "INSERT INTO users (name,email,password) VALUES (%s,%s,%s)"
    cursor.execute(query, (name, email, password))
    db.commit()

    return jsonify({"message": "User registered successfully"})


# Login
@auth_routes.route('/login', methods=['POST'])
def login():
    data = request.json

    email = data.get('email')
    password = data.get('password')

    query = "SELECT * FROM users WHERE email=%s AND password=%s"
    cursor.execute(query, (email, password))
    user = cursor.fetchone()

    if user:
        return jsonify({"message": "Login successful", "user_id": user[0]})
    else:
        return jsonify({"message": "Invalid credentials"}), 401