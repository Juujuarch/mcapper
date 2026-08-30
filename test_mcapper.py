import unittest

from mcapper import position


class TestPosition(unittest.TestCase):
    def test_known_case(self):
        r = position(100, 10_000, 350_000)
        self.assertAlmostEqual(r["supply_share_pct"], 1.0, places=4)
        self.assertAlmostEqual(r["value"], 3_500, places=2)
        self.assertAlmostEqual(r["multiple"], 35.0, places=6)

    def test_seventy_x(self):
        r = position(100, 10_000, 700_000)
        self.assertAlmostEqual(r["value"], 7_000, places=2)
        self.assertAlmostEqual(r["multiple"], 70.0, places=6)

    def test_five_million(self):
        r = position(100, 10_000, 5_000_000)
        self.assertAlmostEqual(r["value"], 50_000, places=2)
        self.assertAlmostEqual(r["multiple"], 500.0, places=6)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            position(-1, 10_000, 350_000)
        with self.assertRaises(ValueError):
            position(100, 0, 350_000)
        with self.assertRaises(ValueError):
            position(100, 10_000, -5)


if __name__ == "__main__":
    unittest.main()