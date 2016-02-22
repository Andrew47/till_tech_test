from app.interpreter import Interpreter

class Receipt(object):
    """Displays information to customer"""
    def __init__(self, interpreter):
        self.interpreter = interpreter
        self.details = self.interpreter.details
