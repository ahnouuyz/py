#!/usr/bin/env python3

import math

def check(n, k):
    try:
        assert int(n) == n and n > 0
        assert int(k) == k and k > 0
    except(AssertionError):
        raise ValueError('Inputs must be positive integers.')

def nChooseK(n, k):
    check(n, k)
    g = math.gamma
    return int(g(n + 1) / g(k + 1) / g(n - k + 1))

def nChooseK_iterative(n, k):
    check(n, k)
    if k < n - k:
        k = n - k
    numerator = set(range(n + 1)) - set(range(k + 1))
    denominator = range(1, n - k + 1)
    prod = 1
    for num, den in zip(list(numerator)[::-1], denominator):
        prod *= num // den
    return prod

def nChooseK_recursive(n, k):
    if k == 0:
        return 1
    check(n, k)
    if k > n - k:
        k = n - k
    return nChooseK_recursive(n - 1, k - 1) * n // k

if __name__ == '__main__':
    n = 10
    k = 4
    print(nChooseK_iterative(n, k))
    print(nChooseK(n, k))
    print(nChooseK_recursive(n, k))
#    print(nChooseK(6.5, 2))
