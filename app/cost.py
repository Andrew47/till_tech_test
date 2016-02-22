from app.interpreter import Interpreter


class Cost(object):
    """Calculates the costs associated with an order"""
    def __init__(self, interpreter=Interpreter()):
        self.interpreter = interpreter
        self._TAX = 0.0864

    def pretax(self, order):
        total = []
        for item in order:
            total.append(self.price(item) * order[item])
        return reduce(self.add, total)

    def tax(self, order):
        tax = (self.pretax(order))*self._TAX
        return round(tax, 2)

    def price(self, item):
        return self.interpreter.price(item)

    def add(self, x, y):
        return x + y
