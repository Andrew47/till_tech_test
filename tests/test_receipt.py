import unittest
from app.receipt import Receipt
from mock import MagicMock


class TestReceipt(unittest.TestCase):
    """Unit Tests for Receipt methods"""
    def setUp(self):
        self.interpreter = MagicMock()
        self.interpreter = MagicMock(return_value = {"name": "The Coffee Connection",
                                                     "address": "123 Lakeside Way",
                                                     "telephone": "16503600708"
                                                     })
        self.receipt = Receipt(self.interpreter)

    def test_name_extracted_from_interpreter(self):
        pass
