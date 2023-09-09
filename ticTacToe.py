from ttt_gui import board, display_board
from ttt_move import make_a_move
from win_checker import win_checker

display_board(board=board)

for i in range(8):
    cell = int(input("Select a cell: "))
    make_a_move(cell=cell)
    display_board(board=board)
    if win_checker(board=board):
        break
