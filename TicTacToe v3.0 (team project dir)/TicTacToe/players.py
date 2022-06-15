"""Module contains classes for different gameplay logic for both human and AI players."""
import random
from time import sleep
import numpy as np


class Players:
    """Class contains methods that: allow players to choose their game markers ('X' or 'O'), acquires input from players on their turn, applies the player input to complete thier move, """
    def __init__(self):
        self.match_records = "tic.tac.toe.txt"

    def choose_marker(self):
        """Allows main player to choose to be X or O"""
        marker = ' ' # declare marker variable as empty string
        while marker not in ('X', 'O'): # while marker does not equal X or O
            marker = input("\n\tDo you want to be Xs or Os? ").upper() # ask player to choose X or O
        if marker == 'X': # if X,
            return ['X', 'O'] # then return X, O
        return ['O', 'X'] # if O, then return O, X

    def assign_markers(self):  # retrieve marker order from choose_marker() method
        """Assigns gameboard markers (X and O) to the appropriate player."""
        player, opponent = self.choose_marker()  # assign the first char returned to our player,
        return player, opponent  # and the second char to our player's opponent
    
    def player_turn(self, player):  # should rename to something like player_input
        """Acquires player input to determine desired move (1-9)."""
        move = input(f"\n\tPlease enter the square number where you'd like to place your {player}: ")
        print(f"\n\tYou chose square {move}!") # acquire player input to determine desired move
        return move # return chosen square number

class AI(Players):
    def __init__(self) -> None:
        pass
          
    def random_turn(self):
        """Returns a random, available, square number for the easy AI's desired move."""
        possible_moves = [] # declare an empty list of possible moves
        for row in self.board.board: # for each row in our gameboard,
            for square in row: # and for each square in said row,
                if square in self.board.default: # if the square's value is in our values list
                    possible_moves.append(square) # store it in our list of available squares
        move = random.choice(possible_moves) # determine a random, available move for AI
        return move # from our list of possible moves

    def random_move(self, player):
        """Capture, record, and fullfil random AI movement during computer player turns."""
        move = self.random_turn() # get randomly generate move from random_moves() method
        coords = np.where(self.board.board == move) # set the move coordinates
        row, col = (int(coords[0])), (int(coords[1])) # assign the proper index of the move
        sleep(2) # (our AI is thinking. . .)
        print(f"\n\tRandAI chooses square {move}!\n") # announce RandAI's move
        with open(self.match_records, 'a') as record: # open our match records and
            record.write(f"{player}:{move} ") # append each Random AI move
        self.board.place_marker(row, col, player) # as it happens

    def minimax_turn(self):
        pass

    def minmax_move(self):
        pass
