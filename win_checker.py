def win_checker(board: list) -> bool:
    tokens = ["x", "o"]
    r1 = board[0:3]
    r2 = board[3:6]
    r3 = board[6:]
    cero, uno, dos = board[0:3]
    tres, cuatro, cinco = board[3:6]
    seis, siete, ocho = board[6:]
    for i in tokens:
        for j in [r1, r2, r3]:
            if j.count(i) == 3:
                print(f"Player {i} won!")
                return True
    dos, cinco, ocho = [board[2], board[5], board[8]]
    uno, cuatro, siete = [board[1], board[4], board[7]]
    cero, tres, seis = [board[0], board[3], board[6]]

    primero = [dos, cinco, ocho]
    segundo = [uno, cuatro, siete]
    tercero = [cero, tres, seis]

    for i in tokens:
        for j in [primero, segundo, tercero]:
            if j.count(i) == 3:
                print(f"Player {i} won!")
                return True

    cero, cuatro, ocho = [board[0], board[4], board[8]]
    dos, cuatro, seis = [board[2], board[4], board[6]]

    cuarto: list = [cero, cuatro, ocho]
    quinto: list = [dos, cuatro, seis]

    for i in tokens:
        for j in [cuarto, quinto]:
            if j.count(i) == 3:
                print(f"Player {i} won!")
                return True
    return False
    # print(f"{board[0:3] = } { board[3:6] = } { board[6:] = } ")
