import nose
import unittest
from app.cost import Cost

class TestCost(unittest.TestCase):
    """Unit Tests for Cost methods"""
    def setUp(self):
        self.cost = Cost()

    def test_tax_gives_tax_amount(self):
        self.assertEqual(self.cost.tax({"Cafe Latte": 2,
                                            "Blueberry Muffin": 1, "Choc Mudcake": 1}),
                                            (2*4.75 + 4.05 + 6.40)*0.0864)
