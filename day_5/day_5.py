import sys


class Operation:
    operation_size = 4

    @property
    def size(self):
        return self.operation_size

    def execute(self, instructions, offset):
        raise NotImplemented


class Addition(Operation):

    def __init__(self, param_1_is_position, param_2_is_position):
        self.param1_is_position = param_1_is_position
        self.param2_is_position = param_2_is_position

    def execute(self, instructions, offset):
        value_1 = instructions[instructions[1 + offset]] if self.param1_is_position else instructions[1 + offset]
        value_2 = instructions[instructions[2 + offset]] if self.param2_is_position else instructions[2 + offset]
        index_store_result = instructions[3 + offset]
        instructions[index_store_result] = value_1 + value_2
        return instructions


class Multiplication(Operation):
    def __init__(self, param_1_is_position, param_2_is_position):
        self.param1_is_position = param_1_is_position
        self.param2_is_position = param_2_is_position

    def execute(self, instructions, offset):
        value_1 = instructions[instructions[1 + offset]] if self.param1_is_position else instructions[1 + offset]
        value_2 = instructions[instructions[2 + offset]] if self.param2_is_position else instructions[2 + offset]
        index_store_result = instructions[3 + offset]
        instructions[index_store_result] = value_1 * value_2
        return instructions


class Input(Operation):
    operation_size = 2

    def execute(self, instructions, offset):
        value = int(input("Enter an integer"))
        index_store_result = instructions[1 + offset]
        instructions[index_store_result] = value
        return instructions


class Output(Operation):
    operation_size = 2

    def __init__(self, param_1_is_position):
        self.param1_is_position = param_1_is_position

    def execute(self, instructions, offset):
        value = instructions[instructions[1 + offset]] if self.param1_is_position else instructions[1 + offset]
        print(value)


class Halt(Operation):
    operation_size = 1

    def execute(self, instructions, offset):
        self.operation_size = len(instructions) + 1


class JumpIfTrue(Operation):
    operation_size = 3

    def __init__(self, param_1_is_position, param_2_is_position):
        self.param1_is_position = param_1_is_position
        self.param2_is_position = param_2_is_position

    def execute(self, instructions, offset):
        value = instructions[instructions[1 + offset]] if self.param1_is_position else instructions[1 + offset]
        index = instructions[instructions[2 + offset]] if self.param2_is_position else instructions[2 + offset]

        if value:
            self.operation_size = index - offset
        else:
            self.operation_size = 3


class JumpIfFalse(Operation):
    operation_size = 3

    def __init__(self, param_1_is_position, param_2_is_position):
        self.param1_is_position = param_1_is_position
        self.param2_is_position = param_2_is_position

    def execute(self, instructions, offset):
        value = instructions[instructions[1 + offset]] if self.param1_is_position else instructions[1 + offset]
        index = instructions[instructions[2 + offset]] if self.param2_is_position else instructions[2 + offset]

        if not value:
            self.operation_size = index - offset
        else:
            self.operation_size = 3


class LessThan(Operation):
    operation_size = 4

    def __init__(self, param_1_is_position, param_2_is_position):
        self.param1_is_position = param_1_is_position
        self.param2_is_position = param_2_is_position

    def execute(self, instructions, offset):
        value_1 = instructions[instructions[1 + offset]] if self.param1_is_position else instructions[1 + offset]
        value_2 = instructions[instructions[2 + offset]] if self.param2_is_position else instructions[2 + offset]

        instructions[instructions[3 + offset]] = 1 if value_1 < value_2 else 0


class Equal(Operation):
    operation_size = 4

    def __init__(self, param_1_is_position, param_2_is_position):
        self.param1_is_position = param_1_is_position
        self.param2_is_position = param_2_is_position

    def execute(self, instructions, offset):
        value_1 = instructions[instructions[1 + offset]] if self.param1_is_position else instructions[1 + offset]
        value_2 = instructions[instructions[2 + offset]] if self.param2_is_position else instructions[2 + offset]

        instructions[instructions[3 + offset]] = 1 if value_1 == value_2 else 0


def parse_operation(operator):
    operator_string = str(operator)
    length = len(operator_string)
    params = {}
    for x in range(length - 2):
        x_int = int(x)
        params[x] = int(operator_string[length - 3 - x])

    return {
        'op_code': int(operator_string[length - 2: length]),
        'params': params
    }


class OperatorFactory:
    @staticmethod
    def create(op_code):

        param1_is_position = True
        param2_is_position = True
        if op_code > 99:
            op_data = parse_operation(op_code)
            op_code = op_data.get("op_code")
            if 0 in op_data['params']:
                param1_is_position = not op_data['params'][0]
            if 1 in op_data['params']:
                param2_is_position = not op_data['params'][1]

        if op_code == 1:
            return Addition(param1_is_position, param2_is_position)
        elif op_code == 2:
            return Multiplication(param1_is_position, param2_is_position)
        elif op_code == 99:
            return Halt()
        elif op_code == 3:
            return Input()
        elif op_code == 4:
            return Output(param1_is_position)
        elif op_code == 5:
            return JumpIfTrue(param1_is_position, param2_is_position)
        elif op_code == 6:
            return JumpIfFalse(param1_is_position, param2_is_position)
        elif op_code == 7:
            return LessThan(param1_is_position, param2_is_position)
        elif op_code == 8:
            return Equal(param1_is_position, param2_is_position)
        else:
            raise Exception(op_code)


def parse_instructions(instructions):
    index = 0
    max_index = len(instructions)
    while index < max_index:
        operator = instructions[index]
        op = OperatorFactory.create(operator)
        op.execute(instructions, index)
        index += op.operation_size
        # print(instructions)
    return instructions


