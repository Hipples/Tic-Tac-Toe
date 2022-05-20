import numpy as np
import random

# Tic Tac Toe, Three in a Row!
class TicTacToe:
    """Play a TicTacToe game!"""
    def __init__(self):
        # Initialize game with the board as an empty list 
        self.board = []


    
    def create_board(self):
        for i in range(9):
            self.board.append(i + 1)
        self.board = np.reshape(self.board, (3, 3))

    def display_board(self):
        print('_________________________')
        for row in self.board:
            print('|       |       |       | ')
            print('|', end = '')
            for item in row:
                print(f'   {item}   |', end = '')
            print()
            print('|       |       |       |')
            print('_________________________')

        










    def coin_flip(self):
        # initialize player markers
        player, opponent = "X", "O"
        # flip the coin
        result = random.randint(0, 1)
        if result == 0:
            return player
        elif result == 1: 
            return opponent # assign first player

    def evaluate(board):
        """Evaluate the current gameboard status."""
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

TicTacToe()