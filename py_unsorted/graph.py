def all_paths(M, u, v):
    'Return a list of all paths from u to v in M'
    current_row = M[u]
    print(current_row)

    ll = []
    for i, val in enumerate(current_row):
        lst = []
        if i == v:
            lst.append(i)
            return lst
        if val == 1:
            lst.append(i)
            ll.append(all_paths(M, i, v))

    return M, u, v

def main():
    M = [[0, 1, 1, 0],
         [1, 0, 1, 1],
         [1, 1, 0, 1],
         [0, 1, 1, 0]]
    u = 0
    v = 3
    print(all_paths(M, u, v))

if __name__ == '__main__':
    main()
