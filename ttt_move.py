from ttt_gui import board


def make_a_move(cell: int, token: str = "x", board: list = board) -> None:
    board[cell] = token
