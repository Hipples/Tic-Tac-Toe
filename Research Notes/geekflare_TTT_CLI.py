# code from tutorial at https://geekflare.com/tic-tac-toe-python-code/

import random

class TicTacToe:

    def __init__(self): 
        # "__init__" is a reseved method in python classes. It is known as a constructor in object oriented concepts. This method called when an object is created from the class and it allow the class to initialize the attributes of a class. 

        # source: https://micropyramid.com/blog/understand-self-and-__init__-method-in-python-class/
        self.board = []
        # initializes tic-tac-toe board as an empty list



    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)
            
            
    def get_random_first_player(self):
        return random.randint(0, 1) # used to select who goes first: X or O


    def pick_spot(self, row, col, player):
        self.board[row][col] = player # replaces the '-' with either X or O


    def is_player_win(self, player):
        win = None
        n = len(self.board)

        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True


    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True


    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'


    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=' ') # creates the columns
            print() # creates the rows


    
    def start(self):
        self.create_board() # create the tic tac toe board

        player = 'X' if self.get_random_first_player() == 1 else 'O' # assign first player

        while True: # begin game-play loop
            print(f"\nPlayer {player}'s turn.\n") # display whose turn to play (X or O)

            self.show_board() # display current board for player

            # capture player input
            row, col = list(map(int, input(f"\nEnter row then column number to place your '{player}': ").split()))
            print() 

            # placing marker based on player input
            self.pick_spot(row - 1, col - 1, player) # -1 to get to actual index as users enter 1, 2 or 3

            # check whether current player has won
            if self.is_player_win(player):
                print(f"\nPlayer {player} wins the game!\n")
                break # end game-play loop

            # check for draw
            if self.is_board_filled():
                print("\nMatch draw!\n")
                break # end game-play loop

            # swapping turns
            player = self.swap_player_turn(player)

        # display final view of board
        print()
        self.show_board()


# test the game
tic_tac_toe = TicTacToe()
tic_tac_toe.start()













    
