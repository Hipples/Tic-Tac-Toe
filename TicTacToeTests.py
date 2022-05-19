import numpy as np
import TicTacToe as T

class TicTacToeTests:
    def __init__(self):
        pass

    def test_get_new_board(self):
        new_board = T.get_new_board()
        return new_board

    def evaluate(board):
        """Evaluate the current gameboard status."""
        # initialize player markers
        player, opponent = "X", "O"
        # check all rows for a victory 
        for row in range(3):
            if(board[row][0]) == board[row][1] and board[row][1] == board[row][2]:
                if (board[row][0] == player):
                    return 10
                elif (board[row][0] == opponent):
                    victory = f"Player {opponent} wins!"
                    return -10, victory
        # check all columns for a victory
        for column in range(3):
            if (board[0][column] == board[1][column] and board[1][column] == board[2][column]):
                if (board[0][column] == player):
                    return 10
                elif (board[0][column] == opponent):
                    victory = f"Player {opponent} wins!"
                    return -10, victory
        # check the two diagonals for a victory
        if (board[0][0] == board[1][1] and board[1][1] == board[2][2]):
            if (board[0][0] == player): # descending diagonal
                return 10
            elif (board[0][0] == opponent):
                victory = f"Player {opponent} wins!"
                return -10, victory
        if (board[0][2] == board[1][1] and board[1][1] == board[2][0]):
            if (board[0][2] == player): # ascending diagonal
                return 10
            elif(board[0][2] == opponent):
                victory = f"Player {opponent} wins!"
                return -10, victory
        # otherwise return 0
        return 0 

    test_get_new_board()