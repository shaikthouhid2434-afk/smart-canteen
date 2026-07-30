from flask import Blueprint, request, jsonify
from db import cursor, db

order_routes = Blueprint('orders', __name__)

# ✅ Place Order
@order_routes.route('/order', methods=['POST'])
def place_order():
    data = request.json

    user_id = data.get('user_id')
    total = data.get('total')

    query = "INSERT INTO orders (user_id, total) VALUES (%s, %s)"
    cursor.execute(query, (user_id, total))
    db.commit()

    return jsonify({"message": "Order placed successfully"})


# ✅ Get all orders (Admin)
@order_routes.route('/orders', methods=['GET'])
def get_orders():
    cursor.execute("SELECT * FROM orders")
    data = cursor.fetchall()

    orders_list = []
    for order in data:
        orders_list.append({
            "id": order[0],
            "user_id": order[1],
            "total": order[2]
        })

    return jsonify(orders_list)


# ✅ Get orders by user
@order_routes.route('/orders/<int:user_id>', methods=['GET'])
def get_user_orders(user_id):
    query = "SELECT * FROM orders WHERE user_id=%s"
    cursor.execute(query, (user_id,))
    data = cursor.fetchall()

    user_orders = []
    for order in data:
        user_orders.append({
            "id": order[0],
            "user_id": order[1],
            "total": order[2]
        })

    return jsonify(user_orders)


# ✅ Delete order (Admin)
@order_routes.route('/order/delete/<int:id>', methods=['DELETE'])
def delete_order(id):
    query = "DELETE FROM orders WHERE id=%s"
    cursor.execute(query, (id,))
    db.commit()

    return jsonify({"message": "Order deleted successfully"})