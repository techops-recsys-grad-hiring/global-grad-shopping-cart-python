import src.model.customer as Customer


class Order:
    def __init__(self, customer=Customer, products=[], totalPrice = 0):
        self.customer = customer
        self.products = products
        self.total = totalPrice
        self.order_status = "ORDER_PLACED"
