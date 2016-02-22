import nose
import unittest
from app.receipt import Receipt
from app.interpreter import Interpreter


class TestReceiptFeatures(unittest.TestCase):
    def setUp(self):
        self.interpreter = Interpreter()
        self.receipt = Receipt(self.interpreter)

    def test_receipt_displays_restaurant_details(self):
        self.assertEqual(self.receipt.read_details['name'], "The Coffee Connection")
        self.assertEqual(self.receipt.read_details['address'], "123 Lakeside Way")
        self.assertEqual(self.receipt.read_details['telephone'], "16503600708")
