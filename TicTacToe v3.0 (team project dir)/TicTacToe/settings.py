"""This module contains our Tic Tac Toe game modes and gameboard settings."""
import numpy as np
from menus import PlayerSelections as P

class Settings:
    """Properties for gameplay settings with default values."""
    def __init__(self, board_size = 1):
        self.board_size = board_size

    def board_option(self):
        set = P()
        set.display_board_options()
        option = set.gameboard_options()
        if option == 1:
            return self.default_board
        if option == 2:
            return self.larger_board\

# this is a failing idea...