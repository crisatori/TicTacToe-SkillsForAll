board = [["00", "01", "02"], ["10", "11", "12"], ["20", "21", "22"]]


def display_board(board):
    a, b, c = board[0]
    d, e, f = board[1]
    g, h, i = board[2]
    print(
        f"""
        {a} \t{b}\t{c}\n
        {d}\t{e}\t{f}\n
        {g}\t{h}\t{i}
        """
    )
    return None


# for row in board:
#     for cell in enumerate(row):
#         ind = cell[0]
#         ele = cell[1]
#         print(" | ", ele, end=" ", flush=True)
#         if ind == 2:
#             print(" | ")
def make_list_of_free_fields(board=board) -> int:
    pass
    available_space = 0
    for row in board:
        for cell in row:
            if cell == "x" or cell == "o":
                available_space += 1
    return available_space


def enter_move(token, board: list[str] = board):
    row, element = None, None
    row = int(input("Type the row number *0 - 2* :"))
    element = int(input("Type element number *0 - 2* :"))
    board[row][element] = token
    display_board(board)
    space = make_list_of_free_fields(board)
    print(f"Players have made {space}/8 movements.")


for i in range(1, 8 + 1):
    enter_move("x")
