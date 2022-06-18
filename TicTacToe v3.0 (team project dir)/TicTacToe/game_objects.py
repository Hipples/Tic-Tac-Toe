"""
This modules is designed to define a variety of gameplay objects required for our tic tac toe gameplay loops.
The following classes have been included:

    - TicTacToeBoard        x. classic 3x3 and big 5x5 board options included
    - PlayerActions         x. human player actions and records included
    - AI                    x. random AI and minimax AI logics included
"""
import random
from time import sleep
import numpy as np

class TicTacToeBoards:
    """
    The class TicTacToeBoard is the parent class of PlayerActions and the grandparent class of AI.
    This class contains methods designed to generate, display, write to, read from, and reset the
    tic tac toe gameboards.

    - Methods for classic, 3x3, gameboard:
        - create_board()
        - display_board()
        - is_winner_by_row()
        - is_winner_by_col()
        - is_winner_by_diag()
        - is_winner()

    - Methods for big, 5x5, gameboard:
        - create_big_board()
        - display_big_board()
        - is_winner_by_big_row()
        - is_winner_by_big_col()
        - is_winner_by_big_diag()
        - is_big_winner()

    - Methods compatible with both board options:
        - reset_board()
        - place_marker()
        - is_board_full()       x. requires a size parameter for the big board option
    """

    def __init__(self):
        """TicTacToeBoard class variables include:

            - self.board               x. used as actual gameboard during each match
            - self.board_record        x. records of marks placed on the board for minimax AI
            - self.human_record        x. records human player marks for minimax AI
            - self.computer_record     x. records computer marks for minimax AI
            - self.classic             x. contains the classic board empty square values (1-9)
            - self.big                 x. contains the big board empty square values (1-25)
            - self.default_size        x. the default board size option is 1 (classic)
        """
        self.board = []
        self.board_record = []
        self.human_record = []
        self.computer_record = []
        self.classic = ['1', '2', '3',  # classic board values
                        '4', '5', '6', 
                        '7', '8', '9']  
        self.board_option = 1  # defaults to classic board
        self.big = [ '1',  '2',  '3',  '4',  '5',  # big board values
                     '6',  '7',  '8',  '9', '10', 
                    '11', '12', '13', '14', '15', 
                    '16', '17', '18', '19', '20', 
                    '21', '22', '23', '24', '25']  

    def create_board(self, board_option):
        """The method create_board() generates a classic, 3x3, gameboard."""
        # if classic board
        if board_option == 1:
            for i in np.arange(1, 10).astype(str):  # nine numbers, as strings, because we replace
                self.board.append(i)  # the empty board numbers with Xs and Os (datatype consistency)
            self.board = np.reshape(self.board, (3, 3))  # shaped into 3 rows x 3 columns
        # if big board
        if board_option == 2:
            for i in np.arange(1, 26).astype(str):
                self.board.append(i)
            self.board = np.reshape(self.board, (5, 5))

    def print_classic_board(self):
        """The method display_board() displays the classic, 3x3, gameboard."""
        print('\t-------------------------------')
        for row in self.board:
            print('\t|         |         |         |')
            print('\t|', end = '')
            for item in row:
                print(f'    {item}    |', end = '')
            print()
            print('\t|         |         |         |')
            print('\t-------------------------------')

    def print_big_board(self):
        """The method display_big_board() display the big, 5x5, gameboard."""
        print('\t---------------------------------------------------')
        for row in self.board:
            print('\t|         |         |         |         |         |')
            print('\t|', end = '')
            for item in row:
                print('    %2s   |' %item, end = '')
            print()
            print('\t|         |         |         |         |         |')
            print('\t---------------------------------------------------')

    def display_board(self, board_option):
        if board_option == 1:
            self.print_classic_board()
        if board_option == 2:
            self.print_big_board()

    def reset_board(self):
        """The method reset_board() resets the gameboard and any record values to an empty list."""
        self.board = []
        self.board_record = []
        self.human_record = []
        self.computer_record = []

    def place_marker(self, row, col, player):
        """The method place_marker() places the player marker (X or O) in the designated square."""
        self.board[row][col] = player

    def is_board_full(self, board_option):
        """The is_board_full() method returns True if there is a draw for specified board."""
        for row in self.board:
            for square in row:
                # if classic board
                if board_option == 1:
                    if square in self.classic:
                        return False
                # if big board
                if board_option == 2:
                    if square in self.big:
                        return False
        return True

    def is_winner_by_row(self, board, player, board_option):
        """The is_winner_by_row() method checks for horizontal winning patterns on the classic board."""
        # if classic board
        if board_option == 1:
            for row in range(3):
                if board[row][0] == board[row][1] and board[row][1] == board[row][2]:
                    if board[row][0] == player:
                        return True
        # if big board
        if board_option == 2:
            for row in range(5):
                if board[row][0] == board[row][1] and board[row][1] == board[row][2] and board[row][2] == board[row][3] and board[row][3] == board[row][4]:
                    if board[row][0] == player:
                        return True

    def is_winner_by_col(self, board, player, board_option):
        """The is_winner_by_col() method checks for vertical winning patterns on the classic board."""
        # if classic board
        if board_option == 1:
            for col in range(3):
                if board[0][col] == board[1][col] and board[1][col] == board[2][col]:
                    if board[0][col] == player:
                        return True
        # if big board
        if board_option == 2:
            for col in range(5):
                if board[0][col] == board[1][col] and board[1][col] == board[2][col] and board[2][col] == board[3][col] and board[3][col] == board[4][col]:
                    if board[0][col] == player:
                        return True

    def is_winner_by_diag(self, board, player, board_option):
        """The is_winner_by_diag() method checks for diagonal winning patterns on specified board."""
        # if classic board
        if board_option == 1:
            # check descending diagonal for win
            if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
                if board[0][0] == player:
                    return True
            # check ascending diagonal for win
            if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
                if board[0][2] == player:
                    return True
        # if big board
        if board_option == 2:
            # check descending diagonal for win
            if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[2][2] == board[3][3] and board[3][3] == board[4][4]:
                if board[0][0] == player:
                    return True
            # check ascending diagonal for win
            if board[0][4] == board[1][3] and board[1][3] == board[2][2] and board[2][2] == board[3][1] and board[3][1] == board[4][0]:
                if board[0][4] == player:
                    return True

    def is_winner(self, board, player, board_option):
        """The is_winner() method checks specified board for winning patterns and returns True if one is found."""
        if self.is_winner_by_row(board, player, board_option):
            return True
        if self.is_winner_by_col(board, player, board_option):
            return True
        if self.is_winner_by_diag(board, player, board_option):
            return True
        return False
  
