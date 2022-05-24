import unittest
import numpy as np
from tic_tac_toe import TicTacToe
from io import StringIO
from unittest.mock import patch

# create a public TicTacToe class object to use in the method unit tests
Tic = TicTacToe()

# create a class for our tic_tac_toe module unit test cases
class TicTacToeTest(unittest.TestCase):
    """"Unit tests for our TicTacToe class."""

    # 01. test create_board()
    def test_create_board(self):
        """Test that the gameboard is properly created."""
        Tic.create_board() # call method we are testing
        values = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        test_board = np.reshape(values, (3, 3)) # construct our expected result
        # compare using np.testing due to type of ndarray
        np.testing.assert_array_equal(Tic.board, test_board)

    # 02. test display_board()
    def test_display_board(self):
        """Test that the gameboard is properly displayed."""
        with patch('sys.stdout', new=StringIO()) as output:
            Tic.display_board() # capture output of the method we are testing       
        # construct expected output
        values = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        test_board = np.reshape(values, (3, 3))
        test_display =   ('\t-------------------------------\n')
        test_display +=  ('\t|         |         |         |\n')
        test_display += (f'\t|    {test_board[0, 0]}    |    {test_board[0, 1]}    |    {test_board[0, 2]}    |\n')
        test_display +=  ('\t|         |         |         |\n')
        test_display +=  ('\t-------------------------------\n')
        test_display +=  ('\t|         |         |         |\n')
        test_display += (f'\t|    {test_board[1, 0]}    |    {test_board[1, 1]}    |    {test_board[1, 2]}    |\n')
        test_display +=  ('\t|         |         |         |\n')
        test_display +=  ('\t-------------------------------\n')
        test_display +=  ('\t|         |         |         |\n')
        test_display += (f'\t|    {test_board[2, 0]}    |    {test_board[2, 1]}    |    {test_board[2, 2]}    |\n')
        test_display +=  ('\t|         |         |         |\n')
        test_display +=  ('\t-------------------------------\n')
        # compare the value of our method's output and our expected output
        self.assertEqual(output.getvalue(), test_display)

    # 03. test reset_board()
    def test_reset_board(self):
        """Test that the gameboard is reset to an empty list"""
        Tic.reset_board() # call method we are testing
        test_board = [] # construct expected result
        # compare by calling in the class variable that was reset using Tic
        self.assertEqual(Tic.board, test_board)


    @unittest.mock.patch('tic_tac_toe.input', create = True)
    # 04. test choose_marker()
    def test_choose_marker(self, mocked_input):
        """Test that user input is properly reflected in the list order of the returned characters."""
        mocked_input.side_effect = ['x'] # create a mock input for 'x'
        result = Tic.choose_marker() # capture results of the method we are testing
        self.assertEqual(result, ['X', 'O']) # compare with expected results based on mock input

        mocked_input.side_effect = ['o'] # create a mock input for 'o'
        result = Tic.choose_marker() # capture results of the method we are testing
        self.assertEqual(result, ['O', 'X']) # compare with expected results based on mock input






# run the tests
if __name__ == '__main__':
    unittest.main() 