# Tic Tac Toe with a GUI guided by this tutorial: https://www-geeksforgeeks-org.cdn.ampproject.org/v/s/www.geeksforgeeks.org/tic-tac-toe-game-with-gui-using-tkinter-in-python/amp/?amp_gsa=1&amp_js_v=a9&usqp=mq331AQKKAFQArABIIACAw%3D%3D#amp_tf=From%20%251%24s&aoh=16525271879831&referrer=https%3A%2F%2Fwww.google.com&ampshare=https%3A%2F%2Fwww.geeksforgeeks.org%2Ftic-tac-toe-game-with-gui-using-tkinter-in-python%2F

# ONLY ISSUE IN THIS PROGRAM IS THAT THE GAME DOES NOT RECOGNIZE DIAGONAL WINS 

# import necessary libraries
import random
from tkinter import *
from functools import partial
from tkinter import messagebox
from copy import deepcopy

# sign variable to determine whose turn it is
sign = 0

# create an empty board
global board 
board = [[" " for x in range(3)] for y in range(3)]

# check if match has been won
def winner(b, l): # straight across, up and down, or diagonal
    return ((b[0][0] == l and b[0][1] == l and b[0][2] == l) or 
            (b[1][0] == l and b[1][1] == l and b[1][2] == l) or
            (b[2][0] == l and b[2][1] == l and b[2][2] == l) or
            (b[0][0] == l and b[1][0] == l and b[2][0] == l) or
            (b[0][1] == l and b[1][1] == l and b[2][1] == l) or
            (b[0][2] == l and b[1][2] == l and b[2][2] == l) or
            (b[0][0] == 1 and b[1][1] == 1 and b[2][2] == 1) or 
            (b[2][0] == 1 and b[1][1] == 1 and b[0][2] == 1))

# configure text on button (Player vs Player)
def get_text(i, j, gb, l1, l2):
    global sign
    if board[i][j] == ' ':
        if sign % 2 == 0:
            l1.config(state = DISABLED)
            l2.config(state = ACTIVE)
            board[i][j] = "X"
        else:
            l2.config(state = DISABLED)
            l1.config(state = ACTIVE)
            board[i][j] = "O"
        sign += 1
        button[i][j].config(text = board[i][j])
    if winner(board, "X"):
        gb.destroy()
        box = messagebox.showinfo("Winner", "Player 1 won the match!")
    elif winner(board, "O"):
        gb.destroy()
        box = messagebox.showinfo("Winner", "Play 2 won the match!")
    elif (isfull()):
        gb.destroy()
        box = messagebox.showinfo("Tie Game", "It's a draw!")

# check if the player can push the button or not
def isfree(i, j):
    return board[i][j] == ' '

# check if board is full or not
def isfull():
    flag = True
    for i in board:
        if (i.count(' ') > 0):
            flag = False
    return flag

# decide the next move of the system
def pc():
    possiblemove = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ' ':
                possiblemove.append([i, j])
    move = []
    if possiblemove == []:
        return
    else:
        for let in ['O', 'X']:
            for i in possiblemove:
                boardcopy = deepcopy(board)
                boardcopy[i[0]][i[1]] = let
                if winner(boardcopy, let):
                    return i
        corner = []
        for i in possiblemove:
            if i in [[0, 0], [0, 2], [2, 0], [2, 2]]:
                corner.append(i)
        if len(corner) > 0:
            move = random.randint(0, len(corner) - 1)
            return corner[move]
        edge = []
        for i in possiblemove:
            if i in [[0, 1], [1, 0], [1, 2], [2, 1]]:
                edge.append(i)
        if len(edge) > 0:
            move = random.randint(0, len(edge) - 1)
            return edge[move]

# configure text on button (Player vs PC)    
def get_text_pc(i, j, gb, l1, l2):
    global sign
    if board[i][j] == ' ':
        if sign % 2 == 0:
            l1.config(state = DISABLED)
            l2.config(state = ACTIVE)
            board[i][j] = "X"
        else:
            button[i][j].config(state = ACTIVE)
            l2.config(state = DISABLED)
            l1.config(state = ACTIVE)
            board[i][j] = "O"
        sign += 1
        button[i][j].config(text = board[i][j])
    x = True
    if winner(board, "X"):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Winner", "Player won the match!")
    elif winner(board, "O"):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Winner", "Computer won the match!")
    elif (isfull()):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Tie Game", "It's a draw!")
    if (x):
        if sign % 2 != 0:
            move = pc()
            button[move[0]][move[1]].config(state = DISABLED)
            get_text_pc(move[0], move[1], gb, l1, l2)

# create the GUI of the gameboard (Player vs PC)
def gameboard_pc(game_board, l1, l2):
    global button
    button = []
    for i in range(3):
        m = 3 + i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(get_text_pc, i, j, game_board, l1, l2)
            button[i][j] = Button(game_board, bd = 5, command = get_t, height = 4, width = 8)
            button[i][j].grid(row = m, column = n)
    game_board.mainloop()

# initialize the gameboard (Player vs PC)
def withPC(game_board):
    game_board.destroy()
    game_board = Tk()
    game_board.title("Tic Tac Toe")
    l1 = Button(game_board, text = "Player: X", width = 10)
    l1.grid(row = 1, column = 1)
    l2 = Button(game_board, text = "Computer: O", width = 10, state = DISABLED)
    l2.grid(row = 2, column = 1)
    gameboard_pc(game_board, l1, l2)

# create the gameboard GUI (Player vs Player)
def gameboard_pl(game_board, l1, l2):
    global button
    button = []
    for i in range(3):
        m = 3 + i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(get_text, i, j, game_board, l1, l2)
            button[i][j] = Button(game_board, bd = 5, command = get_t, height = 4, width = 8)
            button[i][j].grid(row = m, column = n)
    game_board.mainloop()

# initialize the gameboard (Player vs Player)
def withPlayer(game_board):
    game_board.destroy()
    game_board = Tk()
    game_board.title("Tic Tac Toe")
    l1 = Button(game_board, text = "Player 1: X", width = 10)
    l1.grid(row = 1, column = 1)
    l2 = Button(game_board, text = "Player 2: O", width = 10, state = DISABLED)
    l2.grid(row = 2, column = 1)
    gameboard_pl(game_board, l1, l2)

# main function
def play():
    menu = Tk()
    menu.geometry("250x250")
    menu.title("Tic Tac Toe")
    wpc = partial(withPC, menu)
    wpl = partial(withPlayer, menu)

    head = Button(menu, text = "---Welcome to Tic-Tac-Toe---",
                  activeforeground = 'red',
                  activebackground = 'yellow', bg = 'red',
                  fg = 'yellow', width = 500, font = 'summer', bd = 5)

    B1 = Button(menu, text = "Single Player", command = wpc,
                activeforeground = 'red',
                activebackground = 'yellow', bg = 'red', 
                fg = 'yellow', width = 500, font = 'summer', bd = 5)

    B2 = Button(menu, text = "Multiplayer", command = wpl,
                activeforeground = 'red',
                activebackground = 'yellow', bg = 'red', 
                fg = 'yellow', width = 500, font = 'summer', bd = 5)

    B3 = Button(menu, text = "Exit", command = menu.quit,
                activeforeground = 'red',
                activebackground = 'yellow', bg = 'red', 
                fg = 'yellow', width = 500, font = 'summer', bd = 5)

    head.pack(side = 'top')
    B1.pack(side = 'top')
    B2.pack(side = 'top')
    B3.pack(side = 'top')
    menu.mainloop()

# call main function
if __name__ == '__main__':
    play()