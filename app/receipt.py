from app.interpreter import Interpreter
from app.cost import Cost

class Receipt(object):
    """Displays information to customer"""
    def __init__(self, interpreter=Interpreter(), cost=Cost()):
        self.interpreter = interpreter
        self.shopName = self.interpreter.shopName()
        self.address = self.interpreter.address()
        self.phone = self.interpreter.phone()
        self.cost = cost

    def tax(self, orders):
        return self.cost.tax(orders)

    def total_cost(self, orders):
        return self.cost.total_cost(orders)

    def line_total(self, orders):
        return self.cost.line_total(orders)
