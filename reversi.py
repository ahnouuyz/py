import copy

vsum = lambda v1, v2: tuple(map(lambda a, b: a + b, v1, v2))
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
    sboard = [['-BWbw'[n] for n in row] for row in board]
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
    """ Have to exclude count of 0 later.
    """
    s = [[1 for row in board for n in row if n == i] for i in (0, 1, 2)]
    return tuple(map(sum, s))

def enclosing(board, player, pos, direct):
    lst = []
    r, c = vsum(pos, direct)
    while (r, c) in board_positions:
        if board[r][c] == 0:
            break
        lst.append(board[r][c])
        r, c = vsum((r, c), direct)

    if lst:
        if player in lst[1:]:
            k = lst[1:].index(player) + 1
            # print(pos, direct, lst, player, k, all(val == (0, 2, 1)[player] for val in lst[:k]))
            if all(val == (0, 2, 1)[player] for val in lst[:k]):
                return True

def valid_moves(board, player):
    directs = directions
    vmoves = []
    for pos in sorted(board_positions):
        for direct in directs:
            valid = enclosing(board, player, pos, direct)
            if valid:
                vmoves.append(pos)
                break
    
    for pos in vmoves:
        r, c = pos
        board[r][c] = player + 2
    
    return vmoves

def next_state(board, player, pos):
#    tpos = vsum(pos, (-1, -1))
    tpos = pos
    print(tpos, valid_moves(board, player))
    if tpos in valid_moves(board, player):
        r, c = tpos
        board[r][c] = player
        return board, (0, 2, 1)[player]
    else:
        print('Invalid move.')
        return False

def position(string):
    if isinstance(string, str):
        r = '12345678'.index(string[1])
        c = 'abcdefgh'.index(string[0])
        return r, c
    pass

def run_two_players():
    pass

def run_single_player():
    pass

def empty_spaces(board):
    lst = [1 for row in board for num in row if num == 0]
    return sum(lst)


if __name__ == '__main__':
    game1 = new_board()
    print('score(game1):', score(game1))
    print('enclosing(game1, 1, (4, 5), (0, -1)):', enclosing(game1, 1, (4, 5), (0, -1)))
    print('enclosing(game1, 1, (4, 5), (1, 1)):', enclosing(game1, 1, (4, 5), (1, 1)))
    move1 = next_state(game1, 1, (4, 5))
    print('next_state(game1, 1, (4, 5)):')
    # print(move1)
    print_board(move1[0])
    print('valid_moves(move1[0], 2):')
    print(valid_moves(move1[0], 2))
    print_board(move1[0])

    print(empty_spaces(game1))
    # r = '12345678'.index('4')
    # c = 'abcdefgh'.index('e')
    # print(r, c)

    # print_board(board)
    # print()
    # print(score(board))
    # print(enclosing(board, 1, (3, 4), (1, 0)))
    # print(enclosing(board, 1, (6, 3), (-1, 1)))
    # print(sorted(valid_moves(game1, 1)))
    # print(sorted(valid_moves(game1, 2)))
    # board2 = next_state(board, 1, (3, 4))
    # print_board(game1)
    # print_board(board2[0])
