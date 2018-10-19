from src.service.order_service import OrderService
import unittest

from src.model.customer import Customer
from src.model.product import Product
from src.model.shoppingcart import ShoppingCart


class ShoppingCartTest(unittest.TestCase):
    def test_should_validate_information_passed_on_to_confirmation(self):
        cart = ShoppingCart(Customer("test"), [Product(100, "DIS_10_ABCD", "T")], "ANYTHING")

        order_service = FakeOrderService() 

        cart.set_order_service(order_service)

        total = cart.checkout()
        self.assertEqual(90.00, order_service.total_price)


class FakeOrderService(OrderService):

    def show_confirmation(self, customer, products, total_price, loyalty_points_earned):
        self.total_price = total_price
