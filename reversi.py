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
            if row[i] == 2:
                row[i] = 'W'
            elif row[i] == 1:
                row[i] = 'B'
            
            if i == 0:
                txt += str(row[i]) + ' | '
            else:
                txt += str(row[i]) + ' '
        print(txt)

    for r in range(len(new_board)):
        print_row(new_board[r])
        if r == len(new_board) - 2:
            print(hline)

def score(board):
    s1, s2 = 0, 0
    for row in board:
        for num in row:
            if num == 1:
                s1 += 1
            elif num == 2:
                s2 += 1
    return s1, s2

def enclosing(board, player, pos, direct):
    pass

def valid_moves(board, player):
    pass

def next_state(board, player, pos):
    pass


board = new_board()
print_board(board)
print()
print(score(board))
