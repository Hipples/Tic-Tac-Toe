"""This module contains two classes: TicTacToeMenus and PlayerSelections(TicTacToeMenus). 

The parent class contains methods to create and display three game menus: 
(1) welcome screen/main menu
(2) gameboard options
(3) gameover screen

The child class prompts, acquires, and applies the chosen menu options via user input."""
# import game settings module
from TicTacToe.data.settings import GameModes, GameBoards
select_mode = GameModes()
select_board = GameBoards()

class TicTacToeMenus:
    """Creates and displays menus with player options for a Tic Tac Toe game."""
    def __init__(self):
        pass

    def create_welcome_screen(self):
        """Creates the welcome screen to be displayed upon startup. Main menu."""
        startup =  "\t __________________________________________________ \n"
        startup += "\t|                                                  |\n"
        startup += "\t|            TIC TAC TOE - Xs AND Os               |\n"
        startup += "\t|                                                  |\n"
        startup += "\t|--------------------------------------------------|\n"
        startup += "\t|                                                  |\n"
        startup += "\t|  Welcome Player(s)!                              |\n"
        startup += "\t|                                                  |\n"        
        startup += "\t|  To continue, enter an option below:             |\n"
        startup += "\t|--------------------------------------------------|\n" 
        startup += "\t|                                                  |\n"
        startup += "\t|  [1]: Player vs Player                           |\n"
        startup += "\t|                                                  |\n"
        startup += "\t|  [2]: Player vs Computer (random AI)             |\n"
        startup += "\t|                                                  |\n"
        startup += "\t|  [3]: Player vs Computer (minimax AI)            |\n"
        startup += "\t|                                                  |\n"       
        startup += "\t|  [4]: Gameboard Options                          |\n"
        startup += "\t|                                                  |\n"     
        startup += "\t|  [5]: Quit                                       |\n"
        startup += "\t|__________________________________________________|\n"
        return(startup)

    def display_welcome_screen(self):
        """Prints welcome screen to CLI."""
        print(self.create_welcome_screen())

    def create_game_over_screen(self):
        """Creates a game over screen to be displayed when players choose not to replay their current game."""
        game_over =  "\t __________________________________________________ \n"
        game_over += "\t|                                                  |\n"
        game_over += "\t|                    GAME OVER!                    |\n"
        game_over += "\t|                                                  |\n"
        game_over += "\t|--------------------------------------------------|\n"
        game_over += "\t|                                                  |\n"
        game_over += "\t|  GGs! Would you like to play another mode?       |\n"
        game_over += "\t|                                                  |\n"        
        game_over += "\t|  Enter an option from the menu below:            |\n"
        game_over += "\t|--------------------------------------------------|\n" 
        game_over += "\t|                                                  |\n"
        game_over += "\t|  [1]: Main Menu                                  |\n"
        game_over += "\t|                                                  |\n"
        game_over += "\t|  [2]: Quit                                       |\n"         
        game_over += "\t|__________________________________________________|\n"
        return(game_over)

    def display_game_over_screen(self):
        """Prints game over screen to CLI."""
        print(self.create_game_over_screen())

    def create_gameboard_options(self):
        """Creates a menu for players to choose the size of their gameboard (3x3 or 5x5)."""
        board_options =  "\t __________________________________________________ \n"
        board_options += "\t|                                                  |\n"
        board_options += "\t|                GAMEBOARD OPTIONS                 |\n"
        board_options += "\t|                                                  |\n"
        board_options += "\t|--------------------------------------------------|\n"
        board_options += "\t|                                                  |\n"
        board_options += "\t|  Choose the size of your gameboard!              |\n"
        board_options += "\t|                                                  |\n"        
        board_options += "\t|  Enter an option from the menu below:            |\n"
        board_options += "\t|--------------------------------------------------|\n" 
        board_options += "\t|                                                  |\n"
        board_options += "\t|  [1]: 3x3 (default)                              |\n"
        board_options += "\t|                                                  |\n"
        board_options += "\t|  [2]: 5x5                                        |\n"     
        board_options += "\t|                                                  |\n"    
        board_options += "\t|  [3]: Main Menu                                  |\n"         
        board_options += "\t|__________________________________________________|\n"
        return(board_options)

    def display_gameboard_options(self):
        """Prints gameboard options menu to CLI."""
        print(self.create_gameboard_options())

class PlayerSelections(TicTacToeMenus):
    """Captures and applies player selections from game menu options."""
    def __init__(self):
        pass

    def get_player_selection(self):
        """Captures player input, converts to integer, and returns selection."""
        while True:
            try:
                selection = int(input("\n\tPlayer Selection: "))
            except ValueError:  # catches inputs that cannot convert to int
                print("\n\tInvalid input. Please enter the number of your selection.")
            except KeyboardInterrupt:  # ensures ctrl + c allows players to quit the program
                print("\n\tGood bye!\n")
                exit()
            else:
                print()
                return selection

    def gameboard_options(self):
        """Allows selection of gameboard options."""
        self.display_gameboard_options()
        while True:  # loop prompts, captures, applies, and displays player selections
            option = self.get_player_selection()
            if option == 1:
                print("\n\tYou have chosen to play on a 3x3 gameboard!")
                self.display_welcome_screen()  # returns to welcome screen
                return select_board.default
            if option == 2:
                # TODO: method not yet created for 5x5 gameboard [GAMEBOARD: FIVE_BY_FIVE]
                print("\n\tYou have chosen to play on a 5x5 gameboard!")
                self.display_welcome_screen()  # returns to welcome screen
                return select_board.five_by_five
            if option == 3:
                self.display_welcome_screen()  # returns to welcome screen
                break  # ends loop
            else:  # catches invalid inputs and prompts player to try again
                print("\n\tInvalid input. Please try again.")    

    def main_menu_options(self):
        """Allows selection of gameplay options from main menu."""
        while True:
            option = self.get_player_selection()
            board_option = select_board.default
            if option == 1:
                select_mode.game_mode_1(board_option)  # initiates game play loop for PvP mode
                break  # ends loop
            if option == 2:
                select_mode.game_mode_2(board_option)  # initiates game play loop for PvE random mode
                break  # ends loop
            if option == 3:
                self.display_welcome_screen()  # returns to welcome screen
                break  # ends loop
            else:  # catches invalid inputs and prompts player to try again
                print("\n\tInvalid input. Please try again.") 

