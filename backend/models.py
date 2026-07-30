# This file defines data structures (models)
# Not mandatory for simple projects, but useful for clean code

class User:
    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
        }


class MenuItem:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price
        }


class Order:
    def __init__(self, id, user_id, total):
        self.id = id
        self.user_id = user_id
        self.total = total

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "total": self.total
        }