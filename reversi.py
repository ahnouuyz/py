import copy

# Define a vector sum function to add tuples element-wise.
vsum = lambda v1, v2: tuple(map(lambda a, b: a + b, v1, v2))

# Define a set of all valid directions.
all_dirs = set((v - 1, h - 1) for h in range(3) for v in range(3))
all_dirs -= {(0, 0)}

# Define a set of all valid board positions.
all_pos = set((r, c) for c in range(8) for r in range(8))

# Define a set of currently available positions.
pos_left = copy.deepcopy(all_pos)

def update_pos_left(pos_left, pos):
    """ Remove pos from pos_left.
        We can completely avoid this function if we used classes.
        In fact, try to find a way to get rid of this function.
    """
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
    # Append row number (in string format) to the start of each row.
    # Concurrently, convert numbers in each row to symbols.
    # The small letters are there to visualize valid positions (remove when before final version).
    # Every entry in sboard would be strings at the end.
    sboard = [[str(i + 1)] + ['-BWbw'[n] for n in row] for i, row in enumerate(sboard)]
    sboard.append(' ,a,b,c,d,e,f,g,h'.split(','))

    # Store entire printout in render, then print all at once, instead of line-by-line.
    # Prepare for transition into classes in the future.
    render = '\n'
    for i, row in enumerate(sboard):
        line = ' '
        for j, val in enumerate(row):
            # Only add a stroke after the first column (with the row numbers).
            line += val + ' ' if j > 0 else val + ' | '
        render += line[:-1] + '\n'
        # Only add a hohrizontal line before the last row (with the column markers).
        if i == len(sboard) - 2:
            render += '---|' + len(line[:-4]) * '-' + '\n'
    print(render)

def score(board):
    """ Have to exclude count of 0 later.
        Dictionary conprehension would be even better!
    """
    s = [[1 for row in board for n in row if n == i] for i in (0, 1, 2)]
    return tuple(map(sum, s))

def enclosing(board, player, pos, direct):
    """ This is probably the most important function.
        This can be optimized.
        I think.
    """
    other = (0, 2, 1)[player]
    lst = []
    r, c = vsum(pos, direct)
    while (r, c) in all_pos:
        if board[r][c] == 0:
            break
        lst.append(board[r][c])
        r, c = vsum((r, c), direct)

    # This is so ugly...
    if lst:
        # Cannot have player's piece immediately ahead.
        # So check the one after and beyond.
        # For now, the check on the first item will happen later.
        # Flaw: pos itself is not checked in this function, but it's ok due to pos_left.
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
    # We should really, really, really do classes.
    ps = pos_left
    ds = all_dirs
    e = enclosing
    vmoves = [p for p in ps for d in ds if e(board, player, p, d)]

    # Just to help visualize valid positions (remove before final version).
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
    """ Reads only the 1st 2 characters of the input string.
        1st character must be in a-h.
        2nd character must be in 1-8.
        The correct row and column indices will be obtained from the respective arrays.
    """
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


def tests():
    test_list = [
        'score(new_board())',
        'enclosing(new_board(), 1, (4, 5), (0, -1))',
        'enclosing(new_board(), 1, (4, 5), (1, 1))',
        'next_state(new_board(), 1, (4, 5))',
        'valid_moves(next_state(new_board(), 1, (4, 5))[0], 2)',
        'position('e3')',
        'position('l1')',
        'position('a0')',
        'position('Genghis Khan')'
    ]
    
    expected = [
        ''
    ]
    
    print('Tests:')
    for test in test_list:
        print(test, ':', eval(test))
    
#    print('score(new_board()):', score(new_board()))
#    print('enclosing(new_board(), 1, (4, 5), (0, -1)):', enclosing(new_board(), 1, (4, 5), (0, -1)))
#    print('enclosing(new_board(), 1, (4, 5), (1, 1)):', enclosing(new_board(), 1, (4, 5), (1, 1)))
#    print('next_state(new_board(), 1, (4, 5)):')
#    print_board(next_state(new_board(), 1, (4, 5))[0])
#    print('valid_moves(next_state(new_board(), 1, (4, 5))[0], 2):')
#    print(valid_moves(next_state(new_board(), 1, (4, 5))[0], 2))
#    print(position('e3'))
#    print(position('l1'))
#    print(position('a0'))
#    print(position('Genghis Khan'))

if __name__ == '__main__':
    tests()
#    print(sorted(pos_left), len(pos_left))
