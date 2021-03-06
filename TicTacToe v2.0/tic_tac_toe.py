"""Module Designed for Tic Tac Toe Gameplay Methods"""

import random
from time import sleep
import numpy as np

# Tic Tac Toe, Three in a Row!
class TicTacToe:
    """Play a TicTacToe game!"""
    def __init__(self) -> None:  # initialize our class with
        self.board = []  # an empty gameboard,
        self.values = ['1', '2', '3', '4', '5', '6', '7', '8', '9']  # a list of empty squares,
        self.match_records = 'tic_tac_toe.txt'  # text record of match movements and outcomes

# copied
    def create_board(self):
        """Create a 3x3 gameboard."""
        for i in np.arange(1, 10).astype(str):  # nine numbers, as strings, because we replace
            self.board.append(i)  # the empty board numbers with Xs and Os (datatype consistency)
        self.board = np.reshape(self.board, (3, 3))  # shaped into 3 rows x 3 columns
# copied
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
# copied
    def reset_board(self):
        """Reset the gameboard."""
        self.board = [] # reset to an empty list
# copied
    def choose_marker(self):
        """Allows main player to choose to be X or O"""
        marker = ' ' # declare marker variable as empty string
        while marker not in ('X', 'O'): # while marker does not equal X or O
            marker = input("\n\tDo you want to be Xs or Os? ").upper() # ask player to choose X or O
        if marker == 'X': # if X,
            return ['X', 'O'] # then return X, O
        return ['O', 'X'] # if O, then return O, X
# copied
    def assign_markers(self):  # retrieve marker order from choose_marker() method
        """Assigns gameboard markers (X and O) to the appropriate player."""
        player, opponent = self.choose_marker()  # assign the first char returned to our player,
        return player, opponent  # and the second char to our player's opponent
# copied
    def coin_flip(self):  # winner goes first
        """Randomly returns a value of either a 0 or 1."""
        return random.randint(0, 1)  # heads or tails?
# copied
    def human_moves(self, player):
        """Acquires player input to determine desired move (1-9)."""
        move = input(f"\n\tPlease enter the square number where you'd like to place your {player}: ")
        print(f"\n\tYou chose square {move}!") # acquire player input to determine desired move
        return move # return chosen square number
# copied
    def get_coords(self, player):
        """Determines the coordinates of the 'empty' square value provided."""
        move = self.human_moves(player) # retrieve player move from human_moves() method
        coords = [] # declare empty list to store move coordinates
        coords = np.where(self.board == move) # determine move coordinates
        return coords # return move coordinates
# copied
    def random_moves(self):
        """Returns a random, available, square number for the easy AI's desired move."""
        possible_moves = [] # declare an empty list of possible moves
        for row in self.board: # for each row in our gameboard,
            for square in row: # and for each square in said row,
                if square in self.values: # if the square's value is in our values list
                    possible_moves.append(square) # store it in our list of available squares
        move = random.choice(possible_moves) # determine a random, available move for AI
        return move # from our list of possible moves
# copied
    def place_marker(self, row, col, player):
        """Places the player marker (X or O) in the designated square."""
        self.board[row][col] = player # use move coordinates to place marker in the chosen square
# copied
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
# copied
    def computer_move(self, player):
        """Capture, record, and fullfil random AI movement during computer player turns."""
        move = self.random_moves() # get randomly generate move from random_moves() method
        coords = np.where(self.board == move) # set the move coordinates
        row, col = (int(coords[0])), (int(coords[1])) # assign the proper index of the move
        sleep(2) # (our AI is thinking. . .)
        print(f"\n\tRandAI chooses square {move}!\n") # announce RandAI's move
        with open(self.match_records, 'a') as record: # open our match records and
            record.write(f"{player}:{move} ") # append each Random AI move
        self.place_marker(row, col, player) # as it happens
# copied
    def is_board_full(self):
        """Determines if gameboard is full (DRAW)."""
        for row in self.board: # for each row on the board,
            for square in row: # and for each square in said row,
                if square in self.values: # if the square value is in our list of empty squares
                    return False # return False
        return True # otherwise return True
# copied
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
# copied
    def swap_player_turn(self, player):
        """Swaps game control between two players."""
        return 'X' if player == 'O' else 'O'
