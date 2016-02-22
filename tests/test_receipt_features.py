import nose
import unittest
import app.receipt


class TestReceiptFeatures(unittest.TestCase):
    def setUp(self):
        self.receipt = Receipt()

    def test_receipt_displays_restaurant_details(self):
        self.assertEqual(self.receipt.details['name'], "The Coffee Connection")
        self.assertEqual(self.receipt.details['address'], "123 Lakeside Way")
        self.assertEqual(self.receipt.details['address'], "16503600708")
