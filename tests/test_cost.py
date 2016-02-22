import nose
import unittest
from app.cost import Cost
from mock import MagicMock

class TestCost(unittest.TestCase):
    """Unit Tests for Cost methods"""
    def setUp(self):
        self.interpreter = MagicMock()
        self.interpreter.price = MagicMock(side_effect=self.side_effect)
        self.cost = Cost(self.interpreter)

    def test_price_gives_correct_price(self):
        self.assertEqual(self.cost.price("Cafe Latte"), 4.75)

    def test_pretax_gives_pretax_amount(self):
        self.assertEqual(self.cost.pretax({"Cafe Latte": 2,
                                            "Blueberry Muffin": 1, "Choc Mudcake": 1}),
                                            round((2*4.75 + 4.05 + 6.40), 2))

    def side_effect(self, value):
        if value == "Cafe Latte":
            return 4.75
        if value == "Blueberry Muffin":
            return 4.05
        if value == "Choc Mudcake":
            return 6.40
