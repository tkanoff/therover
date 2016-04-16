import unittest

import sys
sys.path.append("..")

from rover import Rover
from plateau import Plateau


class TestRoverLogic(unittest.TestCase):
    def test_move_logic_starting_S(self):
        # Prepare test
        rover = Rover()
        plateau = Plateau(10, 10)

        rover.set_position("2 3 S")
        rover.set_directions("MMLLMRMLRM")

        rover.set_plateau(plateau)
        rover.split_coordinates()

        # Run code
        rover.move()

        # Check results
        self.assertEqual(rover.position_x, 4)
        self.assertEqual(rover.position_y, 2)
        self.assertEqual(rover.position_facing, 'E')

    def test_move_logic_starting_E(self):
        # Prepare test
        rover = Rover()
        plateau = Plateau(10, 10)

        rover.set_position("4 4 E")
        rover.set_directions("MMLLMRMLRM")

        rover.set_plateau(plateau)
        rover.split_coordinates()

        # Run code
        rover.move()

        # Check results
        self.assertEqual(rover.position_x, 5)
        self.assertEqual(rover.position_y, 6)
        self.assertEqual(rover.position_facing, 'N')

    def test_move_logic_starting_N(self):
        # Prepare test
        rover = Rover()
        plateau = Plateau(10, 10)

        rover.set_position("4 4 N")
        rover.set_directions("MMLLMRMLRM")

        rover.set_plateau(plateau)
        rover.split_coordinates()

        # Run code
        rover.move()

        # Check results
        self.assertEqual(rover.position_x, 2)
        self.assertEqual(rover.position_y, 5)
        self.assertEqual(rover.position_facing, 'W')


if __name__ == '__main__':
    unittest.main()
