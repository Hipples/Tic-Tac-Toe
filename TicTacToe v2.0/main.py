"""Main module used to launch the Tic Tac Toe startup and gameover menus."""
import tic_tac_toe
import ttt_menus

# class objects
Xs_and_Os = tic_tac_toe.TicTacToe()
menus = ttt_menus.TTTMenus()

def startup():
    """Launches game menu, then acquires and applies player selection to start chosen game mode."""
    while True:  # displays welcome screen until a valid input has been captured
        menus.display_welcome_screen()
        game_mode = ' '
        try:
            game_mode = int(menus.get_player_selection())
        except ValueError:  # catches inputs that are not numbers
            print("\n\tInvalid input. Please enter 1, 2, or 3.\n")
        except KeyboardInterrupt: # ensures ctrl + c allows players to quit the program
            print("\n\tGood bye!\n")
            exit()
        else:
            if(game_mode == 1):  # PvP mode
                Xs_and_Os.game_mode_1()
                break
            if(game_mode == 2):  # Random AI mode
                Xs_and_Os.game_mode_2()
                break
            if(game_mode == 3):  # Quit
                print("\n\tGood bye!\n")
                exit()
            else:  # catches any other invalid inputs
                print("\n\tInvalid input. Please enter 1, 2, or 3.\n")    
        
def game_over():
    while True:
        menus.display_game_over_screen()
        try:
            selection = int(menus.get_player_selection())
        except ValueError:
            print("\n\tInvalid input. Please enter 1 or 2.\n")
        except KeyboardInterrupt:
            print("\n\n\tGood bye!\n")
            exit()
        else:
            if(selection == 1): 
                startup()
            if(selection == 2):
                print("\n\tGood bye!\n")
                exit()

# driver code
startup()
print()
game_over()