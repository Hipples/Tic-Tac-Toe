class TTTStartup:
    def __init__(self):
        pass

    def create_welcome_screen(self):
        startup =  "\t __________________________________________________\n"
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
        startup += "\t|  [2]: Playver vs Computer (random AI)            |\n"
        startup += "\t|__________________________________________________|\n"
        return(startup)

    def display_welcome_screen(self):
        welcome_screen = self.create_welcome_screen()
        print(welcome_screen)

    def get_player_selection(self):
        selection = input("\t\nPlayer Selection: ")
        return(selection)