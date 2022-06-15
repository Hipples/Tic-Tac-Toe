import numpy as np
import random
from time import sleep
from game_objects import PlayerActions, AI

class TicTacToe:
    def __init__(self):
        pass
        

# OC
    def coin_flip(self):  # winner goes first
        """Randomly returns a value of either a 0 or 1."""
        return random.randint(0, 1)  # heads or tails?

# OC
    def swap_player_turn(self, player):
        """Swaps game control between two players."""
        return 'X' if player == 'O' else 'O'

# OC
    def replay(self):
        """Asks if main player would like to replay the current gamemode."""
        replay = input("\n\tWould you like to play again? (y/n): ")
        print()
        if replay.lower() == 'y':
            return True
        if replay.lower() == 'n':
            return False
        self.replay()

# modified to test refactoring        
    def game_mode_1(self):
        """Original PvP mode."""
        # initialize game objects from PlayerActions class
        action = PlayerActions()
        # initiate replay loop
        while True:
            # 0. append 'New Game!' to tic_tac_toe.txt
            with open(action.match_records, 'a') as record:
                record.write("\n\nNew Game!\n")
            # 1. create the gameboard
            action.create_board()
            # 2. assign player markers based on choice
            player, opponent = action.assign_markers()
            # 3. randomly decide which player goes first
            if self.coin_flip() == 1:
                first_player = player
            else:
                first_player = opponent
            # 4. inform the players who won first turn
            print(f"\n\tPlayer {first_player} will go first!\n")
            # 5. display empty gameboard
            action.display_board()
            # 6. input and make move
            action.player_move(first_player)
            print()
            # 7. display updated gameboard
            action.display_board()
            # 8. assign current_player as first_player
            current_player = first_player
            while True:
                # 9. swap player turn
                current_player = self.swap_player_turn(current_player)
                # 10. display whose turn to play
                print(f"\n\tPlayer {current_player}'s turn.\n")
                sleep(1)
                # 11. display updated gameboard
                action.display_board()
                # 12. capture and make player move
                action.player_move(current_player)
                print()
                # 13a. check if there is a winner
                if action.is_winner(action.board, current_player):
                    print(f"\n\tPlayer {current_player} wins the game!\n")
                    # 13b. record the winner in tic_tac_toe.txt
                    with open(action.match_records, 'a') as record:
                        record.write(f"\nPlayer {current_player} won the game!\n")
                    # 13c. game over
                    break
                # 14a. check if there is a draw
                if action.is_board_full():
                    print("\n\tMatch draw!\n")
                    # 14b. record the draw status in tic_tac_toe.txt
                    with open(action.match_records, 'a') as record:
                        record.write("\nMatch was a draw!\n")
                    # 14c. game over
                    break
                # 15. display updated gameboard
                action.display_board()
            print()
            # 16. final gameboard display
            action.display_board()
            print()
            # 17. reset gameboard
            action.reset_board()
            # 18. replay option
            if self.replay() == False:
                break

    def game_mode_2(self):
        """PvE Mode - Easy. Random AI opponent."""
        # initialize game objects from AI class
        ai = AI()
        # initiate replay loop
        while True:
            # 0. append 'New Game!' to tic_tac_toe.txt
            with open(ai.match_records, 'a') as record:
                record.write("\n\nNew Game!\n")
            # 1. create the gameboard
            ai.create_board()
            # 2. assign markers based on choice
            player, computer = ai.assign_markers()
            # 3. randomly decide which player goes first
            if self.coin_flip() == 1:
                first_player = player
            else:
                first_player = computer
            # 4. inform the players who won first turn
            print(f"\n\tPlayer {first_player} will go first!\n")
            # 5. display empty gameboard
            ai.display_board()
            # 6a. if human player. . .
            if first_player == player:
                # input and make move
                ai.player_move(first_player)
                print()
                # display updated gameboard
                ai.display_board()
                # assign to current player
                current_player = player
            # 6b. if computer player. . .
            else:
                # generate and make random move
                ai.random_move(first_player)
                print()
                # display updated gameboard
                ai.display_board()
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
                    ai.player_move(current_player)
                # 10b. if player is a computer, use computer_move method
                else:
                    ai.random_move(current_player)
                # 11a. check if there is a winner
                if ai.is_winner(ai.board, current_player):
                    print(f"\n\tPlayer {current_player} wins the game!\n")
                    # 11b. record the winner in tic_tac_toe.txt
                    with open(ai.match_records, 'a') as record:
                        record.write(f"\nPlayer {current_player} won the game!\n")
                    # 11c. game over
                    break
                # 12a. check if there is a draw
                if ai.is_board_full():
                    print("\n\tMatch draw!\n")
                    # 12b. record the draw status in tic_tac_toe.txt
                    with open(ai.match_records, 'a') as record:
                        record.write("\nMatch was a draw!\n")
                    # 12c. game over
                    break
                # 13. display updated gameboard
                ai.display_board()
            print()
            # 14. final gameboard display
            ai.display_board()
            print()
            # 15. reset the gameboard
            ai.reset_board()
            # 16. replay option
            if self.replay() == False:
                break

    def game_mode_3(self):
        """TODO: Create minimax AI gamemode"""
        pass


