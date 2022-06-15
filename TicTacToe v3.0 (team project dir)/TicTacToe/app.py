"""Tic Tac Toe CLI Application"""
from menus import TicTacToeMenus as menu, PlayerSelections as select

def run():
    """Run the program."""
    while True:
        menu.display_welcome_screen()
        select.main_menu_options()