class PlayerActions(TicTacToeBoards):
    """
    The class PlayerActions is the child class of TicTacToeBoards and the parent class of AI.
    This class contains methods designed to swap player turns, assign player markers (X or O), and acquire and apply player move choices.

    Class methods include:

        - choose_marker()
        - assign_markers()
        - player_turn()
        - get_coords()
        - player_move()
        - swap_player_turn()
    """
    def __init__(self):
        """
        PlayerActions initializes with all parent class variables and defines the following class variables:

            - self.match_records        x. plain text file used to track match records
            - self.player               x. human player character
            - self.opponent             x. ai player character
        """
        super().__init__()
        self.match_records = "tic.tac.toe.txt"
        self.player = ''
        self.opponent = ''

    def choose_marker(self):
        """The method choose_marker() allows the main player to choose to be X or O."""
        marker = ' '  # declare marker variable as empty string
        while marker not in ('X', 'O'):  # while marker does not equal X or O
            marker = input("\n\tDo you want to be Xs or Os? ").upper()  # ask player to choose X or O
        if marker == 'X':  # if X,
            return ['X', 'O']  # then return X, O
        return ['O', 'X']  # if O, then return O, X

    def assign_markers(self):  # retrieve marker order from choose_marker() method
        """The method assign_markers() assigns X and O markers to the appropriate player."""
        self.player, self.opponent = self.choose_marker()  # assign the first char returned to our player,
        return self.player, self.opponent  # and the second char to our opponent
    
    def player_turn(self, player):
        """The method player_turn() acquires player input to determine desired move (1-9)."""
        move = input(f"\n\tPlease enter the square number where you'd like to place your {player}: ")
        print(f"\n\tYou chose square {move}!")  # acquire player input to determine desired move
        return move  # return chosen square value

    def get_coords(self, player):
        """The method get_coords() determines the coordinates of the 'empty' square value provided."""
        move = self.player_turn(player)  # retrieve player move from human_moves() method     
        coords = []  # declare empty list to store move coordinates
        coords = np.where(self.board == move)  # determine move coordinates
        return coords  # return move coordinates

    def player_move(self, player):
        """The player_move() method captures, records, and fulfills human moves while handling exceptions."""
        while True:  # exception catching loop
            try:  # attempt to initialize coords, by retrieving the player's input,
                coords = self.get_coords(player)  # through get_coords() method,
                row, col = int(coords[0]), int(coords[1])  # then assign the proper index of the move
            except KeyboardInterrupt:  # enable Ctrl + c to end program during player input
                print("\n\n\tGood bye!")  # when used - program says good bye,
                exit()  # then ends
            except:  # continue looping until valid input is accepted
                print("\n\tInvalid input. Please try again.\n")  # announce when input is invalid
            else:  # otherwise, reverse engineer our player move by using our determined index
                move = self.board[row][col]  # and assign it to move
                with open(self.match_records, 'a') as record:  # then open our match records and
                    record.write(f"{player}:{move} ")  # append each valid player move
                self.place_marker(row, col, player)  # as it happens
                self.human_record.append(move)  # add move to human records for minimax
                self.board_record.append(move)  # add move to board records for minimax
                return False  # before ending our loop

    def swap_player_turn(self, player):
        """The method swap_player_turn() swaps game control between the two players."""
        return 'X' if player == 'O' else 'O'

