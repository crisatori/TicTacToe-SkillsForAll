board = [["a", "b", "c"], ["d", "e", "f"], ["h", "i", "j"]]


def display_board(board):
    for row in board:
        for cell in enumerate(row):
            ind = cell[0]
            ele = cell[1]
            print(" | ", ele, end=" ", flush=True)
            if ind == 2:
                print(" | ")


display_board(board)
