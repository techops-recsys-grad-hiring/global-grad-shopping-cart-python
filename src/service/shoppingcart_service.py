from src.model.shoppingcart import ShoppingCart
from src.model.customer import Customer

class ShoppingCartService:
    def checkout(self, customer=Customer, products=[]):
        cart = ShoppingCart(customer, products, "OPEN")
        return cart.checkout()
