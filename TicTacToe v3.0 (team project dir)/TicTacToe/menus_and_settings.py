"""This module contains two classes: TicTacToeMenus and PlayerSelections(TicTacToeMenus). 

The parent class contains methods to create and display three game menus: 
    (1) welcome screen/main menu
    (2) gameboard options
    (3) gameover screen

The child class prompts user input related to the menu options, captures specified game settings, and starts the chosen game mode!
"""
from game import TicTacToe  # used to apply settings and start game from main menu

class TicTacToeMenus:
    """
    TicTacToeMenus contains the following class methods:

        - create_welcome_screen()
        - display_welcome_screen()
        - create_game_over_screen()
        - display_game_over_screen()
        - create_board_options()
        - display_board_options()
    """
    def __init__(self):  # no class variables required
        pass

    def create_welcome_screen(self):
        """Creates the welcome screen to be displayed upon startup. Main menu."""
        main_menu =  "\t __________________________________________________ \n"
        main_menu += "\t|                                                  |\n"
        main_menu += "\t|            TIC TAC TOE - Xs AND Os               |\n"
        main_menu += "\t|                                                  |\n"
        main_menu += "\t|--------------------------------------------------|\n"
        main_menu += "\t|                                                  |\n"
        main_menu += "\t|  Welcome Player(s)!                              |\n"
        main_menu += "\t|                                                  |\n"        
        main_menu += "\t|  To continue, enter an option below:             |\n"
        main_menu += "\t|--------------------------------------------------|\n" 
        main_menu += "\t|                                                  |\n"
        main_menu += "\t|  [1]: Player vs Player                           |\n"
        main_menu += "\t|                                                  |\n"
        main_menu += "\t|  [2]: Player vs Computer (random AI)             |\n"
        main_menu += "\t|                                                  |\n"
        main_menu += "\t|  [3]: Player vs Computer (minimax AI)            |\n"
        main_menu += "\t|                                                  |\n"       
        main_menu += "\t|  [4]: Gameboard Options                          |\n"
        main_menu += "\t|                                                  |\n"     
        main_menu += "\t|  [5]: Quit                                       |\n"
        main_menu += "\t|__________________________________________________|\n"
        return(main_menu)

    def display_welcome_screen(self):
        """Prints the welcome screen to CLI."""
        print(self.create_welcome_screen())

    def create_game_over_screen(self):
        """Creates the game over screen to be displayed when players choose not to replay."""
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
        """Prints the game over screen to the CLI."""
        print(self.create_game_over_screen())

    def create_board_options(self):
        """Creates a menu with two board size options (3x3 and 5x5)."""
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

    def display_board_options(self):
        """Prints the board options menu to the CLI."""
        print(self.create_board_options())

class PlayerSelections(TicTacToeMenus):
    """
    PlayerSelections contains the following class methods:
        - set_board_options(board)
        - set_game_mode(mode)
        - get_game_settings()
        - get_player_selection()   
        - get_board_option()       
        - main_menu()               
        - game_over()               
    """
    def __init__(self):
        """    
        PlayerSelections initializes with all parent methods and adds the following class variables:

            - self._board_option
            - self._mode      

        These are used to apply the game settings.   
        """
        super().__init__()
        self.board_option = 1  # defaults to classic board
        self.mode = 1  # defaults to PvP mode  
    
    def set_board_option(self, board):
        """Applies player selection from board options menu to game settings."""
        if board == 1:
            print("\n\tYou have chosen to play on the classic, 3x3, gameboard!")
        if board == 2:
            print("\n\tYou have chosen to play on the big, 5x5, gameboard!")
        self.board_option = board
    
    def set_game_mode(self, mode):
        """Applies player selection (1-3) from main menu to game settings."""
        self.mode = mode

    def get_game_settings(self):
        """Returns all game settings."""
        return self.mode, self.board_option  

    def get_player_selection(self):
        """
        Returns players selections as integers. Catches and reprompts input errors. Accepts Ctrl + c as shortcut to quit out of program during user input.
        """
        while True:
            try:
                selection = int(input("\n\tPlayer Selection: "))
            except ValueError:  # catches inputs that cannot convert to int
                print()
                print("\n\tInvalid input. Please enter the number of your selection.")
            except KeyboardInterrupt:  # ensures ctrl + c allows players to quit the program
                print()
                print("\n\tGood bye!\n")  # with a Good bye! message
                exit()
            else:
                print()
                return selection  # returns player selection

    def board_options(self):
        """Allows user to choose the board size for their game (3x3 or 5x5). Returns to main menu."""
        # loop prompts, captures, returns, and displays any player selections
        while True: 
            self.display_board_options()  # displays board options menu
            option = self.get_player_selection()
            if option in [1, 2]:
                self.set_board_option(board = option)  # saves board_option to game settings
                self.main_menu()
                break
            if option == 3:
                self.main_menu()
                break
            # catches invalid inputs and prompts player to try again
            else:  
                print("\n\tInvalid input. Please enter the number of your selection.") 

    def main_menu(self):
        """
        The main menu has 5 options:
        (1) PvP, (2) Random AI, (3) MiniMax AI, (4) Gameboard Options, or (5) Quit
           
        Options 1-3 immediately start their respective gameplay loops.            
        """
        # loop prompts, captures, and applies player selections
        while True:
            self.display_welcome_screen()  # displays the main menu
            selection = self.get_player_selection()
            if selection in [1, 2, 3]:
                self.set_game_mode(mode = selection)  # saves mode to game settings
                mode, board = self.get_game_settings()  # acuires most recent game settings
                play = TicTacToe(mode, board)  # initiates TicTacToe object
                play.tic_tac_toe()  # starts game
                break
            elif selection == 4:
                self.board_options()  # loads board options menu
                break
            elif selection == 5:
                print("\n\tGood bye!\n")
                exit()  # quits out of program 
            # catches invalid inputs and prompts user to try again
            else:
                print("\n\tInvalid input. Please enter the number of your selection.")

    def game_over(self):
        """The game over screen allows players the option to return to the main menu or quit."""
        while True:  # begins player selection loop
            self.display_game_over_screen()
            selection = self.get_player_selection()  # acquires player selection via input
            if(selection == 1):  # if 1,
                self.main_menu()  # returns to main menu
                break
            if(selection == 2):  # if 2,
                print("\n\tGood bye!\n")  # prints "Good bye!"
                exit()  # and exits program entirely
            # catches invalid inputs and prompts user to try again
            else:
                print("\n\tInvalid input. Please try again.")
