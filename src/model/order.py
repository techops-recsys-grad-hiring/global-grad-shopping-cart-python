class Order:
    def __init__(self, loyalty_points_earned=0, total_price=0):
        self.loyalty_points = loyalty_points_earned
        self.total = total_price

    def __str__(self):
        return "Total price: %s \nWill receive %s" % (self.total, self.loyalty_points)
