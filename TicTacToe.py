import numpy as np
import random

# Tic Tac Toe, Three in a Row!
class TicTacToe:
    """Play a TicTacToe game!"""
    # initialize the game with our board as an empty list and two unknown players
    def __init__(self):
        self.board = []
        self.player = ''
        self.opponent = ''

    # method to create the gameboard
    def create_board(self):
        for i in range(9):
            self.board.append(i + 1)
        self.board = np.reshape(self.board, (3, 3))
    # method to display the gameboard
    def display_board(self):
        print('-------------------------------')
        for row in self.board:
            print('|         |         |         | ')
            print('|', end = '')
            for item in row:
                print(f'    {item}    |', end = '')
            print()
            print('|         |         |         |')
            print('-------------------------------')

    # method to enable the player to choose to be Xs or Os 
    def choose_marker(self):
        marker = ' '
        while (marker != 'X' and marker != 'O'):
            marker = input("Do you want to be Xs or Os? ").upper()
        if marker == 'X':
            return ['X', 'O']
        else:
            return ['O', 'X']
    # method to assign player markers
    def assign_markers(self):
        self.player, self.opponent = self.choose_marker()
        return self.player, self.opponent
    # method to randomly decide who goes first
    def coin_flip(self):
        return random.randint(0, 1)


    def game_mode(self, selection):
        """Enable player selection between three game modes (PvP, PvRandom, PvGenius)"""
        while selection != 1 and selection !=2 and selection !=3:
            selection = int(input("Please enter 1, 2, or 3 to select your : "))
            match selection:
                case 1: 
                    print("Game Mode: Player vs Player!")
                    break
                case 2:
                    print("Game Mode: Player vs Random AI!")
                    break
                case 3:
                    print("Game Mode: Player vs Genius AI!")
                    break


    def evaluate(self, board):
        """Evaluate the current gameboard status."""
        # check all rows for a victory 
        for row in range(3):
            if(board[row][0]) == board[row][1] and board[row][1] == board[row][2]:
                if (board[row][0] == self.player):
                    return 10
                elif (board[row][0] == self.opponent):
                    victory = f"Player {self.opponent} wins!"
                    return -10, victory
        # check all columns for a victory
        for column in range(3):
            if (board[0][column] == board[1][column] and board[1][column] == board[2][column]):
                if (board[0][column] == self.player):
                    return 10
                elif (board[0][column] == self.opponent):
                    victory = f"Player {self.opponent} wins!"
                    return -10, victory
        # check the two diagonals for a victory
        if (board[0][0] == board[1][1] and board[1][1] == board[2][2]):
            if (board[0][0] == self.player): # descending diagonal
                return 10
            elif (board[0][0] == self.opponent):
                victory = f"Player {self.opponent} wins!"
                return -10, victory
        if (board[0][2] == board[1][1] and board[1][1] == board[2][0]):
            if (board[0][2] == self.player): # ascending diagonal
                return 10
            elif(board[0][2] == self.opponent):
                victory = f"Player {self.opponent} wins!"
                return -10, victory
        # otherwise return 0
        return 0    


    def play_game_1(self):
        """Main gameplay loop."""
        self.create_board()             # create the gameboard
        self.choose_marker()            # choose player marker
        # assign player markers based on choice
        player, opponent = self.assign_markers()      
        # randomly decide which player goes first
        if self.coin_flip() == 1:
            current_player = player
        else:
            current_player = opponent
        
        while True:

