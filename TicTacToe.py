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
        for i in np.arange(1, 10).astype(str):
            self.board.append(i)
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
    # method to determine is gameboard is full
    def is_board_full(self):
        for row in self.board:
            for item in row:
                if int(item) not in range(1-10):
                    return False
        return True
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
    # method to get coordinates of the square player chooses each turn
    def get_coords(self, player):
        value = input(f"\nPlease enter the square number where you'd like to place your {player}: ")
        coords = []
        coords = np.where(self.board == value)
        return coords
    # method to place current player marker each turn
    def place_marker(self, row, col, player):
        self.board[row][col] = player
    # method to swap turns during gameplay
    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'


    def player_won(self, player):
        # check rows for win
        win = None
        squares = len(self.board)
        for row in range(squares):
            win = True
            for col in range(squares):
                if self.board[row][col] != player:
                    win = False
                    break
            if win:
                return win
        # check columns for win
        for row in range(squares):
            win = True
            for col in range(squares):
                if self.board[col][row] != player:
                    win = False
                    break
            if win:
                return win
        # check diagonals for win
        win = True
        for row in range(squares):
            if self.board[row][row] != player:
                win = False
                break
            if win:
                return win
        win = True
        for row in range(squares):
            if self.board[row][squares - 1 - row] != player:
                win = False
                break
            if win:
                return win
            return False


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
            print(f"\nPlayer {current_player}'s turn.\n") 

            # 2. display current gameboard
            self.display_board() 

            # 3. capture player move
            coords = self.get_coords(current_player)
            row, col = int(coords[0]), int(coords[1])

            print() # make some space

            # 4. place current player's marker on gameboard
            self.place_marker(row, col, current_player) 

            # 5. check for wins after each player turn
            if self.player_won(current_player):
                print(f"\nPlayer {current_player} wins the game!\n")
                break

            # 6. check for draw after each player turn
            if self.is_board_full():
                print("Match draw!")
                break

            # 7. swap player turns
            current_player = self.swap_player_turn(current_player)

        # display final view of gameboard
        print()
        self.display_board()

# test
game = TicTacToe()
game.play_game_1()



    # def game_mode(self, selection):
    #     """Enable player selection between three game modes (PvP, PvRandom, PvGenius)"""
    #     while selection != 1 and selection !=2 and selection !=3:
    #         selection = int(input("Please enter 1, 2, or 3 to select your : "))
    #         match selection:
    #             case 1: 
    #                 print("Game Mode: Player vs Player!")
    #                 break
    #             case 2:
    #                 print("Game Mode: Player vs Random AI!")
    #                 break
    #             case 3:
    #                 print("Game Mode: Player vs Genius AI!")
    #                 break


    # def evaluate(self, board):
    #     """Evaluate the current gameboard status."""
    #     # check all rows for a victory 
    #     for row in range(3):
    #         if(board[row][0]) == board[row][1] and board[row][1] == board[row][2]:
    #             if (board[row][0] == self.player):
    #                 return 10
    #             elif (board[row][0] == self.opponent):
    #                 return -10
    #     # check all columns for a victory
    #     for column in range(3):
    #         if (board[0][column] == board[1][column] and board[1][column] == board[2][column]):
    #             if (board[0][column] == self.player):
    #                 return 10
    #             elif (board[0][column] == self.opponent):
    #                 return -10
    #     # check the two diagonals for a victory
    #     # descending diagonal
    #     if (board[0][0] == board[1][1] and board[1][1] == board[2][2]):
    #         if (board[0][0] == self.player): 
    #             return 10
    #         elif (board[0][0] == self.opponent):
    #             return -10
    #     # ascending diagonal
    #     if (board[0][2] == board[1][1] and board[1][1] == board[2][0]):
    #         if (board[0][2] == self.player): 
    #             return 10
    #         elif(board[0][2] == self.opponent):
    #             return -10
    #     # otherwise return 0
    #     return 0  
            
