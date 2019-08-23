#!/usr/bin/env python3

def factorize(n):
    if n < 1:
        return 'Only accept positive integers.'
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

def tests():
    examples = [
        'print(factorize(0))', 
        'print(factorize(1))', 
        'print(factorize(2))', 
        'print(factorize(60))', 
        'print(factorize(123456))', 
        'print(factorize(21634987))'
    ]
    for example in examples:
        print(example)
        eval(example)

if __name__ == '__main__':
    tests()
