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


































# Ignore notes below for future versions: 

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
            
