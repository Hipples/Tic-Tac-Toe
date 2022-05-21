import numpy as np
import random

# Tic Tac Toe, Three in a Row!
class TicTacToe:
    """Play a TicTacToe game!"""
    # initialize the game with our board as an empty list
    def __init__(self):
        self.board = []
    # method to create the gameboard
    def create_board(self):
        for i in np.arange(1, 10).astype(str):
            self.board.append(i)
        self.board = np.reshape(self.board, (3, 3))
    # method to display the gameboard
    def display_board(self):
        print('\t-------------------------------')
        for row in self.board:
            print('\t|         |         |         | ')
            print('\t|', end = '')
            for item in row:
                print(f'    {item}    |', end = '')
            print()
            print('\t|         |         |         |')
            print('\t-------------------------------')
    # method to determine is gameboard is full
    def is_board_full(self):
        for row in self.board:
            for item in row:
                if (item) in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    return False
        return True
    # method to enable the player to choose to be Xs or Os 
    def choose_marker(self):
        marker = ' '
        while (marker != 'X' and marker != 'O'):
            marker = input("\n\tDo you want to be Xs or Os? ").upper()
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
    # method to get coordinates of the square player chooses each turn
    def get_coords(self, player):
        value = input(f"\n\tPlease enter the square number where you'd like to place your {player}: ")
        coords = []
        coords = np.where(self.board == value)
        return coords
    # method to place current player marker each turn
    def place_marker(self, row, col, player):
        self.board[row][col] = player
    # method to swap turns during gameplay
    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'
    # method to determine if there is a winner each turn
    def player_won(self, board, player):
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
        if (board[0][0] == board[1][1] and board[1][1] == board[2][2]):
            if (board[0][0] == player):
                win = True
        if win:
            return win
        # check ascending diagonal for win
        if (board[0][2] == board[1][1] and board[1][1] == board[2][0]):
            if(board[0][2]) == player:
                win = True
        if win:
            return win

    # main gameplay loop for PvP mode
    def play_game_1(self):
        """Play Tic Tac Toe (Mode 1: Player vs Player)!"""
        # create the gameboard
        self.create_board()            
        # assign player markers based on choice
        player, opponent = self.assign_markers()    
        # randomly decide which player goes first
        if self.coin_flip() == 1:
            current_player = player
        else:
            current_player = opponent
        # begin gameplay loop
        while True: 
            # 1. display whose turn to play 
            print(f"\n\tPlayer {current_player}'s turn.\n") 
            # 2. display current gameboard
            self.display_board() 
            # 3. capture player move
            coords = self.get_coords(current_player)
            try: 
                row, col = int(coords[0]), int(coords[1])
            except TypeError:
                print("\n\tWrong input! Try again.\n")
                continue

            print() # make some space

            # 4. place current player's marker on gameboard
            self.place_marker(row, col, current_player) 
            # 5. check for wins after each player turn
            if self.player_won(self.board, current_player):
                print(f"\n\tPlayer {current_player} wins the game!\n")
                break
            # 6. check for draw after each player turn
            if self.is_board_full():
                print("\n\tMatch draw!\n")
                break
            # 7. swap player turns
            current_player = self.swap_player_turn(current_player)
        # display final view of gameboard
        print()
        self.display_board()

# allows game to be ran from CLI via command: >>>python TicTacToe.py
game = TicTacToe()
game.play_game_1() # labeled as game_1 due to future plans to include more than one gamemode option