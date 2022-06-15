"""This module contains our Tic Tac Toe game modes and gameboard settings."""

class Settings:
    """Properties for gameplay settings with default values."""
    def __init__(self):
        self._board = list(range(1, 10))
        self._gamemode = 1

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, option):
        self._board = option

    @property
    def gamemode(self):
        return self._gamemode

    @gamemode.setter
    def gamemode(self, option):
        self._gamemode = option
