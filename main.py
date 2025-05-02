# main.py
from controller import OrderController
from product import Product

# GRASP in action
controller = OrderController()

product1 = Product("Laptop", 1000)
product2 = Product("Mouse", 25)

order = controller.create_order()
order.add_item(product1, 1)
order.add_item(product2, 2)

controller.checkout(order)
