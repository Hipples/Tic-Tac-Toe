"""
This module is designed to load menus for our tic tac toe application at startup and shutdown.
"""
from menus import PlayerSelections

def run():
    """The run() function loads the tic tac toe program's main menus."""
    load = PlayerSelections()

    while True:
        load.main_menu()  # startup options
        while True:
            load.game_over()  # shutdown options
