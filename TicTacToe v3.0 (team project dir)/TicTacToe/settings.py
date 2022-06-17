"""module docstring"""

class Settings:
    """class docstring"""
    def __init__(self, board, mode):
        self.board = board
        self.mode = mode

    def _get_board(self):
        print(f"get board size: {self._board}")
        return self._board

    def _set_board(self, option):
        try:
            option in [1, 2]
        except:
            print("\n\tError with _board setter.")
        else:
            self._board = option
            print(f"set board size: {self._board}")

    board = property(fget=_get_board, fset=_set_board, doc="The board size setting.")

    def _get_mode(self):
        print(f"get game mode: {self._mode}")
        return self._mode
    
    def _set_mode(self, option):
        try: 
            option in [1, 2, 3]
        except:
            print("\n\tError with _mode setter.")
        else:
            self._mode = option
            print(f"set game mode: {self._mode}")

    mode = property(fget=_get_mode, fset=_set_mode, doc="The game mode setting.")