import unittest
import src.service.order as order_service

class OrderServiceTest(unittest.TestCase):
  def test_should_be_true(self):
   self.assertTrue(True)

  def test_should_show_confirmation(self):
   customer = {}
   products = []
   totalPrice = 0.00
   loyaltyPointsEarned = 1
   result = order_service.show_confirmation(customer, products, totalPrice, loyaltyPointsEarned)
   self.assertTrue(result)