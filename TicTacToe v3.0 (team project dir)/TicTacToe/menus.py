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

    def display_game_over_menu(self):
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
    """The PlayerSelections class contains the following methods:

            - get_player_selection()    x. acquires and returns user input with error catching
            - get_board_option()        x. displays, acquires, and applies board options via user input
            - main_menu()               x. displays, acquires, and applies user input to setup and start the game
            - game_over()               x. displays after replay refusal, allows player to return to main menu or quit

       The PlayerSelections class contains on class variables:

            - self.board_option         x. default = 1 --> the classic 3x3 gameboard
    """
    def __init__(self):
        super().__init__()
        self.board_option = 1

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

    def main_menu(self):
        """The main_menu method first displays the welcome screen/main menu for the Tic Tac Toe game. 
           
           The main menu has 5 options:
               (1) PvP, (2) Random AI, (3) MiniMax AI, (4) Gameboard Options, or (5) Quit
           
           For the player's selection is then prompted, acquired, and applied. 
           Options 1-3 immediately start their respective gameplay loops.            
        """
        # creates a TicTacToe class object to load chosen game modes
        play = TicTacToe()
        # loop prompts, captures, and applies player selections
        while True:
            self.display_welcome_screen()  # displays the main menu
            selection = self.get_player_selection()
            if selection == 1:
                play.game_mode_1()  # loads PvP mode
                break
            if selection == 2:
                play.game_mode_2()  # loads random AI mode
                break
            if selection == 3:
                play.game_mode_3()
                break  # loads minimax AI mode
            if selection == 4:
                self.get_board_option()  # loads board options menu
            if selection == 5:
                print("\n\tGood bye!\n")
                exit()  # quits out of program 
            # else catches invalid inputs and prompts user to try again
            else:
                print("\n\tInvalid input. Please try again.")

    def game_over(self):
        """The game_over() method displays the end-of-game screen that allows players the option
        to either return to the main menu or quit out of the program all together."""
        while True:  # begins player selection loop
            self.display_game_over_menu()
            selection = self.get_player_selection()  # acquires player selection via input
            if(selection == 1):  # if 1,
                self.main_menu()  # returns to main menu
                break  # and ends loop
            if(selection == 2):  # if 2, 
                print("\n\tGood bye!\n")  # prints "Good bye!"
                exit()  # and exits program entirely
            # else catches invalid inputs and prompts user to try again
            else:
                print("\n\tInvalid input. Please try again.")

    def get_board_option(self):
        """The get_board_options() method allows players to choose one of two board sizes to play on: 

               [1] 3x3 
               [2] 5x5

           Always returns to main menu. Default board size is 3x3. 
        """
        # loop prompts, captures, returns, and displays any player selections
        while True: 
            self.display_board_options()  # displays board options menu
            option = self.get_player_selection()
            if option == 1:
                print("\n\tYou have chosen to play on a 3x3 gameboard!")
                self.display_welcome_screen() 
                self.board_option = option
                return self.board_option  # returns self.board_option with a value of 1
            if option == 2:
                print("\n\tYou have chosen to play on a 5x5 gameboard!")
                self.display_welcome_screen()  
                self.board_option = option
                return self.board_option  # returns self.board_option with a value of 2
            if option == 3:
                self.display_welcome_screen()  
                return self.board_option  # returns self.board_option as is
            # catches invalid inputs and prompts player to try again
            else:  
                print("\n\tInvalid input. Please try again.") 