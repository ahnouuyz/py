import re, sys, time

def nl_to_ll(nl):
    """ Convert a single line of numbers into a square list of lists.
    """
    n = int(len(nl) ** 0.5)
    ll = [list(nl[r:r + n]) for r in range(0, len(nl), n)]
    return ll

def llprint(ll):
    """ Print out a list of lists nicely.
            Draw borders for the main square and the sectors.
    """
    m = int(len(ll) ** 0.5)
    ll_T = list(zip(*ll))
    cws = [max(map(len, col)) for col in ll_T]
    hline = (sum(cws) + len(cws) + m * 2 + 1) * '-'

    def row_print(row, cws):
        txt = '| '
        for i, val in enumerate(row):
                pad = (cws[i] - len(val)) * ' '
                txt += val + pad
                txt += ' | ' if i % m == m - 1 else ' '
        print(txt)

    print(hline)
    for i, r in enumerate(ll):
        row_print(r, cws)
        if i % m == m - 1:
                print(hline)

def blank_in_ll(ll, blank_char):
    for row in ll:
        if blank_char in row:
            return True
    return False

def cell_options(ll, r, c):
    m = int(len(ll) ** 0.5)
    rr = r // m * m
    cc = c // m * m
    row = ll[r]
    col = list(zip(*ll))[c]
    box = [ll[i][j] for i in range(rr, rr + m) for j in range(cc, cc + m)]
    ops = set(map(str, range(1, len(ll) + 1)))
    return ops.difference(row, col, box)

def solve_one_cell(ll, blank_char):
    """ Find the first blank cell with only 1 option and update it.
    """
    for r in range(len(ll)):
        for c in range(len(ll[r])):
            if ll[r][c] == blank_char:
                ops = cell_options(ll, r, c)
                if len(ops) == 1:
                    ll[r][c] = list(ops)[0]
                    return ll, r, c, ll[r][c]
                elif r == len(ll) - 1 and c == len(ll[-1]) - 1:
                    return -1, -1, -1, -1

def naive_solve(nl, blank_char=r'0'):
    """ Limitation:
        Only works for puzzles with one unique solution,
        i.e. deterministic.
    """
    current_count = len([i for i in nl if i != '0'])
    nl = re.sub(r'0', blank_char, nl)
    ll = nl_to_ll(nl)
    llprint(ll)

    safety = 0
    while blank_in_ll(ll, blank_char=blank_char):
        ll, r, c, op = solve_one_cell(ll, blank_char=blank_char)
        if ll == -1:
            print('Unable to find a solution!')
            break
        current_count += 1
        print(f'Solve {current_count} out of {len(nl)}')
        print(f'{op} entered into row {r + 1}, col {c + 1}')
        llprint(ll)
        time.sleep(0.1)
        safety += 1
        if safety > len(nl):
            print('Safety fuse broken!')
            break
    else:
        print('Completed.')

def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1]) as f:
            nll = [l.strip() for l in f]
            nl = nll[0]
            naive_solve(nl, blank_char=r' ')
    else:
        nl = '004300209005009001070060043006002087190007400050083000600000105003508690042910300'
#        nl = '0043002010020010'
        naive_solve(nl, blank_char=r' ')

if __name__ == '__main__':
    main()
