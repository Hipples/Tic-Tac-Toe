"""Module contains different AI gameplay logics."""
import random

class Players:
    def __init__(self):
        pass

class RandomAI(Players):
    def __init__(self) -> None:
        pass
        
    # needs updating with new structure    
    def random_AI_move(self):
        """Returns a random, available, square number for the easy AI's desired move."""
        possible_moves = [] # declare an empty list of possible moves
        for row in self.board: # for each row in our gameboard,
            for square in row: # and for each square in said row,
                if square in self.values: # if the square's value is in our values list
                    possible_moves.append(square) # store it in our list of available squares
        move = random.choice(possible_moves) # determine a random, available move for AI
        return move # from our list of possible moves

class MiniMaxAI(Players):
    def __init__(self) -> None:
        pass

    def minimax_AI_move(self):
        """Returns best, available square number for the impossible AI's desired move."""
        pass



# methods from original tic tac toe module involving player logic -- TODO, set up here.

    def choose_marker(self):
        """Allows main player to choose to be X or O"""
        marker = ' ' # declare marker variable as empty string
        while marker not in ('X', 'O'): # while marker does not equal X or O
            marker = input("\n\tDo you want to be Xs or Os? ").upper() # ask player to choose X or O
        if marker == 'X': # if X,
            return ['X', 'O'] # then return X, O
        return ['O', 'X'] # if O, then return O, X


    def coin_flip(self):  # winner goes first
        """Randomly returns a value of either a 0 or 1."""
        return random.randint(0, 1)  # heads or tails?


    def human_moves(self, player):
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
                print("\n\tBad input! Try again.\n") # announce when input is invalid
            else: # otherwise, reverse engineer our player move by using our determined index
                move = self.board[row][col] # and assign it to move
                with open(self.match_records, 'a') as record: # then open our match records and
                    record.write(f"{player}:{move} ") # append each valid player move
                self.place_marker(row, col, player) # as it happens
                return False # before ending our loop


    def get_coords(self, player):
        """Determines the coordinates of the 'empty' square value provided."""
        move = self.human_moves(player) # retrieve player move from human_moves() method
        coords = [] # declare empty list to store move coordinates
        coords = np.where(self.board == move) # determine move coordinates
        return coords # return move coordinates


    def random_moves(self):
        """Returns a random, available, square number for the easy AI's desired move."""
        possible_moves = [] # declare an empty list of possible moves
        for row in self.board: # for each row in our gameboard,
            for square in row: # and for each square in said row,
                if square in self.values: # if the square's value is in our values list
                    possible_moves.append(square) # store it in our list of available squares
        move = random.choice(possible_moves) # determine a random, available move for AI
        return move # from our list of possible moves


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

    def swap_player_turn(self, player):
        """Swaps game control between two players."""
        return 'X' if player == 'O' else 'O'