import numpy as np
import random

# Tic Tac Toe, Three in a Row!
class TicTacToe:
    """Play a TicTacToe game!"""
    # initialize the game with our board as an empty list 
    def __init__(self):
        self.board = []
    # method to create the gameboard
    def create_board(self):
        for i in range(9):
            self.board.append(i + 1)
        self.board = np.reshape(self.board, (3, 3))
    # method to display the gameboard
    def display_board(self):
        print('-------------------------------')
        for row in self.board:
            print('|         |         |         | ')
            print('|', end = '')
            for item in row:
                print(f'    {item}    |', end = '')
            print()
            print('|         |         |         |')
            print('-------------------------------')
    # method to enable the player to choose to be Xs or Os 
    def choose_player_marker(self):
        marker = ' '
        while (marker != 'X' and marker != 'O'):
            marker = input("Do you want to be Xs or Os? ").upper()
        if marker == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']
    # method to assign player markers in PvP mode
    def assign_PvP_markers(self):
        player_1, player_2 = self.choose_player_marker()
        return player_1, player_2
    # method to assign player markers in PvE modes
    def assign_PvE_markers(self):
        player_1, player_2 = self.choose_player_marker()
        player, computer = player_1, player_2
        return player, computer
    # method to randomly decide who goes first
    def coin_flip(self):
        player = self.player_1 

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