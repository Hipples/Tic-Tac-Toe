# code from tutorial at https://geekflare.com/tic-tac-toe-python-code/

import random

class TicTacToe:

    def __init__(self): 
        # "__init__" is a reseved method in python classes. It is known as a constructor in object oriented concepts. This method called when an object is created from the class and it allow the class to initialize the attributes of a class. 

        # source: https://micropyramid.com/blog/understand-self-and-__init__-method-in-python-class/
        self.board = []
        # initializes tic-tac-toe board as an empty list

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def get_random_first_player(self):
        return random.randint(0, 1) # used to select who goes first: X or O

    def pick_spot(self, row, col, player):
        self.board[row][col] = player # replaces the '-' with either X or O

    def is_player_win(self, player):
        win = None
        n = len(self.board)
        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win
        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win
        # checking diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win




    
