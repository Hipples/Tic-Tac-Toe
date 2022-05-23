class TTTMenus:
    def __init__(self):
        pass 

    def create_welcome_screen(self):
        startup =  "\t __________________________________________________ \n"
        startup += "\t|                                                  |\n"
        startup += "\t|     Tic Tac Toe, Xs and Os, Three in a Row!!     |\n"
        startup += "\t|                                                  |\n"
        startup += "\t|--------------------------------------------------|\n"
        startup += "\t|                                                  |\n"
        startup += "\t|  Welcome Player(s)!                              |\n"
        startup += "\t|                                                  |\n"        
        startup += "\t|  To play, select an option below:                |\n"
        startup += "\t|--------------------------------------------------|\n" 
        startup += "\t|                                                  |\n"
        startup += "\t|  [1]: Player vs Player                           |\n"
        startup += "\t|                                                  |\n"
        startup += "\t|  [2]: Player vs Computer (random AI)             |\n"
        startup += "\t|                                                  |\n"
        startup += "\t|  [3]: Quit                                       |\n"
        startup += "\t|__________________________________________________|\n"
        return(startup)

    def display_welcome_screen(self):
        print(self.create_welcome_screen())

    def get_player_selection(self):
        selection = input("\n\tPlayer Selection: ")
        print()
        return(selection)

    def create_game_over_screen(self):
        game_over =  "\t __________________________________________________ \n"
        game_over += "\t|                                                  |\n"
        game_over += "\t|                    GAME OVER!                    |\n"
        game_over += "\t|                                                  |\n"
        game_over += "\t|--------------------------------------------------|\n"
        game_over += "\t|                                                  |\n"
        game_over += "\t|  GGs! Would you like to play another mode?       |\n"
        game_over += "\t|                                                  |\n"        
        game_over += "\t|  Select an option from the menu below:           |\n"
        game_over += "\t|--------------------------------------------------|\n" 
        game_over += "\t|                                                  |\n"
        game_over += "\t|  [1]: Main Menu                                  |\n"
        game_over += "\t|                                                  |\n"
        game_over += "\t|  [2]: Quit                                       |\n"         
        game_over += "\t|__________________________________________________|\n"
        return(game_over)

    def display_game_over_screen(self):
        print(self.create_game_over_screen())