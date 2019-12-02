import unittest
from .day_2 import addition, multiplication, parse_instructions


class Day2TestCase(unittest.TestCase):
    def test_opcode_addition(self):
        instructions = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        expected_result = [1, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
        result = addition(instructions, 0)
        self.assertEqual(result, expected_result)

    def test_opcode_multiplication(self):
        instructions = [1, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
        expected_result = [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
        result = multiplication(instructions, 4)
        self.assertEqual(result, expected_result)

    def test_multiple_operation(self):
        params = [
            ([1, 0, 0, 0, 99], [2, 0, 0, 0, 99]),
            ([2, 3, 0, 3, 99], [2, 3, 0, 6, 99]),
            ([2, 4, 4, 5, 99, 0], [2, 4, 4, 5, 99, 9801]),
            ([1, 1, 1, 4, 99, 5, 6, 0, 99], [30, 1, 1, 4, 2, 5, 6, 0, 99])
        ]

        for w, f in params:
            with self.subTest(w=w, f=f):
                self.assertEqual(f, parse_instructions(w))


if __name__ == '__main__':
    unittest.main()
