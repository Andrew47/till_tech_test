from app.interpreter import Interpreter

class Receipt(object):
    """Displays information to customer"""
    def __init__(self, interpreter=Interpreter()):
        self.interpreter = interpreter
        self.shopName = self.interpreter.shopName()
        self.address = self.interpreter.address()
        self.phone = self.interpreter.phone()
