"""Module contains different AI player logics."""
import random

class AILogic:
    def __init__(self) -> None:
        pass
        
    # needs updating with new structure    
    def random_AI_move(self):
        """Returns a random, available, square number for the easy AI's desired move."""
        possible_moves = [] # declare an empty list of possible moves
        for row in self.board: # for each row in our gameboard,
            for square in row: # and for each square in said row,
                if square in self.values: # if the square's value is in our values list
                    possible_moves.append(square) # store it in our list of available squares
        move = random.choice(possible_moves) # determine a random, available move for AI
        return move # from our list of possible moves