def factorize(n):
    """ Returns the factors of a given number.
    """
    dct = {}
    while n % 2 == 0:
        dct[2] = dct.get(2, 0) + 1
        n /= 2
    if n > 1:
        for i in range(3, int(n), 2):
            while n % i == 0:
                dct[i] = dct.get(i, 0) + 1
                n /= i
    if len(dct) < 1:
        dct[n] = 1
    return dct
