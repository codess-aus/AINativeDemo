import random
import unittest


class FlakyDemoTests(unittest.TestCase):
    @unittest.skip("Intentional demo issue: flaky test to be fixed in backlog item #001")
    def test_checkout_id_is_even(self) -> None:
        checkout_id = random.randint(1, 100)
        self.assertEqual(checkout_id % 2, 0)


if __name__ == "__main__":
    unittest.main()