class AI(PlayerActions):
    """
    The class AI is the child class of PlayerActions and the grandchild class of TicTacToeBoard.
    This class contains methods designed to activate a random AI and a minimax AI opponent for
    their respective gamemodes.

    Class methods include:

        - random_logic()
        - random_moves()
        - get_open_squares()
        - can_win()
        - full_board()
        - urgent_move()
        - minimax_logic()
        - minimax_move()
    """
    def __init__(self):
        """
        AI initializes with all of its parent and grandparent class variables, as well as:

            - self.max_score                x. defaults to 10, returned from minimax_logic()
            - self.best_move                x. defaults to 0, returned from minimax_logic()
            - self.winning_patterns         x. list of all winning patterns in the classic board
            - self.big_win_patterns         x. list of all winning patterns in the big board
        """
        super().__init__()
        self.max_score = 10
        self.best_move = 0
        self.winning_patterns = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'],
                                 ['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9'],
                                 ['1', '5', '9'], ['3', '5', '7']]

        self.big_win_patterns = [[ '1',  '2',  '3',  '4',  '5'], [ '1',  '6', '11', '16', '21'], 
                                 [ '6',  '7',  '8',  '9', '10'], [ '2',  '7', '12', '17', '22'],
                                 ['11', '12', '13', '14', '15'], [ '3',  '8', '13', '18', '23'],
                                 ['16', '17', '18', '19', '20'], [ '4',  '9', '14', '19', '24'], [ '1',  '7', '13', '19', '25'],
                                 ['21', '22', '23', '24', '25'], [ '5', '10', '15', '20', '25'], [ '5',  '9', '13', '17', '21']]

    def random_logic(self, board_option):
        """Returns a random, available, square number from the current gameboard."""
        possible_moves = [] # declare an empty list of possible moves
        for row in self.board: # for each row in our gameboard,
            for square in row: # and for each square in said row,
                # if classic board
                if board_option == 1:
                    if square in self.classic: # if the square's value is in our values list
                        possible_moves.append(square) # store it in our list of available squares
                # if big board
                if board_option == 2:
                    if square in self.big:
                        possible_moves.append(square)        
        move = random.choice(possible_moves) # determine a random, available move for AI
        return move # from our list of possible moves

    def random_move(self, player, board_option):
        """Capture, record, and fullfil the random AI's turn in game (gamemode #2)."""
        move = self.random_logic(board_option) # get randomly generate move from random_moves() method
        coords = np.where(self.board == move) # set the move coordinates
        row, col = (int(coords[0])), (int(coords[1])) # assign the proper index of the move
        sleep(1) # (our AI is thinking. . .)
        print(f"\n\tRandom AI chooses square {move}!\n") # announce RandAI's move
        with open(self.match_records, 'a') as record: # open our match records and
            record.write(f"{player}:{move} ") # append each Random AI move
        self.place_marker(row, col, player) # as it happens

    def get_open_squares(self, board_option):
        """TODO: method docstring...."""
        squares = []
        if board_option == 1:
            for square in list(set(self.classic) - set(self.board_record)):
                squares.append(square)
            return squares
        if board_option == 2:
            for square in list(set(self.big) - set(self.board_record)):
                squares.append(square)
            return squares

    def can_win(self, board_option, depth):
        """TODO: method docstring...."""
        if board_option == 1:
            if len(self.board_record) > 3:
                for win in self.winning_patterns:
                    if set(win) <= set(self.computer_record):
                        return self.opponent
                    if set(win) <= set(self.human_record):
                        return self.player
            return False
        if board_option == 2:
            if len(self.board_record) > 8:
                if depth <= 5:
                    for win in self.big_win_patterns:
                        if set(win) <= set(self.computer_record):
                            return self.opponent
                        if set(win) <= set(self.human_record):
                            return self.player
            return False

    def full_board(self, board_option):
        """TODO: method docstring...."""
        if board_option == 1:
            if len(self.board_record) == 9:
                return True
        if board_option == 2:
            if len(self.board_record) == 25:
                return True
        return False

    def first_move(self, board_option):
        if board_option == 1: 
            move = random.choices([1, 3, 7, 9])[0]
            return move
        if board_option == 2:
            move = random.choices([1, 5, 21, 25])[0]
            return move

    def urgent_move(self, board_option):
        """TODO: method docstring...."""
        if board_option == 1:
            for win in self.winning_patterns:
                if len(list(set(win) - set(self.computer_record))) == 1 and len(set(self.computer_record)) > 1:
                    move = list(set(win) - set(self.computer_record))[0]
                    if move not in set(self.human_record):
                        return move
            for win in self.winning_patterns:
                if len(list(set(win) - set(self.human_record))) == 1 and len(set(self.human_record)) > 1:
                    move = list(set(win) - set(self.human_record))[0]
                    if move not in set(self.computer_record):
                        return move
        if board_option == 2:
            for win in self.big_win_patterns:
                if len(list(set(win) - set(self.computer_record))) == 1 and len(set(self.computer_record)) > 1:
                    move = list(set(win) - set(self.computer_record))[0]
                    if move not in set(self.human_record):
                        return move
            for win in self.big_win_patterns:
                if len(list(set(win) - set(self.human_record))) == 1 and len(set(self.human_record)) > 1:
                    move = list(set(win) - set(self.human_record))[0]
                    if move not in set(self.computer_record):
                        return move
        return False

    def is_last_move(self, board_option):
        if board_option == 1 and len(self.board_record) == 8:
            return True
        if board_option == 2 and len(self.board_record) == 24:
            return True
        return False        

    def is_urgent_move(self, board_option):
        if board_option == 1 and (len(self.human_record) > 1 or len(self.computer_record) >1):
            return True
        if board_option == 2 and (len(self.human_record) > 3 or len(self.computer_record) > 3):
            return True
        return False

    def is_early_move(self, board_option):
        if board_option == 1:
            return False
        if board_option == 2 and len(self.board_record) < 15:
            return True
        return False

    def minimax_logic(self, player, board_option, depth = 0):
        """TODO: method docstring...."""
        if player == self.opponent:  # initiate max_score
            self.max_score = -10  # as -10 if player is the computer
        else:  # otherwise
            self.max_score = 10  # as +10
        result = self.can_win(board_option, depth)  # check for winning player and
        if result == self.opponent:  # if winner is the computer,
            return 10 + depth, None  # return depth + 10 
        if result == self.player:  # if winner is human
            return -10 - depth, None  # retun depth - 10
        if result == False:
            pass
        if self.full_board(board_option):  # if the board is already full,
                    return 0, None  # return 0
        for move in self.get_open_squares(board_option):  # then, for each available move 
            if player == self.opponent:  # if player is the computer
                self.computer_record.append(move)  # add move to the computer record
            else:  # otherwise
                self.human_record.append(move)  # add move to the human record   
            self.board_record.append(move)  # record any moves to the board record afterwards
            player = self.swap_player_turn(player)  # and swap players
            score, _ = self.minimax_logic(player, board_option, depth + 1)  # before recursively running this method
            player = self.swap_player_turn(player)  # and swapping players again
            if player == self.opponent:  # now, if player is the computer
                self.computer_record.pop()  # remove the most recently appended move from its record
            else:  # otherwise
                self.human_record.pop()  # remove the most recently appended move from the human record
            self.board_record.pop()  # and finally, remove the most recent move from the board record 
            if player == self.opponent:  # next, if the player is the computer,
                if score > self.max_score:  # and if the current score is greater than our max score
                    self.max_score = score  # set the return variables
                    self.best_move = move 
            else :  # otherwise, if human,
                if score < self.max_score:  # and if our score is lower than the max score
                    self.max_score = score  # set the return variables
                    self.best_move = move                    
        return self.max_score, self.best_move  # return the best move with the maximum score potential

    def minimax_move(self, player, board_option):
        """TODO: method docstring...."""
        if len(self.board_record) == 0:
            move = self.first_move(board_option)
        elif self.is_last_move(board_option):
            move = self.get_open_squares(board_option)[0]
        elif self.is_urgent_move(board_option):
            move = self.urgent_move(board_option)  # win or prevent win (classic)
            if move == False:
                if self.is_early_move(board_option):
                    move = self.random_logic(board_option)
                else:
                    _, move = self.minimax_logic(player, board_option)
        elif self.is_early_move(board_option):
            move = self.random_logic(board_option)
        else:   
            _, move = self.minimax_logic(player, board_option)
        move = str(move)
        coords = np.where(self.board == move)
        row, col = (int(coords[0])), (int(coords[1]))
        print(f"\n\tMiniMax AI chooses square {move}!\n")
        with open(self.match_records, 'a') as record: 
            record.write(f"{player}:{move} ")
        self.place_marker(row, col, player)
        self.computer_record.append(move)
        self.board_record.append(move)  
