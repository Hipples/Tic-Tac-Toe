"""
This module is designed to define a variety of gameplay objects required for our tic tac toe
gameplay loops. The following classes have been included:

    - TicTacToeBoard
    - PlayerActions
    - AI
"""
import random
from time import sleep
import numpy as np


class TicTacToeBoards:
    """
    TicTacToeBoards is the parent class of PlayerActions and the grandparent class of AI.

    This class contains methods designed to generate, display, write to, read from, and reset both
    tic tac toe gameboards.

        - create_board(board_option)
        - print_classic_board()
        - print_big_board()
        - display_board(board_option)
        - reset_board()
        - place_marker(row, col, player)
        - is_board_full(board_option)
        - is_winner_by_row(board, player, board_option)
        - is_winner_by_col(board, player, board_option)
        - is_winner_by_diag(board, player, board_option)
        - is_winner(board, player, board_option)
    """

    def __init__(self):
        """
        TicTacToeBoard initializes the following class variables:

            - self.board
            - self.board_record
            - self.human_record
            - self.computer_record
            - self.classic
            - self.board_option
            - self.big
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
        """Generates specified gameboard (3x3 or 5x5)."""
        # classic board
        if board_option == 1:
            for i in np.arange(1, 10).astype(str):  # nine numbers, as strings
                self.board.append(i)  # for datatype consistency with X and O
            self.board = np.reshape(self.board, (3, 3))  # shaped into 3 rows x 3 columns
        # big board
        if board_option == 2:
            for i in np.arange(1, 26).astype(str):
                self.board.append(i)
            self.board = np.reshape(self.board, (5, 5))

    def print_classic_board(self):
        """Prints the classic, 3x3, gameboard."""
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
        """Prints the big, 5x5, gameboard."""
        print('\t---------------------------------------------------')
        for row in self.board:
            print('\t|         |         |         |         |         |')
            print('\t|', end = '')
            for item in row:
                # C0209: Formatting a regular string which could be a f-string
                #        (consider-using-f-string) -pylama
                print('    %2s   |' %item, end = '')
            print()
            print('\t|         |         |         |         |         |')
            print('\t---------------------------------------------------')

    def display_board(self, board_option):
        """Displays current gameboard."""
        if board_option == 1:
            self.print_classic_board()
        if board_option == 2:
            self.print_big_board()

    def reset_board(self):
        """Resets the gameboard and any record values to an empty list."""
        self.board = []
        self.board_record = []
        self.human_record = []
        self.computer_record = []

    def place_marker(self, row, col, player):
        """Places the player marker (X or O) in the designated square."""
        self.board[row][col] = player

    def is_draw(self, board_option):
        """Returns True if there is a draw for the specified board."""
        for row in self.board:
            for square in row:
                # classic board
                if board_option == 1:
                    if square in self.classic:
                        return False
                # big board
                if board_option == 2:
                    if square in self.big:
                        return False
        return True

    def is_winner_by_row(self, board, player, board_option):
        """Checks for horizontal winning patterns on the specified gameboard."""
        # classic board
        if board_option == 1:
            for row in range(3):
                if board[row][0] == board[row][1] and board[row][1] == board[row][2]:
                    if board[row][0] == player:
                        return True
        # big board
        if board_option == 2:
            for row in range(5):
                if board[row][0] == board[row][1] and board[row][1] == board[row][2]\
                and board[row][2] == board[row][3] and board[row][3] == board[row][4]:
                    if board[row][0] == player:
                        return True
        return False

    def is_winner_by_col(self, board, player, board_option):
        """Checks for vertical winning patterns on the specified gameboard."""
        # classic board
        if board_option == 1:
            for col in range(3):
                if board[0][col] == board[1][col] and board[1][col] == board[2][col]:
                    if board[0][col] == player:
                        return True
        # big board
        if board_option == 2:
            for col in range(5):
                if board[0][col] == board[1][col] and board[1][col] == board[2][col]\
                and board[2][col] == board[3][col] and board[3][col] == board[4][col]:
                    if board[0][col] == player:
                        return True
        return False

    def is_winner_by_diag(self, board, player, board_option):
        """Checks for diagonal winning patterns on specified board."""
        # classic board
        if board_option == 1:
            # check descending diagonal for win
            if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
                if board[0][0] == player:
                    return True
            # check ascending diagonal for win
            if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
                if board[0][2] == player:
                    return True
        # big board
        if board_option == 2:
            # check descending diagonal for win
            if board[0][0] == board[1][1] and board[1][1] == board[2][2]\
            and board[2][2] == board[3][3] and board[3][3] == board[4][4]:
                if board[0][0] == player:
                    return True
            # check ascending diagonal for win
            if board[0][4] == board[1][3] and board[1][3] == board[2][2]\
            and board[2][2] == board[3][1] and board[3][1] == board[4][0]:
                if board[0][4] == player:
                    return True
        return False

    def is_winner(self, board, player, board_option):
        """Checks specified gameboard for winning patterns and returns True if one is found."""
        if self.is_winner_by_row(board, player, board_option):
            return True
        if self.is_winner_by_col(board, player, board_option):
            return True
        if self.is_winner_by_diag(board, player, board_option):
            return True
        return False


class PlayerActions(TicTacToeBoards):
    """
    PlayerActions is the child class of TicTacToeBoards and the parent class of AI.
    PlayerActions contains methods designed to swap player turns, assign player markers (X or O),
    and acquire and apply player move choices.

    Class methods include:

        - choose_marker()
        - assign_markers()
        - player_turn(player)
        - get_coords(player)
        - player_move(player)
        - swap_player_turn(player)
    """
    def __init__(self):
        """
        PlayerActions initializes with all parent methods/variables and defines the following:

            - self.match_records
            - self.player
            - self.opponent
        """
        super().__init__()
        self.match_records = "tic.tac.toe.txt"
        self.player = ''
        self.opponent = ''

    def choose_marker(self):
        """Allows the main player to choose to be X or O."""
        marker = ' '  # declare marker variable as empty string
        while marker not in ('X', 'O'):  # while marker does not equal X or O
            marker = input("\n\tDo you want to be Xs or Os? ").upper()  # choose X or O
        if marker == 'X':  # if X,
            return ['X', 'O']  # then return X, O
        return ['O', 'X']  # if O, then return O, X

    def assign_markers(self):  # retrieve marker order from choose_marker() method
        """Assigns X and O markers to the appropriate players."""
        self.player, self.opponent = self.choose_marker()  # assign the first char to our player,
        return self.player, self.opponent  # and the second char to our opponent

    def player_turn(self, player):
        """Acquires player input to determine desired move."""
        move = input(f"\n\tPlease enter the number where you'd like to place your {player}: ")
        print(f"\n\tYou chose square {move}!")  # acquire player input to determine desired move
        return move  # return chosen square value

    def get_coords(self, player):
        """Determines the coordinates of the 'empty' square value provided."""
        move = self.player_turn(player)  # retrieve player move from human_moves() method
        coords = []  # declare empty list to store move coordinates
        coords = np.where(self.board == move)  # determine move coordinates
        return coords  # return move coordinates

    def player_move(self, player):
        """Captures, records, and fulfills human moves while handling exceptions."""
        while True:  # exception catching loop
            try:  # attempt to initialize coords, by retrieving the player's input,
                coords = self.get_coords(player)  # through get_coords() method,
                row, col = int(coords[0]), int(coords[1])  # assign the proper index of the move
            except KeyboardInterrupt:  # enable Ctrl + c to end program during player input
                print("\n\n\tGood bye!")  # when used - program says good bye,
                exit()  # then ends
            # W0702: No exception type(s) specified (bare-except) -pylama
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
        """Swaps game control between the two players."""
        return 'X' if player == 'O' else 'O'

class AI(PlayerActions):
    """
    AI is the child class of PlayerActions and the grandchild class of TicTacToeBoard.
    AI contains methods designed to activate a random AI and a minimax AI opponent for their
    respective gamemodes.

    Class methods include:

        - random_logic(board_option)
        - random_move(player, board_option)
        - get_open_squares(board_option)
        - can_win(board_option)
        - first_move(board_option)
        - urgent_move(board_option)
        - full_board(board_option)
        - is_last_move(board_option)
        - urgent_move()
        - minimax_logic()
        - minimax_move()
    """
    def __init__(self):
        """
        AI initializes with all of its parent and grandparent class variables, as well as:

            - self.max_score
            - self.best_move
            - self.winning_patterns
            - self.big_win_patterns
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
                                 ['16', '17', '18', '19', '20'], [ '4',  '9', '14', '19', '24'],
                                 ['21', '22', '23', '24', '25'], [ '5', '10', '15', '20', '25'],
                                 [ '1',  '7', '13', '19', '25'], [ '5',  '9', '13', '17', '21']]

    # TODO: could probably use the get_open_squares() methods below and make this
    # a three line method, but, another time.
    def random_logic(self, board_option):
        """Returns a random, available, square number from the current gameboard."""
        possible_moves = []  # declare an empty list of possible moves
        for row in self.board:  # for each row in our gameboard,
            for square in row:  # and for each square in said row,
                # if classic board
                if board_option == 1:
                    if square in self.classic:  # if the square's value is in our classic list
                        possible_moves.append(square)  # store it in our list of available squares
                # if big board
                if board_option == 2:
                    if square in self.big:
                        possible_moves.append(square)
        move = random.choice(possible_moves)  # determine a random, available move for AI
        return move  # from our list of possible moves

    def random_move(self, player, board_option):
        """Captures, records, and fullfils the Random AI's turn in game."""
        move = self.random_logic(board_option)  # generates random move,
        coords = np.where(self.board == move)  # sets the move coordinates
        row, col = (int(coords[0])), (int(coords[1]))  # assign the proper index of the move
        sleep(1) # (our AI is thinking. . .)
        print(f"\n\tRandom AI chooses square {move}!\n")  # announce Random AI's move
        with open(self.match_records, 'a') as record:  # open our match records and
            record.write(f"{player}:{move} ")  # append the Random AI move
        self.place_marker(row, col, player)  # as it happens

    def get_open_squares(self, board_option):
        """Obtains all available moves from the board records for the minimax alogrithm."""
        squares = []
        # classic board
        if board_option == 1:
            for square in list(set(self.classic) - set(self.board_record)):
                squares.append(square)
            return squares
        # big board
        if board_option == 2:
            for square in list(set(self.big) - set(self.board_record)):
                squares.append(square)
            return squares
        return None

    def can_win(self, board_option):
        """Returns potential winners found by the minimax AI's branch searches."""
        # classic board
        if board_option == 1:
            for win in self.winning_patterns:
                if set(win) <= set(self.computer_record):
                    return self.opponent
                if set(win) <= set(self.human_record):
                    return self.player
        # big board
        if board_option == 2:
            for win in self.big_win_patterns:
                if set(win) <= set(self.computer_record):
                    return self.opponent
                if set(win) <= set(self.human_record):
                    return self.player
        return False

    def first_move(self, board_option):
        """
        Tells minimax AI to take a corner position on the specified board if it is assigned
        first player.
        """
        # classic board
        if board_option == 1:
            move = random.choices([1, 3, 7, 9])[0]
            return move
        # big board
        if board_option == 2:
            move = random.choices([1, 5, 21, 25])[0]
            return move
        return False

    def urgent_move(self, board_option):
        """Checks for any wins that could be obtained or prevented each turn by the minimax AI."""
        # classic board
        if board_option ==1:
            winpatten = self.winning_patterns
        # big board
        else:
            winpatten = self.big_win_patterns

        # checking computer moves
        for win in winpatten:
            if len(list(set(win) - set(self.computer_record))) == 1\
            and len(set(self.computer_record)) > 1:
                move = list(set(win) - set(self.computer_record))[0]
                if move not in set(self.human_record):
                    return move
        # checking human moves
        for win in winpatten:
            if len(list(set(win) - set(self.human_record))) == 1\
            and len(set(self.human_record)) > 1:
                move = list(set(win) - set(self.human_record))[0]
                if move not in set(self.computer_record):
                    return move
        return False

    def full_board(self, board_option) -> bool:
        """Tells the minimax AI when there are no more moves available to check."""
        # classic board
        if board_option == 1:
            if len(self.board_record) == 9:
                return True
        # big board
        if board_option == 2:
            if len(self.board_record) == 25:
                return True
        return False

    def is_last_move(self, board_option) -> bool:
        """Checks if there is only one available move left for minimax AI."""
        # classic board
        if board_option == 1 and len(self.board_record) == 8:
            return True
        # big board
        if board_option == 2 and len(self.board_record) == 24:
            return True
        return False

    def is_urgent(self, board_option) -> bool:
        """"
        Checks if enough markers have been placed for someone to have a potential win
        for minimax AI.
        """
        # classic board
        if board_option == 1 and (len(self.board_record) > 3):
            return True
        # big board
        if board_option == 2 and (len(self.board_record) > 7):
            return True
        return False

    def is_early_move(self, board_option) -> bool:
        """
        Checks if the big board has at least 12 markers placed for the minimax AI to
        limit nodes.
        """
        # big board
        if board_option == 2 and len(self.board_record) < 12:
            return True
        return False
    
    def append_moves(self, player, move):
        """Appends moves to specified record for minimax AI."""
        if player == self.opponent:  # if player is the computer
            self.computer_record.append(move)  # add move to the computer record
        else:  # otherwise
            self.human_record.append(move)  # add move to the human record
        self.board_record.append(move)  # record any moves to the board record afterwards

    def pop_moves(self, player):
        """Removes moves from specified record for minimax AI."""
        if player == self.opponent:  # now, if player is the computer
            self.computer_record.pop()  # remove the most recently appended move from its record
        else:  # otherwise
            self.human_record.pop()  # remove the most recent move from the human record
        self.board_record.pop()  # remove the most recent move from the board record

    # TODO: Need to do something about the amount of time our minimax AI takes to make a choice
    # on the big board. Slash, this is potentially not fully functional on either board at the
    # moment due to edits from debugging the big board.

    def minimax_logic(self, player, board_option, depth = 0):
        """Logic used by minimax AI to discover best next move."""
        if player == self.opponent:  # sets max_score
            self.max_score = -10  # as -10 if player is the computer
        else:  # otherwise
            self.max_score = 10  # as +10

        # TODO: using this chunk, we only break recursion if a win or draw has been discovered...
        # potential place to work on reducing the amount of time the AI takes choosing a move on
        # the big board

        if self.is_urgent(board_option):
            result = self.can_win(board_option)  # check for winning player and
            if result == self.opponent:  # if winner is the computer,
                return 10 + depth, None  # return depth + 10
            if result == self.player:  # if winner is human
                return -10 - depth, None  # return depth - 10
            if self.full_board(board_option):  # if the board is already full,
                return 0, None  # return 0 --> this chunk breaks the recursive calls on each open square

        for move in self.get_open_squares(board_option):  # then, for each available move
            self.append_moves(player, move)
            player = self.swap_player_turn(player)  # and swap players
            score, _ = self.minimax_logic(player, board_option, depth + 1)  # do the recursive thing
            player = self.swap_player_turn(player)  # and swap players again
            self.pop_moves(player)

            if player == self.opponent:  # next, if the player is the computer,
                if score > self.max_score:  # and if the current score is greater than our max score
                    self.max_score = score  # set the return variables
                    self.best_move = move
            else :  # otherwise, if human,
                if score < self.max_score:  # and if our score is lower than the max score
                    self.max_score = score  # set the return variables
                    self.best_move = move
        return self.max_score, self.best_move  # returns the best move with the max score potential

    # TODO: Need to do something about the amount of time our minimax AI takes to make a choice on
    # the big board. Slash, this is potentially not fully functional on either board at the moment
    # due to edits from debugging the big board.

    def minimax_move(self, player, board_option):
        """Captures, records, and fullfils the minimax AI's turn in game."""
        # is it the first move of the game?
        if len(self.board_record) == 0:
            move = self.first_move(board_option)
        # is it the last move of the game?
        elif self.is_last_move(board_option):
            move = self.get_open_squares(board_option)[0]
        # can a win be obtained or prevented with this move?
        elif self.is_urgent(board_option):
            move = self.urgent_move(board_option)  # win or prevent win
        # if all that fails, do a minimax search 
            if move is False:
                _, move = self.minimax_logic(player, board_option)  # holds score
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
