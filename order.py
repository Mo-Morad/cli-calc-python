# order.py
class Order:
    def __init__(self):
        self.items = []

    # GRASP: Creator — Order creates OrderItem because it aggregates them
    def add_item(self, product, quantity):
        item = OrderItem(product, quantity)
        self.items.append(item)

