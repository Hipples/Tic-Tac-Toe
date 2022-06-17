"""module docstring"""
from menus import PlayerSelections as set

class Settings:
    """class docstring"""
    def __init__(self, board, mode) -> None:
        self.board = board
        self.mode = mode

    def _get_board(self):
        print("get board size")
        return self._board

    def _set_board(self, option):
        try:
            option in [1, 2]
        except:
            print("\n\tError with board_size setter.")
        else:
            self._board = option
            print("set board size")

    board = property(fget=_get_board, fset=_set_board, doc="The board size setting.")

    def _get_mode(self):
        return self._mode
    
    def _set_mode(self, option):
        try: 
            option in [1, 2, 3]
        except:
            print("\n\tError with game_mode setter.")
        else:
            self._mode = option

    mode = property(fget=_get_mode, fset=_set_mode, doc="The game mode setting.")