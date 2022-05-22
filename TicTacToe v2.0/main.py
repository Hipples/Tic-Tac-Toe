import ttt_startup
import tic_tac_toe

startup = ttt_startup.TTTStartup()
Xs_and_Os = tic_tac_toe.TicTacToe()

startup.create_welcome_screen()
startup.display_welcome_screen()
option = int(startup.get_player_selection())

if(option == 1):
    Xs_and_Os.play_game_1()
else:
    Xs_and_Os.play_game_2()