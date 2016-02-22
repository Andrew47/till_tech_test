import unittest
from app.receipt import Receipt
from mock import MagicMock


class TestReceipt(unittest.TestCase):
    """Unit Tests for Receipt methods"""
    def setUp(self):
        self.interpreter = MagicMock()
        self.interpreter.shopName = MagicMock(return_value = "The Coffee Connection")
        self.interpreter.address = MagicMock(return_value = "123 Lakeside Way")
        self.receipt = Receipt(self.interpreter)

    def test_receipt_reads_shopName_from_interpreter(self):
        self.assertEqual(self.receipt.shopName, "The Coffee Connection")

    def test_receipt_reads_address_from_interpreter(self):
        self.assertEqual(self.receipt.address, "123 Lakeside Way")

    def test_receipt_reads_phone_from_interpreter(self):
        pass
