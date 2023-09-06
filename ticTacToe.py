board = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]


def display_board(board):
    for row in board:
        for cell in range(len(row)):
            print(" | ", row[cell], end=" ", flush=True)
            if row[cell] == row[-1]:
                print(" | ")
                print("")


display_board(board)
