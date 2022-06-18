"""This game module contains the gameplay loop logic necessary to run a smooth Tic Tac Toe match in a variety of game modes."""

import random
from time import sleep
from game_objects import PlayerActions, AI

class TicTacToe:
    """game's TicTacToe class contains the following methods:
            - coin_flip()       x. used to randomly decide first player
            - replay()          x. used to offer instant replay of same game mode
            - game_mode_1()     x. Player vs Player game loop
            - game_mode_2()     x. Player vs Random AI game loop
            - game_mode_3()     x. Player vs MiniMax AI game loop
    """
    def __init__(self, mode, board_option):
        self.mode = mode
        self.board_option = board_option

    def coin_flip(self):  # winner goes first
        """Returns either 0 or 1, randomly."""
        return random.randint(0, 1)  # heads or tails?

    def replay(self):
        """Asks if main player would like to replay the current gamemode. Returns True or False."""
        replay = input("\n\tWould you like to play again? (y/n): ")
        print()
        if replay.lower() == 'y':
            return True
        if replay.lower() == 'n':
            return False
  
    def game_one(self):
        """Classic PvP Mode. Game loop."""
        # initialize game objects from PlayerActions class
        action = PlayerActions()
        # initiate replay loop
        while True:
            # 0. append 'New Game!' to tic_tac_toe.txt
            with open(action.match_records, 'a') as record:
                record.write("\n\nPlayer vs Player! Game on!\n")
            # 1. create the gameboard
            action.create_board(self.board_option)
            # 2. assign player markers based on choice
            action.player, action.opponent = action.assign_markers()
            # 3. randomly decide which player goes first
            if self.coin_flip() == 1:
                first_player = action.player
            else:
                first_player = action.opponent
            # 4. inform the players who won first turn
            print(f"\n\tPlayer {first_player} will go first!\n")
            # 5. display starting gameboard
            action.display_board(self.board_option)
            # 6. input and make move
            action.player_move(first_player)
            print()
            # 7. display updated gameboard
            action.display_board()
            # 8. assign current_player as first_player
            current_player = first_player
            while True:
                # 9. swap player turn
                current_player = action.swap_player_turn(current_player)
                # 10. display whose turn to play
                print(f"\n\tPlayer {current_player}'s turn.\n")
                sleep(1)
                # 11. display updated gameboard
                action.display_board(self.board_option)
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

    def game_two(self):
        """PvE Mode - Easy. Random AI opponent. Game loop."""
        # initialize game objects from AI class
        ai = AI()
        # initiate replay loop
        while True:
            # 0. append 'New Game!' to tic_tac_toe.txt
            with open(ai.match_records, 'a') as record:
                record.write("\n\nPlayer vs Random AI! Game on!\n")
            # 1. create the gameboard
            ai.create_board()
            # 2. assign markers based on choice
            ai.player, ai.opponent = ai.assign_markers()
            # 3. randomly decide which player goes first
            if self.coin_flip() == 1:
                first_player = ai.player
            else:
                first_player = ai.opponent
            # 4. inform the players who won first turn
            print(f"\n\tPlayer {first_player} will go first!\n")
            # 5. display empty gameboard
            ai.display_board()
            # 6a. if human player. . .
            if first_player == ai.player:
                # input and make move
                ai.player_move(first_player)
                print()
                # display updated gameboard
                ai.display_board()
                # assign to current player
                current_player = ai.player
            # 6b. if computer player. . .
            else:
                # generate and make random move
                ai.random_move(first_player)
                print()
                # display updated gameboard
                ai.display_board()
                # assign to current player
                current_player = ai.opponent
            # 7. main game play loop
            while True:
                # 8. swap player turn
                current_player = ai.swap_player_turn(current_player)
                # 9. display the current player
                print(f"\n\tPlayer {current_player}'s turn.\n")
                # 10a. if player is human, use player_move method
                if current_player == ai.player:
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

    def game_three(self):
        """PvE Mode - Hard. Minimax AI opponent. Game loop."""
        # initialize game objects from AI class
        ai = AI()
        # initiate replay loop
        while True:
            # 0. append 'New Game!' to tic_tac_toe.txt
            with open(ai.match_records, 'a') as record:    
                record.write(f"\n\nPlayer vs MiniMax AI! Game on!\n")
            # 1. create the gameboard
            ai.create_board(self.board_option)
            # 2. assign markers based on choice
            ai.player, ai.opponent = ai.assign_markers()
            # 3. randomly decide which player goes first
            if self.coin_flip() == 1:
                first_player = ai.player
            else:
                first_player = ai.opponent
            # 4. inform the players who won first turn
            print(f"\n\tPlayer {first_player} will go first!\n")
            # 5. display empty gameboard
            ai.display_board(self.board_option)
            # 6a. if human player. . .
            if first_player == ai.player:
                # input and make move
                ai.player_move(first_player)
                print()
                # display updated gameboard
                ai.display_board(self.board_option)
                # assign to current player
                current_player = ai.player
            # 6b. if computer player. . .
            else:
                # generate and make random move
                ai.minimax_move(first_player)
                print() 
                # display updated gameboard
                ai.display_board(self.board_option)
                # assign to current player
                current_player = ai.opponent            
            # 7. main game play loop
            while True:
                # 8. swap player turn
                current_player = ai.swap_player_turn(current_player)
                # 9. display the current player
                print(f"\n\tPlayer {current_player}'s turn.\n")
                # 10a. if player is human, use player_move
                if current_player == ai.player:
                    ai.player_move(current_player)  # TODO: coords breaking when only one move left??
                # 10b. if player is a computer, use minimax_move
                else: 
                    ai.minimax_move(current_player)                
                # 11a. check if there is a winner
                if ai.is_winner(ai.board, current_player):
                    print(f"\n\tPlayer {current_player} wins the game!\n")
                    # 11b. record the winner in tic_tac_toe.txt
                    with open(ai.match_records, 'a') as record:    
                        record.write(f"\nPlayer {current_player} won the game!\n")
                    # 11c. game over
                    break                
                # 12a. check if there is a draw
                if ai.is_board_full(self.board_option):
                    print("\n\tMatch draw!\n")
                    # 12b. record the draw status in tic_tac_toe.txt
                    with open(ai.match_records, 'a') as record:
                        record.write("\nMatch was a draw!\n")
                    # 12c. game over
                    break                
                # 13. display updated gameboard
                ai.display_board(self.board_option) 
            print()           
            # 14. final gameboard display
            ai.display_board(self.board_option)
            print()            
            # 15. reset the gameboard
            ai.reset_board()
            # 16. replay option
            if self.replay() == False:
                break

    def tic_tac_toe(self):
        if self.mode == 1:
            self.game_one()
        if self.mode == 2:
            self.game_two()
        if self.mode == 3:
            self.game_three()
