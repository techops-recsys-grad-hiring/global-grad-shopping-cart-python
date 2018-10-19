from src.model.order import Order
from src.model.customer import Customer

class OrderService:

    def show_confirmation(self, customer, products, total_price, loyalty_points_earned):
        # show confirmation
        # do some calculations and formatting on the shopping cart data and ask user for confirmation
        # after confirmation, redirect to place order
        return 


    def placeOrder(self, customer=Customer, products=[]):
        # place order
        return Order(customer, products)
