import copy

def new_board():
    ll = [[0 for _ in range(8)] for _ in range(8)]
    ll[3][3] = 2
    ll[3][4] = 1
    ll[4][3] = 1
    ll[4][4] = 2
    return ll

def print_board(board):
    new_board = [[str(i + 1)] + board[i] for i in range(8)]
    new_board.append(' ,a,b,c,d,e,f,g,h'.split(','))
    hline = (9 * 2 - 1) * '-'
    hline = '---|' + hline
    
    def print_row(row):
        txt = ' '
        for i in range(len(row)):
            if i == 0:
                txt += str(row[i]) + ' | '
            elif isinstance(row[i], str):
                txt += str(row[i]) + ' '
            else:
                txt += str(('-BW')[row[i]]) + ' '
        print(txt)

    for r in range(len(new_board)):
        print_row(new_board[r])
        if r == len(new_board) - 2:
            print(hline)

def score(board):
    s = {1: 0, 2: 0}
    for row in board:
        for num in row:
            if num in s:
                s[num] += 1
    return s[1], s[2]

def enclosing(board, player, pos, direct):
    lst = []
    r = pos[0] + direct[0]
    c = pos[1] + direct[1]
    while r < len(board) + 1 and c < len(board[0]) + 1:
        if board[r - 1][c - 1] == 0:
            break
        lst.append(board[r - 1][c - 1])
        r += direct[0]
        c += direct[1]
    if len(lst) > 1:
        if lst[-1] == player and player not in lst[:-1]:
            return True
        else:
            return False
    else:
        return False

def valid_moves(board, player):
    directs = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1))
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
        r = pos[0]
        c = pos[1]
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

