from ttt_gui import board
from random import randint


def computer_make_a_move(board: list = board) -> None:
    while True:
        choice = randint(0, 8)
        if board[choice] != "x" and board[choice] != "o":
            board[choice] = "o"
            break
