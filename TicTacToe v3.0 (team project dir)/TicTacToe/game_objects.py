"""TODO: Module Docstring...."""
import random
from time import sleep
import numpy as np

class TicTacToeBoard:
    """TODO: class docstring...."""

    def __init__(self):
        """TODO: Initialization docstring..."""
        self.board = []
        self.board_record = []
        self.human_record = []
        self.computer_record = []
        self.default = ['1', '2', '3', '4', '5', '6', '7', '8', '9'] # default board values
        self.big = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', 
                    '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25'] # big board values

    def create_board(self):
        """Create a 3x3 gameboard."""
        for i in np.arange(1, 10).astype(str):  # nine numbers, as strings, because we replace
            self.board.append(i)  # the empty board numbers with Xs and Os (datatype consistency)
        self.board = np.reshape(self.board, (3, 3))  # shaped into 3 rows x 3 columns

    def create_big_board(self):
        """Create a 5x5 gameboard."""
        for i in np.arange(1, 26).astype(str):
            self.board.append(i)
        self.board = np.reshape(self.board, (5, 5))

    def display_board(self):
        """Display current, classic gameboard."""
        print('\t-------------------------------')
        for row in self.board:
            print('\t|         |         |         |')
            print('\t|', end = '')
            for item in row:
                print(f'    {item}    |', end = '')
            print()
            print('\t|         |         |         |')
            print('\t-------------------------------')

    def display_big_board(self):
        """Display current, big gameboard"""
        print('\t---------------------------------------------------')
        for row in self.board:
            print('\t|         |         |         |         |         |')
            print('\t|', end = '')
            for item in row:
                if int(item) < 10:
                    print(f'    {item}    |', end = '')
                if int(item) > 9:
                    print(f'    {item}   |', end = '')
            print()
            print('\t|         |         |         |         |         |')
            print('\t---------------------------------------------------')     

    def reset_board(self):
        """Reset the gameboard and any records."""
        self.board = [] # reset to an empty list
        self.board_record = []
        self.human_record = []
        self.computer_record = []

    def place_marker(self, row, col, player):
        """Places the player marker (X or O) in the designated square."""
        self.board[row][col] = player # use move coordinates to place marker in the chosen square

    def is_board_full(self):
        """Determines if gameboard is full (DRAW)."""
        for row in self.board: # for each row on the board,
            for square in row: # and for each square in said row,
                if square in self.default: # if the square value is in our list of empty squares
                    return False # return False
        return True # otherwise return True

    def is_winner_by_row(self, board, player):
        """Checks for horizontal winning patterns."""
        for row in range(3):
            if board[row][0] == board[row][1] and board[row][1] == board[row][2]:
                if board[row][0] == player:
                    return True

    def is_winner_by_col(self, board, player):
        """Checks for vertical winning patterns."""
        for col in range(3):
            if board[0][col] == board[1][col] and board[1][col] == board[2][col]:
                if board[0][col] == player:
                    return True

    def is_winner_by_diag(self, board, player):
        """Checks for diagonal winning patterns."""  
        # check descending diagonal for win
        if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            if board[0][0] == player:
                return True
        # check ascending diagonal for win
        if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
            if board[0][2] == player:
                return True

    def is_winner(self, board, player):
        """TODO: method docstring...."""
        win = False
        if self.is_winner_by_row(board, player):
            win = True
        if self.is_winner_by_col(board, player):
            win = True
        if self.is_winner_by_diag(board, player):
            win = True
        return win

class PlayerActions(TicTacToeBoard):
    """Class contains methods that: allow players to choose their game markers ('X' or 'O'), acquires input from players on their turn, applies the player input to complete thier move, """
    def __init__(self):
        super().__init__()

        self.match_records = "tic.tac.toe.txt"
        self.player = ''
        self.opponent = ''

    def swap_player_turn(self, player):
        """Swaps game control between two players."""
        return 'X' if player == 'O' else 'O'

    def choose_marker(self):
        """Allows main player to choose to be X or O."""
        marker = ' '  # declare marker variable as empty string
        while marker not in ('X', 'O'):  # while marker does not equal X or O
            marker = input("\n\tDo you want to be Xs or Os? ").upper()  # ask player to choose X or O
        if marker == 'X':  # if X,
            return ['X', 'O']  # then return X, O
        return ['O', 'X']  # if O, then return O, X

    def assign_markers(self):  # retrieve marker order from choose_marker() method
        """Assigns gameboard markers (X and O) to the appropriate player."""
        self.player, self.opponent = self.choose_marker()  # assign the first char returned to our player,
        return self.player, self.opponent  # and the second char to our player's opponent
    
    def player_turn(self, player):
        """Acquires player input to determine desired move (1-9)."""
        move = input(f"\n\tPlease enter the square number where you'd like to place your {player}: ")
        print(f"\n\tYou chose square {move}!") # acquire player input to determine desired move
        return move # return chosen square number

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
                print("\n\tInvalid input. Please try again.\n") # announce when input is invalid
            else: # otherwise, reverse engineer our player move by using our determined index
                move = self.board[row][col] # and assign it to move
                with open(self.match_records, 'a') as record: # then open our match records and
                    record.write(f"{player}:{move} ") # append each valid player move
                self.place_marker(row, col, player) # as it happens
                self.human_record.append(move)  # add move to human records for minimax
                self.board_record.append(move)  # add move to board records for minimax
                return False # before ending our loop

    def get_coords(self, player):
        """Determines the coordinates of the 'empty' square value provided."""
        move = self.player_turn(player) # retrieve player move from human_moves() method
        coords = [] # declare empty list to store move coordinates
        coords = np.where(self.board == move) # determine move coordinates
        return coords # return move coordinates

