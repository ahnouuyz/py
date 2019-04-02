import copy

board_positions = set((r, c) for c in range(8) for r in range(8))
directions = set((v - 1, h - 1) for h in range(3) for v in range(3))
directions -= {(0, 0)}

def new_board():
    ll = [[0 for _ in range(8)] for _ in range(8)]
    ll[3][3] = 2
    ll[3][4] = 1
    ll[4][3] = 1
    ll[4][4] = 2
    return ll

def print_board(board):
    sboard = [['-BW'[n] for n in row] for row in board]
    sboard = [[str(i + 1)] + row for i, row in enumerate(sboard)]
    sboard.append(' ,a,b,c,d,e,f,g,h'.split(','))

    txt = '\n'
    for i, row in enumerate(sboard):
        line = ' '
        for j, val in enumerate(row):
            line += val + ' ' if j > 0 else val + ' | '
        txt += line[:-1] + '\n'
        if i == len(sboard) - 2:
            txt += '---|' + len(line[:-4]) * '-' + '\n'
    print(txt)

def score(board):
    s = {1: 0, 2: 0}
    for row in board:
        for num in row:
            if num in s:
                s[num] += 1
    return s[1], s[2]

def enclosing(board, player, pos, direct):
    vsum = lambda v1, v2: tuple(map(lambda a, b: a + b, v1, v2))

    lst = []
    r, c = vsum(pos, direct)
    while (r, c) in board_positions:
        if board[r - 1][c - 1] == 0:
            break
        lst.append(board[r - 1][c - 1])
        r, c = vsum((r, c), direct)

    if len(lst) > 1:
        if lst[-1] == player and player not in lst[:-1]:
            return True
        else:
            return False
    else:
        return False

def valid_moves(board, player):
    directs = tuple(directions)
    vmoves = []
    for r in range(len(board)):
        for c in range(len(board[r])):
            for direct in directs:
                valid = enclosing(board, player, (r, c), direct)
                if valid:
                    vmoves.append((r, c))
                    break
    return vmoves

def next_state(board, player, pos):
    if pos in valid_moves(board, player):
        r, c = pos
        board[r][c] = player
        return board, (0, 2, 1)[player]
    else:
        print('Invalid move.')
        return False


board = new_board()
print_board(board)
print()
print(score(board))
print(enclosing(board, 1, (3, 4), (1, 0)))
print(enclosing(board, 1, (6, 3), (-1, 1)))
print(valid_moves(board, 1))
print(valid_moves(board, 2))
board2 = next_state(board, 1, (3, 4))
print_board(board2[0])

