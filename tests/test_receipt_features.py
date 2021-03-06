import nose
import unittest
from app.receipt import Receipt
from app.interpreter import Interpreter


class TestReceiptFeatures(unittest.TestCase):
    """Feature Tests for Receipt"""
    def setUp(self):
        self.interpreter = Interpreter()
        self.receipt = Receipt(self.interpreter)

    def test_receipt_displays_restaurant_details(self):
        self.assertEqual(self.receipt.shopName, "The Coffee Connection")
        self.assertEqual(self.receipt.address, "123 Lakeside Way")
        self.assertEqual(self.receipt.phone, "16503600708")

    def test_receipt_displays_correct_tax(self):
        self.assertEqual(self.receipt.tax({"Cafe Latte": 2,
                                            "Blueberry Muffin": 1, "Choc Mudcake": 1}),
                                            round(((2*4.75 + 4.05 + 6.40)*self.receipt.cost._TAX), 2))

    def test_receipt_displays_correct_total_cost(self):
        self.assertEqual(self.receipt.total_cost({"Cafe Latte": 2,
                                            "Blueberry Muffin": 1, "Choc Mudcake": 1}),
                                            round(((2*4.75 + 4.05 + 6.40)*(1 + self.receipt.cost._TAX)), 2))

    def test_receipt_displays_correct_line_totals(self):
       self.assertEqual(self.receipt.line_total({"Cafe Latte": 2,
                                              "Blueberry Muffin": 1, "Choc Mudcake": 1}),
                                              {"Cafe Latte": 2*4.75,
                                                "Blueberry Muffin": 4.05,
                                                "Choc Mudcake": 6.40}
                                              )
