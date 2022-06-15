"""This module contains our Tic Tac Toe game modes and gameboard settings."""

class Settings:
    """Properties for gameplay settings with default values."""
    def __init__(self, board = 1, gamemode = 1):
        self.board = board
        self.gamemode = gamemode

    def get_board(self):
        return self.board

    def set_board(self, value):
        self.board = value

    @property
    def gamemode(self):
        return self._gamemode

    @gamemode.setter
    def gamemode(self, value):
        self._gamemode = value
