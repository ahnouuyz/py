import copy

def set_remove(set_, pos):
    set_ -= set(pos)

def set_add(set_, pos):
    set_.update(set(pos))

def new_board():
    """ Returns a board with the Reversi starting configuration.
    """
    ll = [[0 for c in range(8)] for r in range(8)]
    ll[3][3] = 2
    ll[3][4] = 1
    ll[4][3] = 1
    ll[4][4] = 2
    set_remove(pos_left, [(3, 3), (3, 4), (4, 3), (4, 4)])
    return ll

def print_board(board):
    """ Prints the given board in human-readable form to the console.
    """
    # Change '-BWbw' to '-BW', or ' BW', or '_BW', etc.
    f1 = lambda num: '-BWbw'[num]
    f2 = lambda i, row: [str(i + 1), '|'] + list(map(f1, row)) + []
    sboard = list(map(f2, range(len(board)), board))
    sboard.append('-,|,-,-,-,-,-,-,-,-,'.split(','))
    sboard.append(' ,|,a,b,c,d,e,f,g,h,'.split(','))
    render = '\n'.join([' -'[row[0] == '-'].join(row) for row in sboard])
    print('\n' + render + '\n')

def score(board):
    """ Returns a pair of integers (s1, s2) where 
        s1 is the number of stones of Player 1 on the board and 
        s2 is the number of stones of Player 2.
    """
    return tuple(sum([n == p for row in board for n in row]) for p in (1, 2))

def enclosing(board, player, pos, dir_):
    """ Represents whether putting a player's stone on a given position would 
        enclose a straight line of opponent's stones in a given direction.
    """
    line = get_line(board, player, pos, dir_)

    # Player must have a stone down the line, beyond the adjacent position.
    if player in line[2:]:
        # Find the position of the nearest stone.
        k = line[2:].index(player) + 2
        opponent = (0, 2, 1)[player]
        # All positions between must have opponent's stones.
        if all(val == opponent for val in line[1:k]):
            return True
        else:
            return False
    else:
        return False

def get_line(board, player, pos, dir_):
    vsum = lambda v1, v2: tuple(map(lambda a, b: a + b, v1, v2))
    line = []
    while pos in all_pos:
        r, c = pos
        line.append(board[r][c])
        pos = vsum(pos, dir_)
    return line

def switch_line(board, player, pos, dir_):
    vsum = lambda v1, v2: tuple(map(lambda a, b: a + b, v1, v2))
    opponent = (0, 2, 1)[player]
    while pos in all_pos:
        r, c = pos
        if board[r][c] == player:
            return None
        elif board[r][c] == opponent:
            board[r][c] = player
        pos = vsum(pos, dir_)

def valid_moves(board, player):
    """ Returns all valid positions that player is allowed to drop a stone on.
    """
    ps = pos_left
    ds = all_dirs
    e = enclosing
    vmoves = [p for p in ps for d in ds if e(board, player, p, d)]

    map_valid_moves(board, player, vmoves)
    return vmoves

def map_valid_moves(board, player, vmoves):
    """ Help visualize valid positions for player.
    """
    for r, c in vmoves:
        board[r][c] = player + 2

def next_state(board, player, pos):
    """ A pair (next_board, next_player) such that 
        next_board is the result from placing player's stone on pos and 
        next_player is the player who moves next, or 0 if the game ends.
    """
    if pos in valid_moves(board, player):
        r, c = pos
        for d in all_dirs:
            switch_line(board, player, pos, d)
        board[r][c] = player
        set_remove(pos_left, [pos])

        if len(pos_left) <= 0:
            player = 0

        next_board = copy.deepcopy(board)
        next_player = (0, 2, 1)[player]
        return next_board, next_player
    else:
        print('Invalid move.')
        return False

def position(string):
    """ Returns the board position (r, c) described by the string or 
        None if the string does not correspond to a valid board position.
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
    examples = {
        'score(new_board())': '(2, 2)',
        'enclosing(new_board(), 1, (4, 5), (0, -1))': 'True',
        'enclosing(new_board(), 1, (4, 5), (1, 1))': 'False',
        'next_state(new_board(), 1, (4, 5))': '',
        'valid_moves(next_state(new_board(), 1, (4, 5))[0], 2)': '[(3, 5), (5, 3), (5, 5)]',
        'position("e3")': '(2, 4)',
        'position("l1")': 'None',
        'position("a0")': 'None',
        'position("Genghis Khan")': 'None'
    }

    print('\n' + '-' * 30, 'Tests:', '-' * 30)
    for test, expect in examples.items():
        if len(expect) == 0:
            print(test, ':')
            print_board(next_state(new_board(), 1, (4, 5))[0])
            set_add(pos_left, [(4, 5)])
        else:
            print(test, ':', expect, '<=?=>', eval(test))

if __name__ == '__main__':
    # Define a set of all valid directions.
    all_dirs = set((v, h) for h in (-1, 0, 1) for v in (-1, 0, 1)) - {(0, 0)}

    # Define a set of all valid board positions.
    all_pos = set((r, c) for c in range(8) for r in range(8))

    # Define a set of currently available positions.
    # This seems like a good idea, but is causing a lot of headaches.
    pos_left = copy.deepcopy(all_pos)

    tests()

# ============================================================================
# Try converting to a class
# ============================================================================

# class Reversi:
#     coords = set((r, c) for r in range(8) for c in range(8))
#     dirs = set((r, c) for r in (-1, 0, 1) for c in (-1, 0, 1)) - {(0, 0)}

#     def __init__(self):
#         self.board = self.new_board()
#         self.spaces = set((r, c) for c in range(8) for r in range(8))

#     def new_board(self):
#         ll = [[0 for _ in range(8)] for _ in range(8)]
#         ll[3][3] = 2
#         ll[3][4] = 1
#         ll[4][3] = 1
#         ll[4][4] = 2
#         return ll
    
#     def print_board(self, board):
#         f1 = lambda num: '-BWbw'[num]
#         f2 = lambda i, row: [str(i + 1), '|'] + list(map(f1, row)) + []
#         sboard = list(map(f2, range(len(board)), board))
#         sboard.append('-,|,-,-,-,-,-,-,-,-,'.split(','))
#         sboard.append(' ,|,a,b,c,d,e,f,g,h,'.split(','))
#         render = '\n'.join([' -'[row[0] == '-'].join(row) for row in sboard])
#         print('\n' + render + '\n')
    
#     def score(self, board):
#         return tuple(sum([n == p for row in board for n in row]) for p in (1, 2))
