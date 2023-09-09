from ttt_gui import board, display_board
from ttt_move import make_a_move
from win_checker import win_checker
from computer import computer_make_a_move

display_board(board=board)

for i in range(8):
    cell = int(input("Select a cell: "))
    make_a_move(cell=cell)
    computer_make_a_move(board=board)
    display_board(board=board)
    if win_checker(board=board):
        break
    if i == 4:
        print("Bueh")
