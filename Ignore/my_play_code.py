import numpy as np
import random

# Tic Tac Toe, Three in a Row!
class TicTacToe:
    """Play a TicTacToe game!"""

    # initialize the game with our board as an empty list, followed by the values to fill it
    def __init__(self):
        self.board = []
        self.values = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

# 0. comparing methods between random_AI_example_3 and my baseline PvP code    
# 1. board = [' ' for x in range(10)]

    # my method to create the gameboard
    def create_board(self):
        for i in np.arange(1, 10).astype(str):
            self.board.append(i)
        self.board = np.reshape(self.board, (3, 3))

# 2. def insertLetter(letter, pos):
#       board[pos] = letter

    # my method to place current player marker each turn
    def place_marker(self, row, col, player):
        self.board[row][col] = player

# 3. def spaceIsFree(pos):
#        return board[pos] == ' '

    # may need to create this one. . .
    def is_move_available(self, row, col):
        move = self.board[row][col]
        for row in self.board:
            for item in row:
                if move == item:
                    return True
                return False

# 4. def printBoard(board):
#       print('   |   |')
#       print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
#       print('   |   |')
#       print('-----------')
#       print('   |   |')
#       print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
#       print('   |   |')
#       print('-----------')
#       print('   |   |')
#       print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
#       print('   |   |')

    # my method to display the gameboard
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

# 5. def isWinner(bo, le):
#     return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or(bo[1] == le and bo[2] == le and bo[3] == le) or(bo[1] == le and bo[4] == le and bo[7] == le) or(bo[2] == le and bo[5] == le and bo[8] == le) or(bo[3] == le and bo[6] == le and bo[9] == le) or(bo[1] == le and bo[5] == le and bo[9] == le) or(bo[3] == le and bo[5] == le and bo[7] == le)

# my method to determine if there is a winner each turn
    def player_won(self, board, player):
        win = None
        # check rows for win
        for row in range(3):
            if board[row][0] == board[row][1] and board[row][1] == board[row][2]:
                if board[row][0] == player:
                    win = True
            if win:
                return(win)
        # check columns for win
        for col in range(3):
            if board[0][col] == board[1][col] and board[1][col] == board[2][col]:
                if board[0][col] == player:
                    win = True
            if win:
                return(win)
        # check descending diagonal for win
        if (board[0][0] == board[1][1] and board[1][1] == board[2][2]):
            if (board[0][0] == player):
                win = True
        if (win):
            return(win)
        # check ascending diagonal for win
        if (board[0][2] == board[1][1] and board[1][1] == board[2][0]):
            if(board[0][2]) == player:
                win = True
        if (win):
            return(win)

# 6. def playerMove():
#        run = True
#        while run:
#            move = input('Please select a position to place an \'X\' (1-9): ')
#            try:
#                move = int(move)
#                if move > 0 and move < 10:
#                    if spaceIsFree(move):
#                        run = False
#                        insertLetter('X', move)
#                    else:
#                        print('Sorry, this space is occupied!')
#                else:
#                    print('Please type a number within the range!')
#            except:
#                print('Please type a number!')

    # my method to get coordinates of the square player chooses each turn
    def get_coords(self, player):
        value = input(f"\n\tPlease enter the square number where you'd like to place your {player}: ")
        coords = []
        coords = np.where(self.board == value)
        return coords

    # # 3. capture player move ((this is a part of my main gameplay loop))
    # coords = self.get_coords(current_player)
    # try: 
    #     row, col = int(coords[0]), int(coords[1])
    # except TypeError:
    #     print("\n\tWrong input! Try again.\n")
    #     continue
    # # 4. place current player's marker on gameboard
    # self.place_marker(row, col, current_player) 
    # print() # make some space

    def player_move(self, player):
        coords = self.get_coords(player)
        try:
            row, col = int(coords[0]), int(coords[1])
        except:
            print("\n\tWrong input! Try again.\n")
        else:
            self.place_marker(row, col, player)

    def computer_move(self, player):
        move = self.random_move()
        if move == 0:
            print("\n\tMatch Draw!\n")
        else:
            coords = np.where(self.board == move)
            row, col = (coords[0]), (coords[1])
            self.place_marker(row, col, player)
    # method to implement a Random AI opponent 
    def random_move(self):
        possible_moves = []
        for row in self.board:
            for square in row:
                if square in self.values:
                    if square != 0:
                        possible_moves.append(square)       
        move = 0 
        for marker in ['O', 'X']:
            for square in possible_moves:
                board_copy = self.board[:]
                board_copy[int(square)] = marker
                if self.player_won(board_copy, marker):
                    move = square
                    return move
        free_corners = []
        for square in possible_moves:
            if square in [1,3,7,9]:
                free_corners.append(square)            
        if len(free_corners) > 0:
            move = self.select_random(free_corners)
            return move
        if 5 in possible_moves:
            move = 5
            return move
        open_edges = []
        for square in possible_moves:
            if square in [2,4,6,8]:
                open_edges.append(square)           
        if len(open_edges) > 0:
            move = self.select_random(open_edges)
        return move

    # my select random method
    def select_random(self, moves):
        count = len(moves)
        choice = random.randrange(0, count)
        return moves[choice]

# 9.
# def isBoardFull(board):
#     if board.count(' ') > 1:
#         return False
#     else:
#         return True

    # my method to determine is gameboard is full
    def is_board_full(self):
        for row in self.board:
            for item in row:
                if (item) in self.values:
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
    # method to swap turns during gameplay
    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'            





    # PvE (easy) mode gameplay loop
    def play_game_2(self):
        # create the gameboard
        self.create_board()            
        # assign player markers based on choice
        player, computer = self.assign_markers()    
        # randomly decide which player goes first
        if self.coin_flip() == 1:
            first_player = player
        else:
            first_player = computer
        # inform the player who won first turn
        print(f"\n\tPlayer {first_player} will go first!\n") 
        self.display_board()
        # if human player. . .
        if first_player == player:
            self.player_move(first_player)
            self.display_board()
            current_player = player
        # if computer player. . .
        else:
            self.computer_move(first_player) 
            self.display_board()
            current_player = computer
        # main game play loop
        while True:
            # swap player turn
            current_player = self.swap_player_turn(current_player)
            # display current player
            print(f"\n\tPlayer {current_player}'s turn.\n") 
            # display current gameboard
            self.display_board() 
            # if current player is human, input move & place marker
            if current_player == player:
                self.player_move(current_player)
            else: # if current player is a computer
                self.computer_move(current_player)
            # check if current player won the game with their last move
            if self.player_won(self.board, current_player):
                print(f"\n\tPlayer {current_player} wins the game!\n")
                break # if so, game over
            # check if the last move caused a draw
            if self.is_board_full():
                print("\n\tMatch draw!\n")
                break # if so, game over    
        print()
        # final gameboard display
        self.display_board()        
            




    # PvP mode gameplay loop
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
            # just making some extra space
            print() 
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
game.play_game_2() 