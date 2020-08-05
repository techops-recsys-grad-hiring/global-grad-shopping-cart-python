class Product:
    def __init__(self, price, product_code, name):
        self.price = price
        self.product_code = product_code
        self.name = name

    def __str__(self):
        return " Name: %s \n Price: %s \n" % (self.name, self.price)