class AI(PlayerActions):
    """TODO: Class docstring...."""

    def __init__(self):
        """TODO: init docstring...."""
        super().__init__()
        self.max_score = 10
        self.best_move = 0
        self.winning_patterns = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], 
                                 ['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9'],
                                 ['1', '5', '9'], ['3', '5', '7']]

    def random_logic(self):
        """Returns a random, available, square number from the current gameboard."""
        possible_moves = [] # declare an empty list of possible moves
        for row in self.board: # for each row in our gameboard,
            for square in row: # and for each square in said row,
                if square in self.default: # if the square's value is in our values list
                    possible_moves.append(square) # store it in our list of available squares
        move = random.choice(possible_moves) # determine a random, available move for AI
        return move # from our list of possible moves

    def random_move(self, player):
        """Capture, record, and fullfil the random AI's turn in game (gamemode #2)."""
        move = self.random_logic() # get randomly generate move from random_moves() method
        coords = np.where(self.board == move) # set the move coordinates
        row, col = (int(coords[0])), (int(coords[1])) # assign the proper index of the move
        sleep(2) # (our AI is thinking. . .)
        print(f"\n\tRandom AI chooses square {move}!\n") # announce RandAI's move
        with open(self.match_records, 'a') as record: # open our match records and
            record.write(f"{player}:{move} ") # append each Random AI move
        self.place_marker(row, col, player) # as it happens

    def get_open_squares(self):
        """TODO: method docstring...."""
        squares = []
        for row in list(set(self.default) - set(self.board_record)):
            squares.append(row)
        return squares

    def can_win(self):
        """TODO: method docstring...."""
        for win in self.winning_patterns:
            if set(win) <= set(self.computer_record):
                return self.opponent
            if set(win) <= set(self.human_record):
                return self.player

    def full_board(self):
        """TODO: method docstring...."""
        if len(self.board_record) == 9:
            return True
        else:
            return False

    def urgent_move(self):
        """TODO: method docstring...."""
        for win in self.winning_patterns:
            if len(list(set(win) - set(self.computer_record))) == 1:
                if len(list((set(win) - set(self.board_record)))) > 0:
                    move = list((set(win) - set(self.board_record)))[0]
                    return move
            for win in self.winning_patterns:
                if len(list(set(win) - set(self.human_record))) == 1:
                    if len(list((set(win) - set(self.board_record)))) > 0:
                        move = list((set(win) - set(self.board_record)))[0]
                        return move
                return False

    def minimax_logic(self, player, depth = 0):
        """TODO: method docstring...."""
        if player == self.opponent:  # initiate max_score
            self.max_score = -10  # as -10 if player is the computer
        else:  # otherwise
            self.max_score = 10  # as +10
        if len(self.board_record) >= 5:  # if there are five or more board records,
            result = self.can_win()  # check for winning player and
            if result == self.opponent:  # if winner is the computer,
                return 10 + depth, None  # return depth + 10 
            if result == self.player:  # if winner is human
                return -10 - depth, None  # retun depth - 10
            if self.full_board():  # if the board is already rull,
                return 0, None  # return 0
        for move in self.get_open_squares():  # then, for each available move 
            if player == self.opponent:  # if player is the computer
                self.computer_record.append(move)  # add move to the computer record
            else:  # otherwise
                self.human_record.append(move)  # add move to the human record   
            self.board_record.append(move)  # record any moves to the board record afterwards
            player = self.swap_player_turn(player)  # and swap players
            score, _ = self.minimax_logic(player, depth + 1)  # before recursively running this method
            player = self.swap_player_turn(player)  # and swapping players again
            if player == self.opponent:  # now, if player is the computer
                self.computer_record.pop()  # remove the most recently appended move from its record
            else:  # otherwise
                self.human_record.pop()  # remove the most recently appended move from the human record
            self.board_record.pop()  # and finally, remove the most recent move from the board record as well. 
            if player == self.opponent:  # next, if the player is the computer,
                if score > self.max_score:  # and if the current score is greater than our max score
                    self.max_score = score  # set the return variables
                    self.best_move = move 
            else :  # otherwise, if human,
                if score < self.max_score:  # and if our score is lower than the max score
                    self.max_score = score  # set the return variables
                    self.best_move = move                    
        return self.max_score, self.best_move  # return the best move with the maximum score potential

    def minimax_move(self, player):
        """TODO: method docstring...."""
        if len(self.computer_record) == 0 and len(self.human_record) == 0:
            move = self.random_logic()
        elif len(self.board_record) == 0 and len(self.human_record) == 0:
            move = self.urgent_move()
            if move == False:
                _, move = self.minimax_logic(player)
        else:
            _, move = self.minimax_logic(player)
        move = str(move)
        coords = np.where(self.board == move)
        row, col = (int(coords[0])), (int(coords[1]))  # TODO: coords breaking when only one move left??
        sleep(1)
        print(f"\n\tMiniMax AI chooses square {move}!\n")
        with open(self.match_records, 'a') as record: 
            record.write(f"{player}:{move} ")
        self.place_marker(row, col, player)
        self.computer_record.append(move)
        self.board_record.append(move)  

# test
test = TicTacToeBoard()
test.create_big_board()
test.display_big_board()