import unittest
from .day_4 import is_valid_code, validate_6digits, validate_has_double, validate_no_decreasing


class TestDay4(unittest.TestCase):

    def test_6digits(self):
        params = [
            (111111, True),
            (1234, False)
        ]
        for w, f in params:
            with self.subTest(w=w, f=f):
                self.assertEqual(f, validate_6digits(str(w)))

    def test_has_double(self):
        params = [
            (123789, False),
            (111122, True)
        ]
        for w, f in params:
            with self.subTest(w=w, f=f):
                self.assertEqual(f, validate_has_double(str(w)))

    def test_no_decreasing(self):
        params = [
            (223450, False),
            (111111, True)
        ]
        for w, f in params:
            with self.subTest(w=w, f=f):
                self.assertEqual(f, validate_no_decreasing(str(w)))

    def test_is_valid_code(self):
        params = [
            (111111, False),
            (223450, False),  # decreasing number
            (123789, False),  # no double
            (12345, False),  # need to be 6 digits
            (122345, True),
            (112233, True),
            (123444, False),
            (111122, True)
        ]

        for w, f in params:
            with self.subTest(w=w, f=f):
                self.assertEqual(f, is_valid_code(w))


if __name__ == '__main__':
    unittest.main()
