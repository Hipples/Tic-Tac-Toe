import numpy as np
import random
from time import sleep
from tic_tac_toe import TicTacToe

class MiniMax:

    def __init__(self):
        self.player = ''
        self.opponent = ''
        self.match_records = "tic_tac_toe.txt"

        self.board = []
        self.board_record = []
        self.computer_record = []
        self.human_record =[]

        self.max_score = 10
        self.min_score = -10
        self.best_move = 0

        self.default = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.winning_patterns = [['1','2','3'],['4','5','6'],['7','8','9'],['1','4','7'],['2','5','8'],['3','6','9'],['1','5','9'],['3','5','7']]

    def create_board(self):
        for i in np.arange(1, 10).astype(str): # nine numbers, as strings, because we replace
            self.board.append(i) # the empty board numbers with Xs and Os (datatype consistency)
        self.board = np.reshape(self.board, (3, 3)) # shaped into 3 rows x 3 columns

    def can_win(self):
        for win in self.winning_patterns:
            if set(win) <= set(self.computer_record):
                return self.opponent
            if set(win) <= set(self.human_record):
                return self.player

    def full_board(self):
        if len(self.board_record) == 9:
            return True
        else:
            return False

    def get_open_squares(self):
        squares = []
        for row in list(set(self.default) - set(self.board_record)):
            squares.append(row)
        return squares

    def swap_player_turn(self):
        pass

    def minimax_logic(self, player, depth = 0):
        # 1. initiate max_score as -10 or 10
        if player == self.opponent:
            self.max_score = -10
        else: 
            self.max_score = 10
        # 2. if there are five+ board records, 
        if len(self.board_record) >= 5:
            # 2a. check for winning player
            result = self.can_win(player)
            # 2b. if winner is the computer
            if result == self.opponent: 
                return 10 + depth
            # 2c. if winner is the player
            if result == self.player:
                return -10 - depth
            # 2d. if board is full
            if self.full_board():
                return 0
        # 3. for each available move
        for move in self.get_open_squares():
            # 3a. if player is the computer
            if player == self.opponent:
                #3b. add move to the computer record
                self.computer_record.append(move)
            # 3c. otherwise    
            else:
                # 3d. add move to the human record
                self.human_record.append(move)
            # 3e. regardless, add the move to the board record    
            self.board_record.append(move)
            # 3f. then swap players
            player = self.swap_player_turn(player)
            # 3g. and recursively run this method again one depth greater
            score, _ = self.minimax_logic(player, depth + 1) 
            # 3h. before swapping players again
            player = self.swap_player_turn(player)
            # 3i. now, if player is the computer
            if player == self.opponent:
                # 3j. remove the last added move from the computer's record
                self.computer_record.pop()
            else:
                # 3k. otherwise, remove the last added move from the human's record
                self.human_record.pop()
            # 3l. regardless, remove the last added move to the board's record
            self.board_record.pop()
            # 3m. finally, if the current player is the computer
            if player == self.opponent:
                # 3n. and if the current score is greater than our max score
                if score > self.max_score:
                    # 3o. set our return variables
                    self.max_score = score 
                    self.best_move = move 
            # 3p. otherwise, if the current player is our human
            else :
                # 3q. and our score is lower than the max score
                if score < self.min_score:
                    # 3r. set our return variables
                    self.max_score = score 
                    self.best_move = move                    
        # 4. after everything, return our new max score and best possible, available, move!
        return self.max_score, self.best_move



    # def place_marker(self, player):
    #     pass

    def immediate_move(self):
        for win in self.winning_patterns:
            if len(list(set(win) - set(self.computer_record))) == 1:
                if len(list((set(win) - set(self.board_record)))) > 0:
                    move = list((set(win) - set(self.board_record)))[0]
                    return move
        else:
            for win in self.winning_patterns:
                if len(list(set(win) - set(self.human_record))) == 1:
                    if len(list((set(win) - set(self.board_record)))) > 0:
                        move = list((set(win) - set(self.board_record)))[0]
                        return move
            else:
                return False

    def minimax_move(self, player):
        if len(self.computer_record) == 0 and len(self.human_record) == 0:
            move = self.random_moves()
        elif len(self.board_record) == 0 and len(self.human_record) == 0:
            move = self.immediate_move()
            if move == False:
                _, move = self.minimax_logic(player)
        else:
            _, move = self.minimax_logic(player)
        move = str(move)
        coords = np.where(self.board == move)
        row, col = (int(coords[0])), (int(coords[1]))
        sleep(1)
        print(f"\n\tRandAI chooses square {move}!\n")
        with open(self.match_records, 'a') as record: 
            record.write(f"{player}:{move} ")
        self.place_marker(row, col, player)
        self.computer_record.append(move)
        self.board_record.append(move)

