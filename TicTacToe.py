import numpy as np

# Tic Tac Toe, Three in a Row!
class TicTacToe:
    """Play a TicTacToe game!"""
    # GamePlay Menu Options upon Initialization 
    def __init__(self):
        """Display game menu options and pass game mode selection from player(s)."""
        print("--------------------------------------")
        print("Welcome to Tic Tac Toe! Four in a Row!\n")
        print("Please Select a GamePlay Option:\n")
        print("1\t\tPlayer VS Player")
        print("2\t\tPlayer VS Random AI")
        print("3\t\tPlayer VS Genius AI")
        print("--------------------------------------")
        # User Game Mode Selection
        selection = int(input("\nGamePlay Selection: "))
        self.game_mode(selection)

    def game_mode(self, selection):
        if selection > 0 and selection < 4:
            self.get_new_board()
        else:
            prompt("")            

    def new_board(self):
        gameboard = []
        for i in range(9):
            gameboard.append(i + 1)
        new_gameboard = np.reshape(gameboard, (3, 3))
        return new_gameboard

    def get_new_board(self):
        new_gameboard = self.new_board()
        print(new_gameboard)

    def evaluate(board):
        """Evaluate the current gameboard status."""
        # initialize player markers
        player, opponent = "X", "O"
        # check all rows for a victory 
        for row in range(3):
            if(board[row][0]) == board[row][1] and board[row][1] == board[row][2]:
                if (board[row][0] == player):
                    return 10
                elif (board[row][0] == opponent):
                    victory = f"Player {opponent} wins!"
                    return -10, victory
        # check all columns for a victory
        for column in range(3):
            if (board[0][column] == board[1][column] and board[1][column] == board[2][column]):
                if (board[0][column] == player):
                    return 10
                elif (board[0][column] == opponent):
                    victory = f"Player {opponent} wins!"
                    return -10, victory
        # check the two diagonals for a victory
        if (board[0][0] == board[1][1] and board[1][1] == board[2][2]):
            if (board[0][0] == player): # descending diagonal
                return 10
            elif (board[0][0] == opponent):
                victory = f"Player {opponent} wins!"
                return -10, victory
        if (board[0][2] == board[1][1] and board[1][1] == board[2][0]):
            if (board[0][2] == player): # ascending diagonal
                return 10
            elif(board[0][2] == opponent):
                victory = f"Player {opponent} wins!"
                return -10, victory
        # otherwise return 0
        return 0    

TicTacToe()