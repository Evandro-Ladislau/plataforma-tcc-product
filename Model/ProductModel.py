from datetime import datetime

class ProductModel:
    def __init__(self, name, dest, quantity, price):
        self.name = name
        self.dest = dest
        self.quantity = quantity
        self.price = price
        self.active = True
        self.creted_at = datetime.now()