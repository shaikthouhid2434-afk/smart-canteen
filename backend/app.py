from flask import Flask, request, jsonify
from flask_cors import CORS
from db import cursor, db

app = Flask(__name__)
CORS(app)

# ✅ Test route
@app.route('/')
def home():
    return "Backend Running ✅"


# ✅ Get Menu API
@app.route('/menu', methods=['GET'])
def get_menu():
    cursor.execute("SELECT * FROM menu")
    data = cursor.fetchall()

    menu_list = []
    for item in data:
        menu_list.append({
            "id": item[0],
            "name": item[1],
            "price": item[2]
        })

    return jsonify(menu_list)


# ✅ ADD MENU ITEM (ADMIN)
@app.route('/menu/add', methods=['POST'])
def add_menu():
    data = request.json

    name = data.get('name')
    price = data.get('price')

    query = "INSERT INTO menu (name, price) VALUES (%s, %s)"
    cursor.execute(query, (name, price))
    db.commit()

    return jsonify({"message": "Item added"})


# ✅ Place Order API (NO LOGIN REQUIRED)
@app.route('/order', methods=['POST'])
def place_order():
    data = request.json

    total = data.get('total')

    # Default user_id = 1 (since no login system)
    user_id = 1

    query = "INSERT INTO orders (user_id, total) VALUES (%s, %s)"
    cursor.execute(query, (user_id, total))
    db.commit()

    return jsonify({"message": "Order placed successfully"})


# ✅ GET ALL ORDERS (ADMIN)
@app.route('/orders', methods=['GET'])
def get_orders():
    cursor.execute("SELECT * FROM orders")
    data = cursor.fetchall()

    orders = []
    for item in data:
        orders.append({
            "id": item[0],
            "user_id": item[1],
            "total": item[2]
        })

    return jsonify(orders)


if __name__ == '__main__':
    app.run(debug=True)