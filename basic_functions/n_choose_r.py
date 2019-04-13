def n_choose_r(n, r):
    """ Calculate n choose r.
        Note n choose r = n choose (n - r), 
        so choose the greater of r and (n - r) to minimize iterations.
    """
    if r < n - r:
        r = n - r
    
    result = 1
    for i, num in enumerate(range(r + 1, n + 1), start=1):
        result *= num / i
    return result
