import unittest
from .day_1 import calculate_fuel, fuel_of_fuel


class Day1IntegrationTest(unittest.TestCase):
    def test_mass_12(self):
        fuel = calculate_fuel(12)
        self.assertEqual(fuel, 2)

    def test_mass_14(self):
        fuel = calculate_fuel(14)
        self.assertEqual(fuel, 2)

    def test_mass_1969(self):
        fuel = calculate_fuel(1969)
        self.assertEqual(fuel, 654)

    def test_mass_100756(self):
        fuel = calculate_fuel(100756)
        self.assertEqual(fuel, 33583)

    def test_fuel_of_fuel(self):
        params = [
            (14, 2),
            (1969, 966),
            (100756, 50346)
        ]

        for w, f in params:
            with self.subTest(w=w, f=f):
                self.assertEqual(f, fuel_of_fuel(w))


if __name__ == '__main__':
    unittest.main()
