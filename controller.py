from order import Order

class OrderController:
    def __init__(self):
        self.orders = []

    # GRASP: Controller — this class handles external system requests
    def create_order(self):
        order = Order()
        self.orders.append(order)
        return order

    def checkout(self, order):
        total = sum(item.subtotal() for item in order.items)
        print(f"Order total: ${total:.2f}")
