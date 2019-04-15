def n_choose_r(n, r):
    """ Calculate n choose r.
        Note n choose r = n choose (n - r), 
        so choose the greater of r and (n - r) to minimize iterations.
    """
    if n < 0 or r < 0:
        raise ValueError('Negative numbers not accepted.')
    if r < n - r:
        r = n - r
    result = 1
    for i, num in enumerate(range(r + 1, n + 1), start=1):
        result *= num / i
    return int(result)

def tests():
    examples = ['print(n_choose_r(6, 0))', 
#                'print(n_choose_r(6, -1))', 
                'print(n_choose_r(6, 1))', 
                'print(n_choose_r(6, 2))', 
                'print(n_choose_r(6, 3))', 
                'print(n_choose_r(6, 4))', 
                'print(n_choose_r(12, 5))']
    for example in examples:
        print(example)
        eval(example)

if __name__ == '__main__':
    tests()
