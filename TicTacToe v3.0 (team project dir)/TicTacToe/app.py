"""
The app module is designed to load menus and settings for our tic tac toe program at startup
and shutdown.
"""
from menus_and_settings import PlayerSelections


def run():
    """Loads the tic tac toe program's main menus."""
    load = PlayerSelections()

    while True:
        load.main_menu()  # startup options
        while True:
            load.game_over()  # shutdown options

# pylint results 10/10
# no pylama results
# - June 19, 2022
