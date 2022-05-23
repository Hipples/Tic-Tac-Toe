import numpy as np
import random

# Tic Tac Toe, Three in a Row!
class TicTacToe:
    """Play a TicTacToe game!"""
    # initialize the game with our board as an empty list and the values for it
    def __init__(self):
        self.board = []
        self.values = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    # method to create the gameboard
    def create_board(self):
        for i in np.arange(1, 10).astype(str):
            self.board.append(i)
        self.board = np.reshape(self.board, (3, 3))
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
    # method to clear board at game over
    def reset_board(self):
        self.board = []
    # method to determine if there is a winner each turn             
    def is_winner(self, board, player):
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
            if(board[0][col] == board[1][col] and board[1][col] == board[2][col]):
                if(board[0][col] == player):
                    win = True
            if(win):
                return(win)
        # check descending diagonal for win
        if(board[0][0] == board[1][1] and board[1][1] == board[2][2]):
            if(board[0][0] == player):
                win = True
        if(win):
            return(win)
        # check ascending diagonal for win
        if(board[0][2] == board[1][1] and board[1][1] == board[2][0]):
            if(board[0][2]) == player:
                win = True
        if(win):
            return(win)
    # method to get coordinates of square to place marker
    def get_coords(self, player):
        value = input(f"\n\tPlease enter the square number where you'd like to place your {player}: ")
        print(f"\n\tYou chose square {value}!")
        coords = []
        coords = np.where(self.board == value)
        return coords
    # method to place marker
    def place_marker(self, row, col, player):
        self.board[row][col] = player
    # method for human player move
    def player_move(self, player):
        while True:
            try:
                coords = self.get_coords(player)
                row, col = int(coords[0]), int(coords[1])
            except KeyboardInterrupt:
                print("\n\n\tGood bye!")
                exit()
            except:
                print("\n\tWrong input! Try again.\n")
            else:
                self.place_marker(row, col, player)
                return False
    # method for AI movement
    def computer_move(self, player):
        move = self.random_move()
        coords = np.where(self.board == move)
        row, col = (int(coords[0])), (int(coords[1]))
        print(f"\n\tRandAI chooses square {move}!\n")
        self.place_marker(row, col, player)
    # method to implement a Random AI opponent 
    def random_move(self):
        possible_moves = []
        for row in self.board:
            for square in row:
                if square in self.values:
                    possible_moves.append(square)       
        move = random.choice(possible_moves)
        return move
    # method to determine is gameboard is full
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
        player, opponent = self.choose_marker()
        return player, opponent
    # method to randomly decide who goes first
    def coin_flip(self):
        return random.randint(0, 1)
    # method to swap turns during gameplay
    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'      
    # method designed to enable replay at end of round   
    def replay(self):
        replay = input("\n\tWould you like to play again? (y/n) ")
        if replay.lower() == 'y':
            return True
        elif replay.lower() == 'n':
            return False
        else:
            self.replay()          

    # PvE (easy) mode gameplay loop
    def game_mode_2_PvE(self):
        """Play Tic Tac Toe (Mode 2: PvE (random AI))"""
        # initiate replay loop
        while True:
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
                # 11. check if there is a winner
                if self.is_winner(self.board, current_player):
                    print(f"\n\tPlayer {current_player} wins the game!\n")
                    break # if so, game over
                # 12. check if there is a draw
                if self.is_board_full():
                    print("\n\tMatch draw!\n")
                    break # if so, game over
                # 13. display updated gameboard
                self.display_board() 
            print()
            # 14. final gameboard display
            self.display_board()
            print()
            # 15. replay option
            if self.replay() == False:
                break
            else:
                self.reset_board()
    
    ## needs updating ##
            
    # PvP mode gameplay loop
    def game_mode_1_PvP(self):
        """Play Tic Tac Toe (Mode 1: Player vs Player)!"""
        # 1. create the gameboard
        self.create_board()            
        # 2. assign player markers based on choice
        player, opponent = self.assign_markers()    
        # 3. randomly decide which player goes first
        if self.coin_flip() == 1:
            current_player = player
        else:
            current_player = opponent
        # 4. begin gameplay loop
        while True: 
            # 5. display whose turn to play 
            print(f"\n\tPlayer {current_player}'s turn.\n") 
            # 6. display updated gameboard
            self.display_board() 
            # 7. capture and make player move
            self.player_move(current_player)
            # just making some extra space
            print() 
            # 8. check for wins after each player turn
            if self.is_winner(self.board, current_player):
                print(f"\n\tPlayer {current_player} wins the game!\n")
                break # game over
            # 9. check for draw after each player turn
            if self.is_board_full():
                print("\n\tMatch draw!\n")
                break # game over
            # 10. swap player turns
            current_player = self.swap_player_turn(current_player)
        print()
        # game over - display final view of gameboard
        self.display_board()
        self.reset_board()