def main():
    instructions = [3, 225, 1, 225, 6, 6, 1100, 1, 238, 225, 104, 0, 1102, 72, 20, 224, 1001, 224, -1440, 224,
                    4, 224, 102, 8, 223, 223, 1001, 224, 5, 224, 1, 224, 223, 223, 1002, 147, 33, 224, 101,
                    -3036, 224, 224, 4, 224, 102, 8, 223, 223, 1001, 224, 5, 224, 1, 224, 223, 223, 1102, 32,
                    90, 225, 101, 65, 87, 224, 101, -85, 224, 224, 4, 224, 1002, 223, 8, 223, 101, 4, 224, 224,
                    1, 223, 224, 223, 1102, 33, 92, 225, 1102, 20, 52, 225, 1101, 76, 89, 225, 1, 117, 122, 224,
                    101, -78, 224, 224, 4, 224, 102, 8, 223, 223, 101, 1, 224, 224, 1, 223, 224, 223, 1102, 54,
                    22, 225, 1102, 5, 24, 225, 102, 50, 84, 224, 101, -4600, 224, 224, 4, 224, 1002, 223, 8,
                    223, 101, 3, 224, 224, 1, 223, 224, 223, 1102, 92, 64, 225, 1101, 42, 83, 224, 101, -125,
                    224, 224, 4, 224, 102, 8, 223, 223, 101, 5, 224, 224, 1, 224, 223, 223, 2, 58, 195, 224,
                    1001, 224, -6840, 224, 4, 224, 102, 8, 223, 223, 101, 1, 224, 224, 1, 223, 224, 223, 1101,
                    76, 48, 225, 1001, 92, 65, 224, 1001, 224, -154, 224, 4, 224, 1002, 223, 8, 223, 101, 5,
                    224, 224, 1, 223, 224, 223, 4, 223, 99, 0, 0, 0, 677, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1105,
                    0, 99999, 1105, 227, 247, 1105, 1, 99999, 1005, 227, 99999, 1005, 0, 256, 1105, 1, 99999,
                    1106, 227, 99999, 1106, 0, 265, 1105, 1, 99999, 1006, 0, 99999, 1006, 227, 274, 1105, 1,
                    99999, 1105, 1, 280, 1105, 1, 99999, 1, 225, 225, 225, 1101, 294, 0, 0, 105, 1, 0, 1105, 1,
                    99999, 1106, 0, 300, 1105, 1, 99999, 1, 225, 225, 225, 1101, 314, 0, 0, 106, 0, 0, 1105, 1,
                    99999, 1107, 677, 226, 224, 1002, 223, 2, 223, 1005, 224, 329, 101, 1, 223, 223, 7, 677,
                    226, 224, 102, 2, 223, 223, 1005, 224, 344, 1001, 223, 1, 223, 1107, 226, 226, 224, 1002,
                    223, 2, 223, 1006, 224, 359, 1001, 223, 1, 223, 8, 226, 226, 224, 1002, 223, 2, 223, 1006,
                    224, 374, 101, 1, 223, 223, 108, 226, 226, 224, 102, 2, 223, 223, 1005, 224, 389, 1001, 223,
                    1, 223, 1008, 226, 226, 224, 1002, 223, 2, 223, 1005, 224, 404, 101, 1, 223, 223, 1107, 226,
                    677, 224, 1002, 223, 2, 223, 1006, 224, 419, 101, 1, 223, 223, 1008, 226, 677, 224, 1002,
                    223, 2, 223, 1006, 224, 434, 101, 1, 223, 223, 108, 677, 677, 224, 1002, 223, 2, 223, 1006,
                    224, 449, 101, 1, 223, 223, 1108, 677, 226, 224, 102, 2, 223, 223, 1006, 224, 464, 1001,
                    223, 1, 223, 107, 677, 677, 224, 102, 2, 223, 223, 1005, 224, 479, 101, 1, 223, 223, 7, 226,
                    677, 224, 1002, 223, 2, 223, 1006, 224, 494, 1001, 223, 1, 223, 7, 677, 677, 224, 102, 2,
                    223, 223, 1006, 224, 509, 101, 1, 223, 223, 107, 226, 677, 224, 1002, 223, 2, 223, 1006,
                    224, 524, 1001, 223, 1, 223, 1007, 226, 226, 224, 102, 2, 223, 223, 1006, 224, 539, 1001,
                    223, 1, 223, 108, 677, 226, 224, 102, 2, 223, 223, 1005, 224, 554, 101, 1, 223, 223, 1007,
                    677, 677, 224, 102, 2, 223, 223, 1006, 224, 569, 101, 1, 223, 223, 8, 677, 226, 224, 102, 2,
                    223, 223, 1006, 224, 584, 1001, 223, 1, 223, 1008, 677, 677, 224, 1002, 223, 2, 223, 1006,
                    224, 599, 1001, 223, 1, 223, 1007, 677, 226, 224, 1002, 223, 2, 223, 1005, 224, 614, 101, 1,
                    223, 223, 1108, 226, 677, 224, 1002, 223, 2, 223, 1005, 224, 629, 101, 1, 223, 223, 1108,
                    677, 677, 224, 1002, 223, 2, 223, 1005, 224, 644, 1001, 223, 1, 223, 8, 226, 677, 224, 1002,
                    223, 2, 223, 1006, 224, 659, 101, 1, 223, 223, 107, 226, 226, 224, 102, 2, 223, 223, 1005,
                    224, 674, 101, 1, 223, 223, 4, 223, 99, 226]

    instructions = parse_instructions(instructions)


if __name__ == '__main__':
    main()
