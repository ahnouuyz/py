import copy

vsum = lambda v1, v2: tuple(map(lambda a, b: a + b, v1, v2))
all_pos = set((r, c) for c in range(8) for r in range(8))
pos_left = copy.deepcopy(all_pos)
all_dirs = set((v - 1, h - 1) for h in range(3) for v in range(3))
all_dirs -= {(0, 0)}

def update_pos_left(pos_left, pos):
    pos_left -= set(pos)


def new_board():
    ll = [[0 for _ in range(8)] for _ in range(8)]
    ll[3][3] = 2
    ll[3][4] = 1
    ll[4][3] = 1
    ll[4][4] = 2
    update_pos_left(pos_left, [(3, 3), (3, 4), (4, 3), (4, 4)])
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
        Dictionary conprehension would be even better!
    """
    s = [[1 for row in board for n in row if n == i] for i in (0, 1, 2)]
    return tuple(map(sum, s))

def enclosing(board, player, pos, direct):
    """ This can be optimized.
    """
    other = (0, 2, 1)[player]
    lst = []
    r, c = vsum(pos, direct)
    while (r, c) in all_pos:
        if board[r][c] == 0:
            break
        lst.append(board[r][c])
        r, c = vsum((r, c), direct)

    if lst:
        # Cannot have player's piece immediately ahead.
        # So check the one after and beyond.
        # For now, the check on the first item will happen later.
        # No need to check pos itself, because that's done elsewhere.
        if player in lst[1:]:
            k = lst[1:].index(player) + 1
            if all(val == other for val in lst[:k]):
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def valid_moves(board, player):
    ps = pos_left
    ds = all_dirs
    e = enclosing
    vmoves = [p for p in ps for d in ds if e(board, player, p, d)]

    # Just to help visualize how this works. Remove later.
    print('Valid moves:', vmoves)
    for pos in vmoves:
        r, c = pos
        board[r][c] = player + 2
    
    return vmoves

def next_state(board, player, pos):
    if pos in valid_moves(board, player):
        r, c = pos
        board[r][c] = player
        update_pos_left(pos_left, [pos])
        return board, (0, 2, 1)[player]
    else:
        print('Invalid move.')
        return False

def position(string):
    if isinstance(string, str):
        if string[0] in 'abcdefgh' and string[1] in '12345678':
            r = '12345678'.index(string[1])
            c = 'abcdefgh'.index(string[0])
            return r, c
        else:
            print('Invalid input.')

def run_two_players():
    pass

def run_single_player():
    pass


if __name__ == '__main__':
    # Tests.
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
    print(position('e3'))
    print(position('l1'))
    print(position('a0'))
    print(position('Genghis Khan'))

    print(sorted(pos_left), len(pos_left))

