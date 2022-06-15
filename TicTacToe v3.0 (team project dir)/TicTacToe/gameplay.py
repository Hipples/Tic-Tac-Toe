import numpy as np
import random
from time import sleep
from boards import TicTacToeBoard
from players import AI, Players

P = Players()
B = TicTacToeBoard()

class TicTacToe:
    def __init__(self):
        self.match_records = "tic_tac_toe.txt"

    def coin_flip(self):  # winner goes first
        """Randomly returns a value of either a 0 or 1."""
        return random.randint(0, 1)  # heads or tails?

    def swap_player_turn(self, player):
        """Swaps game control between two players."""
        return 'X' if player == 'O' else 'O'

    def replay(self):
        """Asks if main player would like to replay the current gamemode."""
        replay = input("\n\tWould you like to play again? (y/n) ")
        print()
        if replay.lower() == 'y':
            return True
        if replay.lower() == 'n':
            return False
        self.replay()
        
    def game_mode_1(self):
        """Original PvP mode gameplay loop (player selection 1)."""
        # initiate replay loop
        while True:
            # 0. append 'New Game!' to tic_tac_toe.txt
            with open(self.match_records, 'a') as record:
                record.write("\n\nNew Game!\n")
            # 1. create the gameboard
            B.create_board()
            # 2. assign player markers based on choice
            player, opponent = P.assign_markers()
            # 3. randomly decide which player goes first
            if self.coin_flip() == 1:
                first_player = player
            else:
                first_player = opponent
            # 4. inform the players who won first turn
            print(f"\n\tPlayer {first_player} will go first!\n")
            # 5. display empty gameboard
            B.display_board()
            # 6. input and make move
            P.player_move(first_player)
            print()
            # 7. display updated gameboard
            B.display_board()
            # 8. assign current_player as first_player
            current_player = first_player
            while True:
                # 9. swap player turn
                current_player = self.swap_player_turn(current_player)
                # 10. display whose turn to play
                print(f"\n\tPlayer {current_player}'s turn.\n")
                sleep(1)
                # 11. display updated gameboard
                B.display_board()
                # 12. capture and make player move
                P.player_move(current_player)
                print()
                # 13a. check if there is a winner
                if B.is_winner(B.board, current_player):
                    print(f"\n\tPlayer {current_player} wins the game!\n")
                    # 13b. record the winner in tic_tac_toe.txt
                    with open(self.match_records, 'a') as record:
                        record.write(f"\nPlayer {current_player} won the game!\n")
                    # 13c. game over
                    break
                # 14a. check if there is a draw
                if B.is_board_full():
                    print("\n\tMatch draw!\n")
                    # 14b. record the draw status in tic_tac_toe.txt
                    with open(self.match_records, 'a') as record:
                        record.write("\nMatch was a draw!\n")
                    # 14c. game over
                    break
                # 15. display updated gameboard
                B.display_board()
            print()
            # 16. final gameboard display
            B.display_board()
            print()
            # 17. reset gameboard
            B.reset_board()
            # 18. replay option
            if self.replay() == False:
                break

    def game_mode_2(self, board_option):
        """PvE Mode - Easy. Random AI opponent."""
        # initiate replay loop
        while True:
            # 0. append 'New Game!' to tic_tac_toe.txt
            with open(self.match_records, 'a') as record:
                record.write("\n\nNew Game!\n")
            # 1. create the gameboard
            B.create_board()
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

    def game_mode_3(self, board_option):
        """TODO: Create minimax AI gamemode"""
        pass


