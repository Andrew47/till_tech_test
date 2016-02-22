import unittest
from app.receipt import Receipt
from mock import MagicMock


class TestReceipt(unittest.TestCase):
    """Unit Tests for Receipt methods"""
    def setUp(self):
        self.interpreter = MagicMock()
        self.interpreter.name = MagicMock(return_value = "The Coffee Connection")
        self.receipt = Receipt(self.interpreter)

    def test_receipt_reads_name_from_interpreter(self):
        self.assertEqual(self.receipt.name, "The Coffee Connection")
