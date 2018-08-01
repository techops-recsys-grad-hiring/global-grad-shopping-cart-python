import unittest
from src.model.customer import Customer
from src.model.product import Product
from src.model.shoppingcart import ShoppingCart
import src.service.shoppingcart_service as ShoppingCartService
import src.service.order_service as OrderService

class ShoppingCartServiceTest(unittest.TestCase):
  def test_should_validate_information_passed_on_to_confirmation(self):
   cart = ShoppingCart(Customer("test"), [Product(100, "DIS_10_ABCD", "T")], "ANYTHING")
   fake_order_service = OrderService
   cart.set_order_service(fake_order_service)
   actual_total_price = cart.checkout()
   self.assertEqual(90.00, actual_total_price)
