import numpy as np
import random

board = np.zeros((3, 3)).astype(int)
turn = 1
move = 9
print(board)

def play_turn():
    if(turn ==1):
        x = int(input(f"What is player {turn}'s x position?")) # The code will be explained below
        y = int(input(f"What is player {turn}'s y position?")) # in part (a)
    else:
        x = random.randint(0,2); # The code will be explained below
        y = random.randint(0,2); # in part (b)
    
    try: # section explained (a)
        if board[y, x]==0:   # section explained (b)
            board[y, x]=turn # section explained (b)
        else:                                       # section explained (C)
            if(turn == 1):                          # section explained (C) 
                print("The board already contains") # section explained (C)
            play_turn() 
    except IndexError:        # section explained (D)
        print("Input error")  # section explained (D)
        play_turn()           # section explained (D)

def check_win():
    if any(np.sum(board, 1)==3) or any(np.sum(board, 0)==3) or sum(np.diag(board))==3 or sum(np.diag(board[::-1]))==3:
        return True
    if any(np.sum(board, 1)==-3) or any(np.sum(board, 0)==-3) or sum(np.diag(board))==-3 or sum(np.diag(board[::-1]))==-3:
        return True
    return False

while move >0:
    # Draw the board
#         a
#----------------------
    print (board) 
    play_turn()   
#----------------------
    if check_win():
#         b
#--------------------------------------------
        print (f"Player {turn} has won!")
        break
#--------------------------------------------
#         c
#--------------------------------------------
    turn = turn*-1
    move = move -1
#--------------------------------------------