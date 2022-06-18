"""This module contains two classes: TicTacToeMenus and PlayerSelections(TicTacToeMenus). 

The parent class contains methods to create and display three game menus: 
(1) welcome screen/main menu
(2) gameboard options
(3) gameover screen

The child class prompts, acquires, and applies the chosen menu options via user input."""

from game import TicTacToe

class TicTacToeMenus:
    """Creates and displays menus with player options for a Tic Tac Toe game."""
    def __init__(self):
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
        """The display_game_over_screen() method prints the Game Over menu to the CLI."""
        print(self.create_game_over_screen())

    def create_board_options(self):
        """The create_board_options() method creates a menu with two board size options (3x3 and 5x5)."""
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
        """The display_board_options() method prints the Gameboard Options menu to the CLI."""
        print(self.create_board_options())

class PlayerSelections(TicTacToeMenus):
    """
    The PlayerSelections class is the child class to TicTacToeMenus. 
    PlayerSelections contains the following methods:

        - get_player_selection()    x. acquires and returns user input with error catching
        - get_board_option()        x. displays, acquires, and applies board options via user input
        - main_menu()               x. displays, acquires, and applies user input to setup and start the game
        - game_over()               x. displays after replay refusal, allows player to return to main menu or
                                           quit out of the application
    """
    def __init__(self):
        """    
        The PlayerSelections class initializes with all parent variables/methods and adds the following class variables:

            - self._size        x. default = 1 --> the classic 3x3 gameboard
            - self._mode        x. default = 1 --> PvP mode 
        """
        super().__init__()
        self._board_option = 1  # defaults to classic board
        self._mode = 1  # defaults to PvP mode  
    
    def set_board_option(self, board):
        if board == 1:
            print("\n\tYou have chosen to play on the classic, 3x3, gameboard!")
        if board == 2:
            print("\n\tYou have chosen to play on the big, 5x5, gameboard!")
        self.board_option = board
    
    def set_game_mode(self, mode):
        self.mode = mode

    def get_game_settings(self):
        return self.mode, self.board_option  

    def get_player_selection(self):
        """The get_player_selection() method captures player input, converts to integer, and returns selection.
           
           Error catching included for KeyboardInterrupt to allow users to quit the program with Ctrl + c and
           for ValueErrors to ensure user inputs can be converted to integers. 

           Returns the player selection.
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
        """
        The board_options() method allows players to choose one of two board sizes to play on: 

            [1] 3x3 
            [2] 5x5

        Always returns to main menu. Default board size is 3x3. 
        """
        # loop prompts, captures, returns, and displays any player selections
        while True: 
            self.display_board_options()  # displays board options menu
            option = self.get_player_selection()
            if option in [1, 2]:
                self.set_board_option(board = option)
                self.main_menu()
                break
            if option == 3:
                self.main_menu()
                break
            # catches invalid inputs and prompts player to try again
            else:  
                print("\n\tInvalid input. Please try again.") 

    def main_menu(self):
        """
        The main_menu method first displays the welcome screen/main menu for the Tic Tac Toe game. 
           
        The main menu has 5 options:
        (1) PvP, (2) Random AI, (3) MiniMax AI, (4) Gameboard Options, or (5) Quit
           
        For the player's selection is then prompted, acquired, and applied. 
        Options 1-3 immediately start their respective gameplay loops.            
        """

        # loop prompts, captures, and applies player selections
        while True:
            self.display_welcome_screen()  # displays the main menu
            selection = self.get_player_selection()
            if selection in [1, 2, 3]:
                self.set_game_mode(mode = selection)
                mode, board = self.get_game_settings()
                play = TicTacToe(mode, board)
                play.tic_tac_toe()
                break
            elif selection == 4:
                self.board_options()  # loads board options menu
                break
            elif selection == 5:
                print("\n\tGood bye!\n")
                exit()  # quits out of program 
            # else catches invalid inputs and prompts user to try again
            else:
                print("\n\tInvalid input. Please try again.")

    def game_over(self):
        """The game_over() method displays the end-of-game screen that allows players the option
        to either return to the main menu or quit out of the program all together."""
        while True:  # begins player selection loop
            self.display_game_over_screen()
            selection = self.get_player_selection()  # acquires player selection via input
            if(selection == 1):  # if 1,
                self.main_menu()  # returns to main menu
                break
            if(selection == 2):  # if 2, 
                print("\n\tGood bye!\n")  # prints "Good bye!"
                exit()  # and exits program entirely
            # else catches invalid inputs and prompts user to try again
            else:
                print("\n\tInvalid input. Please try again.")