class MiniMaxAI(MiniMax):
    def __init__(self):
        super().__init__()

    # def assign_markers(self):
    #     pass
    # def coin_flip(self):
    #     pass
    # def display_board(self):
    #     pass
    # def player_move(self):
    #     pass
    # def is_winner(self):
    #     pass
    # def is_board_full(self):
    #     pass
    # def reset_board(self):
    #     pass
    # def replay(self):
    #     pass

    def game_mode_3(self):
        """TODO: method docstring...."""
        original_method = TicTacToe()
        # initiate replay loop
        while True:
            # 0. append 'New Game!' to tic_tac_toe.txt
            with open(self.match_records, 'a') as record:    
                record.write(f"\n\nNew Game!\n")
            # 1. create the gameboard
            self.create_board()
            # 2. assign markers based on choice
            self.player, self.opponent = original_method.assign_markers()
            # 3. randomly decide which player goes first
            if original_method.coin_flip() == 1:
                first_player = self.player
            else:
                first_player = self.opponent
            # 4. inform the players who won first turn
            print(f"\n\tPlayer {first_player} will go first!\n")
            # 5. display empty gameboard
            original_method.display_board()
            # 6a. if human player. . .
            if first_player == self.player:
                # input and make move
                original_method.player_move(first_player)
                print()
                # display updated gameboard
                original_method.display_board()
                # assign to current player
                current_player = self.player
            # 6b. if computer player. . .
            else:
                # generate and make random move
                self.minimax_move(first_player)
                print() 
                # display updated gameboard
                original_method.display_board()
                # assign to current player
                current_player = self.opponent            
            # 7. main game play loop
            while True:
                # 8. swap player turn
                current_player = self.swap_player_turn(current_player)
                # 9. display the current player
                print(f"\n\tPlayer {current_player}'s turn.\n")
                # 10a. if player is human, use player_move method
                if current_player == self.player:
                    original_method.player_move(current_player)
                # 10b. if player is a computer, use computer_move method
                else: 
                    self.minimax_move(current_player)                
                # 11a. check if there is a winner
                if original_method.is_winner(self.board, current_player):
                    print(f"\n\tPlayer {current_player} wins the game!\n")
                    # 11b. record the winner in tic_tac_toe.txt
                    with open(self.match_records, 'a') as record:    
                        record.write(f"\nPlayer {current_player} won the game!\n")
                    # 11c. game over
                    break                
                # 12a. check if there is a draw
                if original_method.is_board_full():
                    print("\n\tMatch draw!\n")
                    # 12b. record the draw status in tic_tac_toe.txt
                    with open(self.match_records, 'a') as record:
                        record.write("\nMatch was a draw!\n")
                    # 12c. game over
                    break                
                # 13. display updated gameboard
                original_method.display_board() 
            print()           
            # 14. final gameboard display
            original_method.display_board()
            print()            
            # 15. reset the gameboard
            original_method.reset_board()
            # 16. replay option
            if original_method.replay() == False:
                break

play = MiniMaxAI()
play.game_mode_3()