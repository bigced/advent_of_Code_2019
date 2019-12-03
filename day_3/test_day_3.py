import unittest
from .day3 import distance, Wire, MoveRight, MoveDown, MoveUp, MoveLeft, get_list_of_command, \
    get_lowest_intersection_distance, get_lowest_steps


class TestDay3(unittest.TestCase):
    def test_distance(self):
        result = distance((3, 3))
        self.assertEqual(result, 6)

    def test_right(self):
        wire = Wire()
        command = MoveRight(75)
        command.execute(wire)
        self.assertEqual(wire.x, 75)
        self.assertEqual(wire.position[0], 75)
        self.assertEqual(wire.y, 0)
        self.assertEqual(wire.position[1], 0)

    def test_down(self):
        wire = Wire()
        command = MoveDown(75)
        command.execute(wire)
        self.assertEqual(wire.x, 0)
        self.assertEqual(wire.position[0], 0)
        self.assertEqual(wire.y, -75)
        self.assertEqual(wire.position[1], -75)

    def test_up(self):
        wire = Wire()
        command = MoveUp(75)
        command.execute(wire)
        self.assertEqual(wire.x, 0)
        self.assertEqual(wire.position[0], 0)
        self.assertEqual(wire.y, 75)
        self.assertEqual(wire.position[1], 75)

    def test_left(self):
        wire = Wire()
        command = MoveLeft(75)
        command.execute(wire)
        self.assertEqual(wire.x, -75)
        self.assertEqual(wire.position[0], -75)
        self.assertEqual(wire.y, 0)
        self.assertEqual(wire.position[1], 0)

    def test_minimal_intersect_distance(self):
        wire1 = Wire()
        commands_to_run = "R75,D30,R83,U83,L12,D49,R71,U7,L72"
        commands = get_list_of_command(commands_to_run)
        for command in commands:
            command.execute(wire1)

        wire2 = Wire()
        commands_to_run = "U62,R66,U55,R34,D71,R55,D58,R83"
        commands = get_list_of_command(commands_to_run)
        for command in commands:
            command.execute(wire2)

        intersection_distance = get_lowest_intersection_distance(wire1, wire2)
        self.assertEqual(intersection_distance, 159)

        wire1 = Wire()
        commands_to_run = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
        commands = get_list_of_command(commands_to_run)
        for command in commands:
            command.execute(wire1)

        wire2 = Wire()
        commands_to_run = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
        commands = get_list_of_command(commands_to_run)
        for command in commands:
            command.execute(wire2)

        intersection_distance = get_lowest_intersection_distance(wire1, wire2)
        self.assertEqual(intersection_distance, 135)

    def test_lowest_steps(self):
        wire1 = self.describe_wire("R75,D30,R83,U83,L12,D49,R71,U7,L72")

        wire2 = self.describe_wire("U62,R66,U55,R34,D71,R55,D58,R83")

        lowest_steps = get_lowest_steps(wire1, wire2)
        self.assertEqual(lowest_steps, 610)

        wire1 = self.describe_wire("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51")

        wire2 = self.describe_wire("U98,R91,D20,R16,D67,R40,U7,R15,U6,R7")

        lowest_steps = get_lowest_steps(wire1, wire2)
        self.assertEqual(lowest_steps, 410)

    @staticmethod
    def describe_wire(commands_to_run):
        wire = Wire()

        commands = get_list_of_command(commands_to_run)
        for command in commands:
            command.execute(wire)
        return wire


if __name__ == '__main__':
    unittest.main()
