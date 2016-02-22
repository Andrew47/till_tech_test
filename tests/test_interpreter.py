import nose
import unittest
from app.interpreter import Interpreter

class TestInterpreter(unittest.TestCase):
    """Unit Tests for Interpreter Class"""
    def setUp(self):
        self.interpreter = Interpreter()

    def test_shopName_extracted_from_JSON(self):
        self.assertEqual(self.interpreter.shopName(), "The Coffee Connection")

    def test_address_extracted_from_JSON(self):
        self.assertEqual(self.interpreter.address(), "123 Lakeside Way")

    def test_address_extracted_from_JSON(self):
        self.assertEqual(self.interpreter.phone(), "16503600708")

    def test_price_extracted_from_JSON(self):
        self.assertEqual(self.interpreter.price("Cafe Latte"), 4.75)
