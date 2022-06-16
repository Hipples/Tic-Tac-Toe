"""Tic Tac Toe CLI Application"""
from menus import PlayerSelections

def run():
    """Run the program."""
    load = PlayerSelections()
    while True:
        load.main_menu()
        print()
        while True:
            load.game_over()
