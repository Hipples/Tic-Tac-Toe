
import numpy as np 
import random
from time import sleep
# import Trie 
# import GetHistory
# Tic Tac Toe, Three in a Row!
class TicTacToe:
    """Play a TicTacToe game!"""
    # initialize our class with -->
    def __init__(self):
        self.playerMarker = "X"
        self.computerMarker = "O"
        self.board = [] # an empty gameboard,
        self.boardRecord = []
        self.computerRecord = []
        self.humanRecord = []
        self.winList = [['1','2','3'],['4','5','6'],['7','8','9'],['1','4','7'],['2','5','8'],['3','6','9'],['1','5','9'],['3','5','7']]
        # self.histRecord = GetHistory.GetHistBoards()
        self.maxScore = 10
        self.drawScore = 0
        self.minScore = -10
        self.values = ['1', '2', '3', '4', '5', '6', '7', '8', '9'] # a list of empty squares,
        self.match_records = 'tic_tac_toe.txt' # and a file to keep record of player movements and match outcomes
        self.bestMove = 0
        # self.trie = Trie.Trie()
        # for h in self.histRecord:
        #     self.trie.insert(h)
    # create the gameboard -->
    def create_board(self):
        for i in np.arange(1, 10).astype(str): # nine numbers, as strings, because we replace
            self.board.append(i) # the empty board numbers with Xs and Os (datatype consistency)
        self.board = np.reshape(self.board, (3, 3)) # shaped into 3 rows x 3 columns

    # display the gameboard -->
    def display_board(self):
        print('\t-------------------------------')
        for row in self.board:
            print('\t|         |         |         |')
            print('\t|', end = '')
            for item in row:
                print(f'    {item}    |', end = '')
            print()
            print('\t|         |         |         |')
            print('\t-------------------------------') 

    # clear the gameboard -->
    def reset_board(self):
        self.board = [] # reset to an empty list
        self.boardRecord = []
        self.computerRecord= []
        self.humanRecord = []

    # enable the player to choose Xs or Os -->
    def choose_marker(self):
        marker = ' ' # declare marker variable as empty string
        while (marker != 'X' and marker != 'O'): # while marker does not equal X or O
            marker = input("\n\tDo you want to be Xs or Os? ").upper() # ask player to choose X or O
        if marker == 'X': # if X, 
            self.playerMarker,self.computerMarker = 'X','O'
            return ['X', 'O'] # then return X, O
        else: # if O, 
            self.playerMarker,self.computerMarker = 'O','X'
            return ['O', 'X'] # then return O, X

    # assign the player markers -->
    def assign_markers(self): # retrieve marker order from choose_marker() method
        player, opponent = self.choose_marker() # assign the first char returned to our player, 
        return player, opponent # and the second char to our player's opponent 

    # decide which player goes first -->
    def coin_flip(self): # winner goes first
        return random.randint(0, 1) # heads or tails?

    # determine player move -->
    def human_moves(self, player):
        move = input(f"\n\tPlease enter the square number where you'd like to place your {player}: ")
        print(f"\n\tYou chose square {move}!") # acquire player input to determine desired move
        return move # return chosen square number

    # determine coordinates of player move -->
    def get_coords(self, player):
        move = self.human_moves(player) # retrieve player move from human_moves() method
        coords = [] # declare empty list to store move coordinates
        coords = np.where(self.board == move) # determine move coordinates
        return coords # return move coordinates
    def getPossibleMove(self):
        moves = []
        for row in list(set(self.values) - set(self.boardRecord)): # for each row in our gameboard,
            moves.append(row) # store it in our list of available squares
        return moves
          
    def MinMax_Moves(self,player, depth = 0):
        # print("===============================")
        if player == self.computerMarker:
            self.maxScore = -10
        else: self.maxScore = 10
        # possible_moves = [] # declare an empty list of possible moves
        # for row in self.values: # for each row in our gameboard,
        #     if row not in self.boardRecord: # if the square's value equals a number from our values list
        #         possible_moves.append(row) # store it in our list of available squares
        # #move = random.choice(possible_moves) # determine move by randomly choosing an available square
        if len(self.boardRecord)>=5:
            res = self.IsWin( player)
            if res ==self.computerMarker:
                return 10 + depth,None
            elif res == self.playerMarker:
                return -10 - depth,None
            else:
                if self.isboardfull():
                    return 0,None 
        for move in self.getPossibleMove():
            # move = int(move)
            if player ==self.computerMarker:
                self.computerRecord.append(move)
            else:
                self.humanRecord.append(move)    
            self.boardRecord.append(move)
            player = self.swap_player_turn(player)
            score,_ = self.MinMax_Moves(player, depth+1)
            player = self.swap_player_turn(player)
            if player ==self.computerMarker:
                self.computerRecord.pop()
            else:
                self.humanRecord.pop()
            self.boardRecord.pop()
            if player ==self.computerMarker:
                if score > self.maxScore:
                    self.maxScore = score 
                    self.bestMove = move 
            else :
                if score < self.maxScore:
                    self.maxScore = score 
                    self.bestMove = move                    

        return self.maxScore, self.bestMove # from our list of possible moves

    # determine Random AI moves -->
    def random_moves(self):
        possible_moves = [] # declare an empty list of possible moves
        for row in self.board: # for each row in our gameboard,
            for square in row: # and for each square in said row, 
                if square in self.values: # if the square's value equals a number from our values list
                    possible_moves.append(square) # store it in our list of available squares
        move = random.choice(possible_moves) # determine move by randomly choosing an available square
        return move # from our list of possible moves

    # record player moves on the gameboard -->
    def place_marker(self, row, col, player):
        self.board[row][col] = player # use move coordinates to place marker in the chosen square

    # capture player move while handling exceptions -->
    def player_move(self, player):
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
                self.humanRecord.append(move)
                self.boardRecord.append(move)
                return False # before ending our loop
    def immediateMove(self):
        for w in self.winList:
            if len(list(set(w)-set(self.computerRecord))) ==1 :
                if len(list((set(w)-set(self.boardRecord))))>0:
                    move =  list((set(w)-set(self.boardRecord)))[0]
                    return move
        else:
            for w in self.winList:   
                if  len(list(set(w)-set(self.humanRecord))) ==1:
                    if len(list((set(w)-set(self.boardRecord))))>0:
                        move =  list((set(w)-set(self.boardRecord)))[0]
                        return move      
            else: return False
    # capture Random AI moves -->
    def computer_move(self, player):
        # index = len(self.computerRecord)
        # if index == 2:
        if len(self.computerRecord) ==0 and len(self.humanRecord) ==0:
            move = self.random_moves()
        elif len(self.boardRecord)>=3:
            move = self.immediateMove()
            if(move == False):  
                _,move = self.MinMax_Moves(player)
        else: 
            _,move = self.MinMax_Moves(player)
        move = str(move)
        # move = self.random_moves() # get randomly generate move from random_moves() method
        coords = np.where(self.board == move) # set the move coordinates
        row, col = (int(coords[0])), (int(coords[1])) # assign the proper index of the move
        # sleep(2) # (our AI is thinking. . .)
        print(f"\n\tRandAI chooses square {move}!\n") # announce RandAI's move
        with open(self.match_records, 'a') as record: # open our match records and 
            record.write(f"{player}:{move} ") # append each Random AI move
        self.place_marker(row, col, player) # as it happens
        self.computerRecord.append(move)
        self.boardRecord.append(move)
    
    def isboardfull(self):
        if len(self.boardRecord) == 9:
            return True
        else:
            return False
    # determine if the gameboard is full -->
    def is_board_full(self):
        for row in self.board: # for each row on the board, 
            for square in row: # and for each square in said row, 
                if (square) in self.values: # if the square value equals a value from our list of empty squares
                    return False # return False
        return True # otherwise return True

    # determine if there is a winner -->           
    def is_winner(self, board, player):
        win = None
        # check rows for win
        for row in range(3):
            if board[row][0] == board[row][1] and board[row][1] == board[row][2]:
                if board[row][0] == player:
                    win = True
            if(win):
                return(win)
        # check columns for win
        for col in range(3):
            if board[0][col] == board[1][col] and board[1][col] == board[2][col]:
                if board[0][col] == player:
                    win = True
            if(win):
                return(win)
        # check descending diagonal for win
        if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
            if board[0][0] == player:
                win = True
        if(win):
            return(win)
        # check ascending diagonal for win
        if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
            if board[0][2] == player:
                win = True
        if(win):
            return(win)
    def IsWin(self, player): # this is used to find out the winner
        for w in self.winList:
            if set(w)<=set(self.computerRecord):
                return self.computerMarker
            if set(w)<=set(self.humanRecord):
                return self.playerMarker

    # method to swap turns between players
    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'      
    # method designed to enable replay at end of round   
    def replay(self):
        replay = input("\n\tWould you like to play again? (y/n) ")
        print()
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
            # 0. append 'New Game!' to tic_tac_toe.txt
            with open(self.match_records, 'a') as record:    
                record.write(f"\n\nNew Game!\n")
            # 1. create the gameboard
            self.create_board()            
            # 2. assign markers based on choice
            player, computer = self.assign_markers()
            self.playerMarker =player   
            self.computerMarker = computer
            # 3. randomly decide which player goes first
            if self.coin_flip() == 1:
                first_player = player
            else:
                first_player = computer
            # 4. inform the players who won first turn
            # self.boardRecord.append(first_player)


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

    
    # PvP mode gameplay loop
    def game_mode_1_PvP(self):
        """Play Tic Tac Toe (Mode 1: Player vs Player)!"""
        # initiate reply loop
        while True:
            # 0. append 'New Game!' to tic_tac_toe.txt
            with open(self.match_records, 'a') as record:    
                record.write(f"\n\nNew Game!\n")
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

import ttt_menus


# class objects
menus = ttt_menus.TTTMenus()
Xs_and_Os = TicTacToe()

def startup():
    while True:
        menus.display_welcome_screen()
        game_mode = ' '
        try:
            game_mode = int(menus.get_player_selection())
        except ValueError:
            print("\n\tInvalid input. Please enter 1 2 or 3.\n")
        except KeyboardInterrupt:
            print("\n\tGood bye!\n")
        else:
            if(game_mode == 1): 
                Xs_and_Os.game_mode_1_PvP()
                break
            elif(game_mode == 2): 
                Xs_and_Os.game_mode_2_PvE()
                break
            elif(game_mode == 3):
                print("\n\tGood bye!\n")
                exit()
        return True
        
def game_over():
    while True:
        menus.display_game_over_screen()
        try:
            selection = int(menus.get_player_selection())
        except ValueError:
            print("\n\tInvalid input. Please enter 1 or 2.\n")
        except KeyboardInterrupt:
            print("\n\n\tGood bye!\n")
            exit()
        else:
            if(selection == 1): 
                startup()
            if(selection == 2):
                print("\n\tGood bye!\n")
                exit()

# driver code
startup()
print()
game_over()