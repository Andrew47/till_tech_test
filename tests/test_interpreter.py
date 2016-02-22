import nose
import unittest
from app.interpreter import Interpreter

class TestInterpreter(unittest.TestCase):
    """Translates JSON file into Python Object"""
    def setUp(self):
        self.interpreter = Interpreter()

    def test_shopName_extracted_from_JSON(self):
        self.assertEqual(self.interpreter.shopName(), "The Coffee Connection")

    def test_address_extracted_from_JSON(self):
        self.assertEqual(self.interpreter.address(), "123 Lakeside Way")
