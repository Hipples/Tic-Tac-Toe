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
            
