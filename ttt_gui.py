board = [0, 1, 2, 3, 4, 5, 6, 7, 8]


def display_board(board):
    counter = 0
    for row in board:
        print(row, end="")
        if counter == 0 or counter == 1:
            print(" | ", end="")
        counter += 1
        if counter == 3:
            print(" ")
            counter = 0
