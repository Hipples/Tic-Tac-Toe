import unittest
import numpy as np
from tic_tac_toe import TicTacToe
from io import StringIO
from unittest.mock import patch
import pytest

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

    @unittest.mock.patch('tic_tac_toe.input', create = True)
    # 05. test assign_marker() 
    def test_assign_marker_x(self, mocked_input):
        """Test that the game markers are properly assigned to player and opponent."""
        mocked_input.side_effect = ['x'] # create a mock input of 'x'
        resulting_player, resulting_opponent = Tic.assign_markers() # capture return values
        results = [resulting_player, resulting_opponent] # save results into single variable
        self.assertEqual(results, ['X', 'O']) # compare with expected results

        mocked_input.side_effect = ['O'] # create a mock input of 'o'
        resulting_player, resulting_opponent = Tic.assign_markers() # caputre return values
        results = [resulting_player, resulting_opponent] # save results into a single variables
        self.assertEqual(results, ['O', 'X']) # compare with expected results

    # 06. test coin_flip() 
    def test_coin_flip(self):
        "Test that either 1 or 0 is returned as a result of our coin flip."
        heads_or_tails = Tic.coin_flip() # capture results
        potential_results = [0, 1] # construct expected results list
        self.assertIn(heads_or_tails, potential_results) # captured results is in expected results list

    @unittest.mock.patch('tic_tac_toe.input', create = True)
    # 07. test human_moves()
    def test_human_moves(self, mocked_input):
        """Test that input equals returned value and is printed to console."""
        with patch('sys.stdout', new=StringIO()) as output:
            mocked_input.side_effect = ['5'] # create mock input of 5
            player = 'X' # initilize method parameter
            result = Tic.human_moves(player) # captures printed output and returned value
        test_output = f"You chose square {result}!" # construct expected output
        self.assertEqual(result, '5') # tests returned value
        self.assertEqual(output.getvalue().strip(), test_output) # tests printed output

    @unittest.mock.patch('tic_tac_toe.input', create = True)
    # 08. test get_coords()
    def test_get_coords(self, mocked_input):
        """Tests that input is converted to proper board coordinates and captures console output."""
        with patch('sys.stdout', new=StringIO()) as output:
            mocked_input.side_effect = ['5'] # create mock input of 5
            player = 'X' # initilize method parameter
            results = Tic.get_coords(player) # captures printed output and returned values
        test_output = "You chose square 5!" # construct expected output
        np.testing.assert_equal(results, [1, 1]) # tests returned values
        self.assertEqual(output.getvalue().strip(), test_output) # tests printed output

    # 09. test place_marker()
    def test_place_marker(self):
        """Test that the value of player become the value of the indexed board location."""
        player = 'X'
        row, col = 1, 1
        Tic.place_marker(row, col, player)
        np.testing.assert_equal(Tic.board[1][1], 'X')

    #10. test random_moves()
    def test_random_moves(self):
        """Test that the returned values is one of the gameboard's square numbers."""
        result = Tic.random_moves() 
        self.assertIn(result, ['1', '2', '3', '4', '5', '6', '7', '8', '9'])

# run the tests
if __name__ == '__main__':
    unittest.main() 