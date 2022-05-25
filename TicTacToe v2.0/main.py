import ttt_menus
import tic_tac_toe

# class objects
menus = ttt_menus.TTTMenus()
Xs_and_Os = tic_tac_toe.TicTacToe()

def startup():
    while True:
        menus.display_welcome_screen()
        game_mode = ' '
        try:
            game_mode = int(menus.get_player_selection())
        except ValueError:
            print("\n\tInvalid input. Please enter 1 2 or 3.\n")
        except KeyboardInterrupt:
            print("\n\tGood bye!\n")
        else:
            if(game_mode == 1): 
                Xs_and_Os.game_mode_1_PvP()
                break
            elif(game_mode == 2): 
                Xs_and_Os.game_mode_2_PvE()
                break
            elif(game_mode == 3):
                print("\n\tGood bye!\n")
                exit()
        return True
        
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