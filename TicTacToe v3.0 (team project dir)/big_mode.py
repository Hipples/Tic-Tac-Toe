from TicTacToe.game_objects import PlayerActions

class BigMode:
    def __init__(self, mode = 1, board = 2):
        self.mode = mode
        self.board = board
    
    def coin_flip(self):
        pass


    def big_mode_1(self):
        """Big PvP Mode. Game loop."""
        # initialize game objects from PlayerActions class
        action = PlayerActions()
        # initiate replay loop
        while True:
            # 0. append 'New Game!' to tic_tac_toe.txt
            with open(action.match_records, 'a') as record:
                record.write("\n\nPlayer vs Player (5x5)! Game on!\n")
            # 1. create the gameboard
            action.create_big_board()
            # 2. assign player markers based on choice
            action.player, action.opponent = action.assign_markers()
            # 3. randomly decide which player goes first
            if self.coin_flip() == 1:
                first_player = action.player
            else:
                first_player = action.opponent
            # 4. inform the players who won first turn
            print(f"\n\tPlayer {first_player} will go first!\n")
            # 5. display empty gameboard
            action.print_big_board()
            # 6. input and make move
            action.player_move(first_player)
            print()
            # 7. display updated gameboard
            action.print_big_board()
            # 8. assign current_player as first_player
            current_player = first_player
            while True:
                # 9. swap player turn
                current_player = action.swap_player_turn(current_player)
                # 10. display whose turn to play
                print(f"\n\tPlayer {current_player}'s turn.\n")
                sleep(1)
                # 11. display updated gameboard
                action.print_big_board()
                # 12. capture and make player move
                action.player_move(current_player)
                print()
                # 13a. check if there is a winner
                if action.is_big_winner(action.board, current_player):
                    print(f"\n\tPlayer {current_player} wins the game!\n")
                    # 13b. record the winner in tic_tac_toe.txt
                    with open(action.match_records, 'a') as record:
                        record.write(f"\nPlayer {current_player} won the game!\n")
                    # 13c. game over
                    break
                # 14a. check if there is a draw
                if action.is_draw(board_option = 2):
                    print("\n\tMatch draw!\n")
                    # 14b. record the draw status in tic_tac_toe.txt
                    with open(action.match_records, 'a') as record:
                        record.write("\nMatch was a draw!\n")
                    # 14c. game over
                    break
                # 15. display updated gameboard
                action.print_big_board()
            print()
            # 16. final gameboard display
            action.print_big_board()
            print()
            # 17. reset gameboard
            action.reset_board()
            # 18. replay option
            if self.replay() == False:
                break