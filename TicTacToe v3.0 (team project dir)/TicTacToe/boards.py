"""TODO: Module docstring...."""
import numpy as np

class TicTacToeBoard:

    def __init__(self):
        """Initialize an empty game board."""
        self.board = []  # empty gameboard
        self.default = list(range(1, 10))
        self.board_option = self.default

    def create_board(self):
        """Creates a gameboard based on board_option size (3x3 or 5x5)."""
        for i in np.arange(self.default):  # nine numbers, as strings, because we replace
            self.board.append(i)  # the empty board numbers with Xs and Os (datatype consistency)
        self.board = np.reshape(self.board, (3, 3))  # shaped into 3 rows x 3 columns
        return self.board       

    def display_board(self):
        """Display current gameboard."""
        print('\t-------------------------------')
        for row in self.board:
            print('\t|         |         |         |')
            print('\t|', end = '')
            for item in row:
                print(f'    {item}    |', end = '')
            print()
            print('\t|         |         |         |')
            print('\t-------------------------------')

    def reset_board(self):
        """Reset the gameboard."""
        self.board = [] # reset to an empty list

    def place_marker(self, row, col, player):
        """Places the player marker (X or O) in the designated square."""
        self.board[row][col] = player # use move coordinates to place marker in the chosen square

    def is_board_full(self):
        """Determines if gameboard is full (DRAW)."""
        for row in self.board: # for each row on the board,
            for square in row: # and for each square in said row,
                if square in self.values: # if the square value is in our list of empty squares
                    return False # return False
        return True # otherwise return True

    def is_winner(self, board, player):
        """Checks gameboard for winning patterns."""
        win = None
        # check rows for win
        for row in range(3):
            if board[row][0] == board[row][1] and board[row][1] == board[row][2]:
                if board[row][0] == player:
                    win = True
            if win:
                return win
        # check columns for win
        for col in range(3):
            if board[0][col] == board[1][col] and board[1][col] == board[2][col]:
                if board[0][col] == player:
                    win = True
            if win:
                return win
        # check descending diagonal for win
        if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            if board[0][0] == player:
                win = True
        if win:
            return win
        # check ascending diagonal for win
        if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
            if board[0][2] == player:
                win = True
        if win:
            return win
