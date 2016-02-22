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
                                            round(self.sample_pretax_cost(), 2))

    def test_tax_gives_tax_amount(self):
        self.assertEqual(self.cost.tax({"Cafe Latte": 2,
                                            "Blueberry Muffin": 1, "Choc Mudcake": 1}),
                                            round(self.sample_pretax_cost()*self.cost._TAX, 2))

    def test_total_cost_gives_total_cost_of_order(self):
        self.assertEqual(self.cost.total_cost({"Cafe Latte": 2,
                                            "Blueberry Muffin": 1, "Choc Mudcake": 1}),
                                            round(self.sample_pretax_cost()*(1 + self.cost._TAX), 2))

    def test_line_total_gives_dict_line_totals(self):
        self.assertEqual(self.cost.line_total({"Cafe Latte": 2,
                                               "Blueberry Muffin": 1, "Choc Mudcake": 1}),
                                               {"Cafe Latte": 2*self.interpreter.price("Cafe Latte"),
                                                 "Blueberry Muffin": self.interpreter.price("Blueberry Muffin"),
                                                 "Choc Mudcake": self.interpreter.price("Choc Mudcake")}
                                               )

    def side_effect(self, value):
        if value == "Cafe Latte":
            return 4.75
        if value == "Blueberry Muffin":
            return 4.05
        if value == "Choc Mudcake":
            return 6.40

    def sample_pretax_cost(self):
        return (2*self.interpreter.price("Cafe Latte")
               + self.interpreter.price("Blueberry Muffin")
               + self.interpreter.price("Choc Mudcake"))
