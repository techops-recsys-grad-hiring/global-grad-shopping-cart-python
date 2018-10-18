import src.model.customer as Customer
from src.model.shoppingcart import ShoppingCart


class Order(ShoppingCart):
    def __init__(self, customer=Customer, products=[]):
        super.__init__(customer, products, "ORDER_PLACED")
