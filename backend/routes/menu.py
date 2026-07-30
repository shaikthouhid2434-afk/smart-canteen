from flask import Blueprint, jsonify, request
from db import cursor, db

menu_routes = Blueprint('menu', __name__)

# ✅ Get all menu items
@menu_routes.route('/menu', methods=['GET'])
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


# ✅ Add new item (Admin feature)
@menu_routes.route('/menu/add', methods=['POST'])
def add_menu():
    data = request.json

    name = data.get('name')
    price = data.get('price')

    query = "INSERT INTO menu (name, price) VALUES (%s, %s)"
    cursor.execute(query, (name, price))
    db.commit()

    return jsonify({"message": "Menu item added successfully"})


# ✅ Delete item (Admin feature)
@menu_routes.route('/menu/delete/<int:id>', methods=['DELETE'])
def delete_menu(id):
    query = "DELETE FROM menu WHERE id=%s"
    cursor.execute(query, (id,))
    db.commit()

    return jsonify({"message": "Menu item deleted successfully"})