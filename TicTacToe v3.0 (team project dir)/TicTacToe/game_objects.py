"""TODO: Module Docstring...."""
import random
from time import sleep
import numpy as np

class TicTacToeBoard:
    """TODO: class docstring...."""

# OC --> changed self.values to self.default & removed self.match_records
    def __init__(self):
        """TODO: Initialization docstring..."""
        self.board = []  # empty gameboard
        self.default = ['1', '2', '3', '4', '5', '6', '7', '8', '9'] # default board size

# OC
    def create_board(self):
        """Create a 3x3 gameboard."""
        for i in np.arange(1, 10).astype(str):  # nine numbers, as strings, because we replace
            self.board.append(i)  # the empty board numbers with Xs and Os (datatype consistency)
        self.board = np.reshape(self.board, (3, 3))  # shaped into 3 rows x 3 columns

# OC
    def display_board(self):
        """Display current gameboard."""
        print('\t-------------------------------')
        for row in self.board:
            print('\t|         |         |         |')
            print('\t|', end = '')
            for item in row:
                print(f'    {item}    |', end = '')
            print()
            print('\t|         |         |         |')
            print('\t-------------------------------')

# OC
    def reset_board(self):
        """Reset the gameboard."""
        self.board = [] # reset to an empty list

# OC
    def place_marker(self, row, col, player):
        """Places the player marker (X or O) in the designated square."""
        self.board[row][col] = player # use move coordinates to place marker in the chosen square

# OC --> self.values changed to self.default
    def is_board_full(self):
        """Determines if gameboard is full (DRAW)."""
        for row in self.board: # for each row on the board,
            for square in row: # and for each square in said row,
                if square in self.default: # if the square value is in our list of empty squares
                    return False # return False
        return True # otherwise return True

# OC
    def is_winner(self, board, player):
        """Checks gameboard for winning patterns."""
        win = None
        # check rows for win
        for row in range(3):
            if board[row][0] == board[row][1] and board[row][1] == board[row][2]:
                if board[row][0] == player:
                    win = True
            if win:
                return win
        # check columns for win
        for col in range(3):
            if board[0][col] == board[1][col] and board[1][col] == board[2][col]:
                if board[0][col] == player:
                    win = True
            if win:
                return win
        # check descending diagonal for win
        if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            if board[0][0] == player:
                win = True
        if win:
            return win
        # check ascending diagonal for win
        if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
            if board[0][2] == player:
                win = True
        if win:
            return win


# refactoring is_winner(self)

    # def is_winner_by_row(self, board, player):
    #     """Checks for horizontal winning patterns."""
    #     for row in range(3):
    #         if board[row][0] == board[row][1] and board[row][1] == board[row][2]:
    #             if board[row][0] == player:
    #                 return True

    # def is_winner_by_col(self, board, player):
    #     """Checks for vertical winning patterns."""
    #     for col in range(3):
    #         if board[0][col] == board[1][col] and board[1][col] == board[2][col]:
    #             if board[0][col] == player:
    #                 return True

    # def is_winner_by_diag(self, board, player):
    #     """Checks for diagonal winning patterns."""  
    #     # check descending diagonal for win
    #     if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
    #         if board[0][0] == player:
    #             return True
    #     # check ascending diagonal for win
    #     if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
    #         if board[0][2] == player:
    #             return True

    # def is_winner(self, board, player):
    #     win = False
    #     if self.is_winner_by_row(board, player):
    #         win = True
    #     if self.is_winner_by_col(board, player):
    #         win = True
    #     if self.is_winner_by_diag(board, player):
    #         win = True
    #     return win


class PlayerActions(TicTacToeBoard):
    """Class contains methods that: allow players to choose their game markers ('X' or 'O'), acquires input from players on their turn, applies the player input to complete thier move, """
    def __init__(self):
        super().__init__()
        self.match_records = "tic.tac.toe.txt"

# OC
    def choose_marker(self):
        """Allows main player to choose to be X or O"""
        marker = ' '  # declare marker variable as empty string
        while marker not in ('X', 'O'):  # while marker does not equal X or O
            marker = input("\n\tDo you want to be Xs or Os? ").upper()  # ask player to choose X or O
        if marker == 'X':  # if X,
            return ['X', 'O']  # then return X, O
        return ['O', 'X']  # if O, then return O, X

# OC
    def assign_markers(self):  # retrieve marker order from choose_marker() method
        """Assigns gameboard markers (X and O) to the appropriate player."""
        player, opponent = self.choose_marker()  # assign the first char returned to our player,
        return player, opponent  # and the second char to our player's opponent

# OC --> renamed from human_moves() to player_turn()    
    def player_turn(self, player):
        """Acquires player input to determine desired move (1-9)."""
        move = input(f"\n\tPlease enter the square number where you'd like to place your {player}: ")
        print(f"\n\tYou chose square {move}!") # acquire player input to determine desired move
        return move # return chosen square number

# OC
    def player_move(self, player):
        """Capture, record, and fulfill human player moves while handling exceptions."""
        while True: # exception catching loop
            try: # attempt to initialize coords, by retrieving the player's input,
                coords = self.get_coords(player) # through get_coords() method,
                row, col = int(coords[0]), int(coords[1]) # then assign the proper index of the move
            except KeyboardInterrupt: # enable Ctrl + c to end program during player input
                print("\n\n\tGood bye!") # program says good bye,
                exit() # then ends
            except: # continue looping until valid input is accepted
                print("\n\tBad input! Try again.\n") # announce when input is invalid
            else: # otherwise, reverse engineer our player move by using our determined index
                move = self.board[row][col] # and assign it to move
                with open(self.match_records, 'a') as record: # then open our match records and
                    record.write(f"{player}:{move} ") # append each valid player move
                self.place_marker(row, col, player) # as it happens
                return False # before ending our loop

# OC --> changed self.human_moves() to self.player_turn()
    def get_coords(self, player):
        """Determines the coordinates of the 'empty' square value provided."""
        move = self.player_turn(player) # retrieve player move from human_moves() method
        coords = [] # declare empty list to store move coordinates
        coords = np.where(self.board == move) # determine move coordinates
        return coords # return move coordinates

class AI(PlayerActions):
    """TODO: Class docstring..."""

    def __init__(self):
        super().__init__()

# OC --> change name from random_moves() to random_logic() and self.values to self.default  
    def random_logic(self):
        """Returns a random, available, square number for the easy AI's desired move."""
        possible_moves = [] # declare an empty list of possible moves
        for row in self.board: # for each row in our gameboard,
            for square in row: # and for each square in said row,
                if square in self.default: # if the square's value is in our values list
                    possible_moves.append(square) # store it in our list of available squares
        move = random.choice(possible_moves) # determine a random, available move for AI
        return move # from our list of possible moves

# OC --> changed name from computer_move() to random_move(), changed self.random_moves() to self.random_logic()
    def random_move(self, player):
        """Capture, record, and fullfil random AI movement during computer player turns."""
        move = self.random_logic() # get randomly generate move from random_moves() method
        coords = np.where(self.board == move) # set the move coordinates
        row, col = (int(coords[0])), (int(coords[1])) # assign the proper index of the move
        sleep(2) # (our AI is thinking. . .)
        print(f"\n\tRandAI chooses square {move}!\n") # announce RandAI's move
        with open(self.match_records, 'a') as record: # open our match records and
            record.write(f"{player}:{move} ") # append each Random AI move
        self.place_marker(row, col, player) # as it happens

# future AI player logic
    def minimax_turn(self):
        pass

    def minmax_move(self):
        pass
