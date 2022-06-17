"""
This module is designed to load menus for our tic tac toe application at startup and shutdown.
"""
from menus import PlayerSelections as play

def run():
    """The run() function loads the tic tac toe program's main menus."""
    load = play()

    while True:
        load.main_menu()  # startup options
        print()
        
        print()
        while True:
            load.game_over()  # shutdown options
