from src.model.product import Product
from src.model.customer import Customer

class ShoppingCart:
 # customer contains product and quantity
 def __init__(self, customer = Customer, products = [], cart_state = ""):
  self.products = products
  self.customer = customer
  self.cart_state = cart_state
  return

 def set_order_service(self, order_service):
  self.order_service = order_service

 def remove_product(self, product = Product):
  self.products = [p for p in self.products if p.product_code == product.product_code]

 def checkout(self):
  total_price = 0.00
  loyalty_points_earned = 0.00
  for product in self.products:
   discount = 0.00
   if product.product_code.startswith("DIS_10"):
    loyalty_points_earned += (product.price / 10)
    discount = product.price * 0.1
   elif product.product_code.startswith("DIS_15"):
    loyalty_points_earned += (product.price / 15)
    discount = product.price * 0.15
   else:
    loyalty_points_earned += (product.price / 5)
    discount = 0.00
  
  total_price += product.price - discount
  return total_price

