"""Tic Tac Toe CLI Application"""
from menus import TicTacToeMenus, PlayerSelections

def run():

    load = TicTacToeMenus()
    select = PlayerSelections()

    """Run the program."""
    while True:
        load.display_welcome_screen()
        select.main_menu_options()
