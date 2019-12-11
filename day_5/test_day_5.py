import builtins
import sys
import unittest
from unittest.mock import Mock

from .day_5 import Addition, Multiplication, parse_instructions, Input, Output, parse_operation, JumpIfTrue, \
    JumpIfFalse, LessThan, Equal


class Day2TestCase(unittest.TestCase):
    def test_opcode_addition(self):
        instructions = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        expected_result = [1, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
        op = Addition(1, 1)
        result = op.execute(instructions, 0)
        self.assertEqual(result, expected_result)

    def test_opcode_multiplication(self):
        instructions = [1, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
        expected_result = [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
        op = Multiplication(1, 1)
        result = op.execute(instructions, 4)
        self.assertEqual(result, expected_result)

    # def test_multiple_operation(self):
    #     params = [
    #         ([1, 0, 0, 0, 99], [2, 0, 0, 0, 99]),
    #         ([2, 3, 0, 3, 99], [2, 3, 0, 6, 99]),
    #         ([2, 4, 4, 5, 99, 0], [2, 4, 4, 5, 99, 9801]),
    #         ([1, 1, 1, 4, 99, 5, 6, 0, 99], [30, 1, 1, 4, 2, 5, 6, 0, 99])
    #     ]
    #
    #     for w, f in params:
    #         with self.subTest(w=w, f=f):
    #             self.assertEqual(f, parse_instructions(w))

    def test_input(self):
        builtins.input = Mock()
        input.return_value = 1
        instructions = [3, 4, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
        expected_result = [3, 4, 10, 70, 1, 3, 11, 0, 99, 30, 40, 50]
        op = Input()
        result = op.execute(instructions, 0)
        self.assertEqual(expected_result, result)

    def test_output(self):
        builtins.print = Mock()
        instructions = [4, 4, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
        op = Output(1)
        op.execute(instructions, 0)
        builtins.print.assert_called_once_with(2)

    def test_integration_input_output(self):
        builtins.input = Mock()
        input.return_value = 1010
        builtins.print = Mock()
        instructions = [3, 0, 4, 0, 99]
        parse_instructions(instructions)
        builtins.input.assert_called_once()
        builtins.print.assert_called_once_with(1010)

    def test_immediate(self):
        instructions = [1002, 4, 3, 4, 33]
        expected_result = [1002, 4, 3, 4, 99]
        result = parse_instructions(instructions)
        self.assertEqual(expected_result, result)

    def test_parse_operation(self):
        operator = 1002
        value = parse_operation(operator)

        print(value)
        self.assertEqual(2, value['op_code'])
        self.assertEqual(0, value['params'][0])
        self.assertEqual(1, value['params'][1])

    def test_jump_if_true(self):
        instructions = [5, 4, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
        op = JumpIfTrue(1)
        op.execute(instructions, 0)

        self.assertEqual(40, op.operation_size)

        instructions = [5, 4, 10, 70, 0, 3, 11, 0, 99, 30, 40, 50]
        op = JumpIfTrue(1)
        op.execute(instructions, 0)

        self.assertEqual(3, op.operation_size)

    def test_jump_if_false(self):
        instructions = [5, 4, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
        op = JumpIfFalse(1)
        op.execute(instructions, 0)

        self.assertEqual(3, op.operation_size)

        instructions = [5, 3, 10, 0, 2, 3, 11, 0, 99, 30, 40, 50]
        op = JumpIfFalse(1)
        op.execute(instructions, 0)

        self.assertEqual(40, op.operation_size)

    def test_less_than(self):
        instructions = [7, 4, 10, 4, 2, 3, 11, 0, 99, 30, 40, 50]
        op = LessThan(1, 1)
        op.execute(instructions, 0)

        self.assertEqual(4, op.operation_size)
        expected_instructions = [7, 4, 10, 4, 1, 3, 11, 0, 99, 30, 40, 50]
        self.assertEqual(expected_instructions, instructions)

        instructions = [7, 10, 4, 4, 2, 3, 11, 0, 99, 30, 40, 50]
        op = LessThan(1, 1)
        op.execute(instructions, 0)

        self.assertEqual(4, op.operation_size)
        expected_instructions = [7, 10, 4, 4, 0, 3, 11, 0, 99, 30, 40, 50]
        self.assertEqual(expected_instructions, instructions)

    def test_equal(self):
        instructions = [8, 10, 10, 4, 2, 3, 11, 0, 99, 30, 40, 50]
        op = Equal(1, 1)
        op.execute(instructions, 0)

        self.assertEqual(4, op.operation_size)
        expected_instructions = [8, 10, 10, 4, 1, 3, 11, 0, 99, 30, 40, 50]
        self.assertEqual(expected_instructions, instructions)

        instructions = [8, 10, 4, 4, 2, 3, 11, 0, 99, 30, 40, 50]
        op = Equal(1, 1)
        op.execute(instructions, 0)

        self.assertEqual(4, op.operation_size)
        expected_instructions = [8, 10, 4, 4, 0, 3, 11, 0, 99, 30, 40, 50]
        self.assertEqual(expected_instructions, instructions)

    def test_something(self):
        instructions = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
        builtins.input = Mock()
        builtins.print = Mock()
        input.return_value = 8
        parse_instructions(instructions)
        builtins.print.assert_called_once_with(1)

        instructions = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
        builtins.input = Mock()
        builtins.print = Mock()
        input.return_value = 1
        parse_instructions(instructions)
        builtins.print.assert_called_once_with(0)

    def test_something_2(self):
        instructions = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
        builtins.input = Mock()
        builtins.print = Mock()
        input.return_value = 7
        parse_instructions(instructions)
        builtins.print.assert_called_once_with(1)

        instructions = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
        builtins.input = Mock()
        builtins.print = Mock()
        input.return_value = 10
        parse_instructions(instructions)
        builtins.print.assert_called_once_with(0)

    def test_something_3(self):
        instructions = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
        builtins.input = Mock()
        builtins.print = Mock()
        input.return_value = 8
        parse_instructions(instructions)
        builtins.print.assert_called_once_with(1)

        instructions = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
        builtins.input = Mock()
        builtins.print = Mock()
        input.return_value = 11
        parse_instructions(instructions)
        builtins.print.assert_called_once_with(0)

    def test_something_4(self):
        instructions = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
        builtins.input = Mock()
        builtins.print = Mock()
        input.return_value = 7
        parse_instructions(instructions)
        builtins.print.assert_called_once_with(1)

        instructions = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
        builtins.input = Mock()
        builtins.print = Mock()
        input.return_value = 11
        parse_instructions(instructions)
        builtins.print.assert_called_once_with(0)

    def test_something_5(self):
        instructions = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
        builtins.input = Mock()
        builtins.print = Mock()
        input.return_value = 0
        parse_instructions(instructions)
        builtins.print.assert_called_once_with(0)

        instructions = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
        builtins.input = Mock()
        builtins.print = Mock()
        input.return_value = 100
        parse_instructions(instructions)
        builtins.print.assert_called_once_with(1)

    def test_something_6(self):
        instructions = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
        builtins.input = Mock()
        builtins.print = Mock()
        input.return_value = 0
        parse_instructions(instructions)
        builtins.print.assert_called_once_with(0)

        instructions = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
        builtins.input = Mock()
        builtins.print = Mock()
        input.return_value = 100
        parse_instructions(instructions)
        builtins.print.assert_called_once_with(1)


if __name__ == '__main__':
    unittest.main()
