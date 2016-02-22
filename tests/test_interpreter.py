import nose
import unittest
from app.interpreter import Interpreter

class TestInterpreter(unittest.TestCase):
    """Translates JSON file into Python Object"""
    def setUp(self):
        self.interpreter = Interpreter()

    def test_name_extracted_from_JSON(self):
        self.assertEqual(self.interpreter.shopName(), "The Coffee Connection")