# copied
    def replay(self):
        """Asks if main player would like to replay the current gamemode."""
        replay = input("\n\tWould you like to play again? (y/n) ")
        print()
        if replay.lower() == 'y':
            return True
        if replay.lower() == 'n':
            return False
        self.replay()

    def game_mode_2(self):
        """PvE Mode - Easy. Random AI opponent."""
        # initiate replay loop
        while True:
            # 0. append 'New Game!' to tic_tac_toe.txt
            with open(self.match_records, 'a') as record:
                record.write("\n\nNew Game!\n")
            # 1. create the gameboard
            self.create_board()
            # 2. assign markers based on choice
            player, computer = self.assign_markers()
            # 3. randomly decide which player goes first
            if self.coin_flip() == 1:
                first_player = player
            else:
                first_player = computer
            # 4. inform the players who won first turn
            print(f"\n\tPlayer {first_player} will go first!\n")
            # 5. display empty gameboard
            self.display_board()
            # 6a. if human player. . .
            if first_player == player:
                # input and make move
                self.player_move(first_player)
                print()
                # display updated gameboard
                self.display_board()
                # assign to current player
                current_player = player
            # 6b. if computer player. . .
            else:
                # generate and make random move
                self.computer_move(first_player)
                print()
                # display updated gameboard
                self.display_board()
                # assign to current player
                current_player = computer
            # 7. main game play loop
            while True:
                # 8. swap player turn
                current_player = self.swap_player_turn(current_player)
                # 9. display the current player
                print(f"\n\tPlayer {current_player}'s turn.\n")
                # 10a. if player is human, use player_move method
                if current_player == player:
                    self.player_move(current_player)
                # 10b. if player is a computer, use computer_move method
                else:
                    self.computer_move(current_player)
                # 11a. check if there is a winner
                if self.is_winner(self.board, current_player):
                    print(f"\n\tPlayer {current_player} wins the game!\n")
                    # 11b. record the winner in tic_tac_toe.txt
                    with open(self.match_records, 'a') as record:
                        record.write(f"\nPlayer {current_player} won the game!\n")
                    # 11c. game over
                    break
                # 12a. check if there is a draw
                if self.is_board_full():
                    print("\n\tMatch draw!\n")
                    # 12b. record the draw status in tic_tac_toe.txt
                    with open(self.match_records, 'a') as record:
                        record.write("\nMatch was a draw!\n")
                    # 12c. game over
                    break
                # 13. display updated gameboard
                self.display_board()
            print()
            # 14. final gameboard display
            self.display_board()
            print()
            # 15. reset the gameboard
            self.reset_board()
            # 16. replay option
            if self.replay() == False:
                break

# copied
    # PvP mode gameplay loop
    def game_mode_1(self):
        """Original PvP mode."""
        # initiate reply loop
        while True:
            # 0. append 'New Game!' to tic_tac_toe.txt
            with open(self.match_records, 'a') as record:
                record.write("\n\nNew Game!\n")
            # 1. create the gameboard
            self.create_board()
            # 2. assign player markers based on choice
            player, opponent = self.assign_markers()
            # 3. randomly decide which player goes first
            if self.coin_flip() == 1:
                first_player = player
            else:
                first_player = opponent
            # 4. inform the players who won first turn
            print(f"\n\tPlayer {first_player} will go first!\n")
            # 5. display empty gameboard
            self.display_board()
            # 6. input and make move
            self.player_move(first_player)
            print()
            # 7. display updated gameboard
            self.display_board()
            # 8. assign current_player as first_player
            current_player = first_player
            while True:
                # 9. swap player turn
                current_player = self.swap_player_turn(current_player)
                # 10. display whose turn to play
                print(f"\n\tPlayer {current_player}'s turn.\n")
                sleep(1)
                # 11. display updated gameboard
                self.display_board()
                # 12. capture and make player move
                self.player_move(current_player)
                print()
                # 13a. check if there is a winner
                if self.is_winner(self.board, current_player):
                    print(f"\n\tPlayer {current_player} wins the game!\n")
                    # 13b. record the winner in tic_tac_toe.txt
                    with open(self.match_records, 'a') as record:
                        record.write(f"\nPlayer {current_player} won the game!\n")
                    # 13c. game over
                    break
                # 14a. check if there is a draw
                if self.is_board_full():
                    print("\n\tMatch draw!\n")
                    # 14b. record the draw status in tic_tac_toe.txt
                    with open(self.match_records, 'a') as record:
                        record.write("\nMatch was a draw!\n")
                    # 14c. game over
                    break
                # 15. display updated gameboard
                self.display_board()
            print()
            # 16. final gameboard display
            self.display_board()
            print()
            # 17. reset gameboard
            self.reset_board()
            # 18. replay option
            if self.replay() == False:
                break
