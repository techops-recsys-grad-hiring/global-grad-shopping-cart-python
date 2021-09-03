import unittest

from src.model.product import Product

PRICE = 300
PRODUCT = "PROD_NAME"
DIS_COUNT = "DIS_10"

class ProductTest(unittest.TestCase):
    def test_product_name_is_valid(self):
        products = [Product(PRICE, DIS_COUNT, ""), Product(PRICE, DIS_COUNT, PRODUCT)]
        for i, p in enumerate(products):
            self.assertIsInstance(p, Product)
            self.assertIsInstance(p.name, str)
            self.assertIsInstance(p.product_code, str)
            if i == 0:
                self.assertFalse(len(p.name) > 0)
            else:
                self.assertTrue(len(p.name) > 0)
