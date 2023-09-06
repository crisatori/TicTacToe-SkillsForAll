board = [["", "", ""], ["", "", ""], ["", "", ""]]


def display_board(board):
    for row in board:
        for cell in enumerate(row):
            ind = cell[0]
            ele = cell[1]
            print(" | ", ele, end=" ", flush=True)
            if ind == 2:
                print(" | ")


def enter_move(board=board):
    pass
    row = int(input("Type the row number *0 - 2* :"))
    element = int(input("Type element number *0 - 2* :"))
    board[row][element] = "v"
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.


enter_move()
display_board(board)
