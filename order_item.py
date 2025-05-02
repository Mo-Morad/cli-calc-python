# order_item.py
class OrderItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    # GRASP: Information Expert — this class has both price and quantity
    def subtotal(self):
        return self.product.price * self.quantity
