import sys
import random as rd
from copy import deepcopy

def nl_to_ll(nl):
    n = int(len(nl) ** 0.5)
    return [list(nl[r:r + n]) for r in range(0, len(nl), n)]

def new_board(n=9):
    return [['0' for c in range(n)] for r in range(n)]

def llprint(ll):
    mv = int(len(ll) ** 0.5)
    mh = int(len(ll[0]) ** 0.5)
    sll = [[str(v) for v in row] for row in ll]
    cws = [max(map(len, col)) for col in zip(*ll)]
    sll = [[(cw - len(v)) * ' ' + v 
            for cw, v in zip(cws, row)] 
            for row in sll]

    preline = [cw * '-' for cw in cws]
    qreline = [cw * '-' for cw in cws]

    for i in range(mh + 1):
        for row in sll:
            row.insert(i * (mh + 1), '|')
        preline.insert(i * (mh + 1), '|')
        qreline.insert(i * (mh + 1), '-')

    hline = '-'.join(preline)
    gline = '-'.join(qreline)

    sll = [' '.join(row) for row in sll]
    for j in range(mv + 1):
        sll.insert(j * (mv + 1), (hline, gline)[j in (0, mv)])

    render = '\n'.join(sll)
    print(render)

def cell_ops(tbl, row, col):
    m = int(len(tbl) ** 0.5)
    r = row // m * m
    c = col // m * m
    row = set(tbl[row])
    col = set(tuple(zip(*tbl))[col])
    box = set(tbl[i][j] for i in range(r, r + m) for j in range(c, c + m))
    ops = set(map(str, range(1, len(tbl) + 1)))
    return ops.difference(row, col, box)

def trun(tbls, trys, start=0):
    for i2 in range(start, len(tbls) - 1):
        r = i2 // len(tbls[i2])
        c = i2 % len(tbls[i2])

        if tbls[i2][r][c] == '0':
            choices = cell_ops(tbls[i2], r, c)
            choices.difference_update(trys[i2])
            trys[i2 + 1] = []

            if len(choices):
                rn = rd.sample(choices, 1)[0]
                tbls[i2 + 1] = deepcopy(tbls[i2])
                tbls[i2 + 1][r][c] = rn
                trys[i2].append(rn)
                print(' ' * 60, i2 + 1)
                llprint(tbls[i2 + 1])
            else:
                break
        else:
            tbls[i2 + 1] = deepcopy(tbls[i2])
            trys[i2].append(tbls[i2][r][c])
            llprint(tbls[i2 + 1])

    return tbls, trys, i2

def backtrack(n=9, init=None):
    if init == None:
        tbls = [new_board(n) for _ in range(n * n + 1)]
    else:
        n = len(init)
        tbls = [init for _ in range(n * n + 1)]
    trys = [[] for _ in range(n * n + 1)]

    tbls, trys, start = trun(tbls, trys)
    while start < n * n - 1:
        tbls, trys, start = trun(tbls, trys, start - 1)
    print()
    llprint(tbls[-1])
    return None

def main():
    if len(sys.argv) > 2:
        backtrack(int(sys.argv[1]), nl_to_ll(sys.argv[2]))
    elif len(sys.argv) > 1:
        backtrack(int(sys.argv[1]))
    else:
        backtrack(9)

if __name__ == '__main__':
    main()
