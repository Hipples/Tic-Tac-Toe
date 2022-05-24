import unittest
import numpy as np
from tic_tac_toe import TicTacToe

class TicTacToeTest(unittest.TestCase):
    """"Unit tests for the class TicTacToe"""

    def test_create_board(self):
        """Test that the gameboard is properly created."""
        Tic = TicTacToe()
        board = Tic.create_board()
        values = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        test_board = np.reshape(values, (3, 3))

        message = "Newly created gameboard and list of empty squares, do not match."
        np.testing.assert_array_equal(board, test_board, message)

if __name__ == '__main__':
    unittest.main() 