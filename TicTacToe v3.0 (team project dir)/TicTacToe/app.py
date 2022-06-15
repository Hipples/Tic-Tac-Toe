"""Tic Tac Toe CLI Application"""
from yaml import load_all
from menus import TicTacToeMenus
from menus import PlayerSelections

def run():

    load = TicTacToeMenus()
    select = PlayerSelections()

    """Run the program."""
    while True:
        load.display_welcome_screen()
        select.main_menu_options()
