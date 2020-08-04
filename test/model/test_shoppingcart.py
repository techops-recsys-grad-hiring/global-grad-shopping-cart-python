import unittest

from src.model.customer import Customer
from src.model.product import Product
from src.model.shoppingcart import ShoppingCart

CUSTOMER = Customer("test")
PRICE = 100
PRODUCT = "T"


class ShoppingCartTest(unittest.TestCase):
    def test_should_calculate_price_with_no_discount(self):
        products = [Product(PRICE, "", PRODUCT)]
        cart = ShoppingCart(CUSTOMER, products)

        order = cart.checkout()

        self.assertEqual(100.00, order.total)

    def test_should_calculate_loyalty_points_with_no_discount(self):
        products = [Product(PRICE, "", PRODUCT)]
        cart = ShoppingCart(CUSTOMER, products)

        order = cart.checkout()

        self.assertEqual(20, order.loyalty_points)

    def test_should_calculate_price_with_10_percent_discount(self):
        products = [Product(PRICE, "DIS_10_ABCD", PRODUCT)]
        cart = ShoppingCart(CUSTOMER, products)

        order = cart.checkout()

        self.assertEqual(90.00, order.total)

    def test_should_calculate_loyalty_points_with_10_percent_discount(self):
        products = [Product(PRICE, "DIS_10_ABCD", PRODUCT)]
        cart = ShoppingCart(CUSTOMER, products)

        order = cart.checkout()

        self.assertEqual(10, order.loyalty_points)

    def test_should_calculate_price_with_15_percent_discount(self):
        products = [Product(PRICE, "DIS_15_ABCD", PRODUCT)]
        cart = ShoppingCart(CUSTOMER, products)

        order = cart.checkout()

        self.assertEqual(85.00, order.total)

    def test_should_calculate_loyalty_points_with_15_percent_discount(self):
        products = [Product(PRICE, "DIS_15_ABCD", PRODUCT)]
        cart = ShoppingCart(CUSTOMER, products)

        order = cart.checkout()

        self.assertEqual(6, order.loyalty_points)
