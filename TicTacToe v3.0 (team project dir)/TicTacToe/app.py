"""Tic Tac Toe CLI Application"""
from TicTacToe.game.menus import TicTacToeMenus, PlayerSelections

menu = TicTacToeMenus()
select = PlayerSelections()

def run():
    """Run the program."""
    while True:
        menu.display_welcome_screen()
        select.main_menu_options()