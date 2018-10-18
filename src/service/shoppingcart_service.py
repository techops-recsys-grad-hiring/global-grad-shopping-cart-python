from src.model.shoppingcart import ShoppingCart
from src.model.customer import Customer


def checkout(customer=Customer, products=[]):
    cart = ShoppingCart(customer, products, "OPEN")
    return cart.checkout()
