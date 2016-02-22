import unittest
from app.receipt import Receipt
from mock import MagicMock


class TestReceipt(unittest.TestCase):
    """Unit Tests for Receipt methods"""
    def setUp(self):
        self.interpreter = MagicMock()
        self.interpreter.shopName = MagicMock(return_value = "The Coffee Connection")
        self.interpreter.address = MagicMock(return_value = "123 Lakeside Way")
        self.interpreter.phone = MagicMock(return_value = "16503600708")
        self.cost = MagicMock()
        self.cost.tax = MagicMock(return_value = 5)
        self.receipt = Receipt(self.interpreter, self.cost)

    def test_receipt_reads_shopName_from_interpreter(self):
        self.assertEqual(self.receipt.shopName, "The Coffee Connection")

    def test_receipt_reads_address_from_interpreter(self):
        self.assertEqual(self.receipt.address, "123 Lakeside Way")

    def test_receipt_reads_phone_from_interpreter(self):
        self.assertEqual(self.receipt.phone, "16503600708")

    def test_receipt_reads_tax_from_cost(self):
        self.assertEqual(self.receipt.tax({}), 5)

    def test_receipt_sends_order_to_get_tax(self):
        self.receipt.tax({})
        self.cost.tax.assert_called_once_with({})
