import unittest
from decimal import Decimal

from demo.python_app_demo.app.pricing import calculate_total


class PricingTests(unittest.TestCase):
    def test_calculate_total_rounds_to_cents(self) -> None:
        self.assertEqual(calculate_total(Decimal("10.00"), Decimal("0.085")), Decimal("10.85"))


if __name__ == "__main__":
    unittest.main()
