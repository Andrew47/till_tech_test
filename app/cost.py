from app.interpreter import Interpreter


class Cost(object):
    """Calculates the costs associated with an order"""
    def __init__(self, interpreter=Interpreter()):
        self.interpreter = interpreter
        self._TAX = 0.0864

    def pretax(self, order):
        return reduce(self.add, self.cost_list(order))

    def cost_list(self, order):
        total = []
        for item in order:
            total.append(self.price(item) * order[item])
        return total

    def unrounded_tax(self, order):
        return (self.pretax(order))*self._TAX

    def tax(self, order):
        return round(self.unrounded_tax(order), 2)

    def total_cost(self, order):
        total_cost = self.pretax(order) + self.unrounded_tax(order)
        return round(total_cost, 2)

    def price(self, item):
        return self.interpreter.price(item)

    def add(self, x, y):
        return x + y
