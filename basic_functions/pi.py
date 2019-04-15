from math import pi
from math import sqrt

def basel(precision):
    n, basel_sum, pie = 0, 0, 0
    while abs(pie - pi) > precision:
        n += 1
        basel_sum += 1 / n / n
        pie = sqrt(basel_sum * 6)
    return pie, n

def taylor(precision):
    n, taylor_sum, pie = 0, 0, 0
    while abs(pie - pi) > precision:
        n += 1
        taylor_sum += (-1, 1)[n % 2] / (n * 2 - 1)
        pie = taylor_sum * 4
    return pie, n

def wallis(precision):
    n, wallis_product, pie = 0, 1, 0
    while abs(pie - pi) > precision:
        n += 2
        wallis_product *= n * n / (n - 1) / (n + 1)
        pie = wallis_product * 2
    return pie, n // 2

def spigot(precision):
    n, spigot_sum, pie = 0, 0, 0
    while abs(pie - pi) > precision:
        n += 1
        intermediate_product = 1
        for i in range(2, n + 1):
            intermediate_product *= (i - 1) / (i * 2 - 1)
        spigot_sum += intermediate_product
        pie = spigot_sum * 2
    return pie, n

def race(precision, algorithms):
    results = []
    for i, algorithm in enumerate(algorithms, start=1):
        results.append((1, algorithm(precision)[1]))
    return sorted(results, key=lambda x: x[1])

def print_results(results):
    for i, steps in results:
        print(f'Algorithm {i} finished in {steps} steps')

def tests():
    examples = ['print(basel(0.1))',
                'print(taylor(0.2))',
                'print(wallis(0.2))',
                'print(spigot(0.1))',
                'print(race(0.01, [taylor, wallis, basel]))',
                'print_results(race(0.01, [taylor, wallis, basel]))']
    for example in examples:
        print(example)
        eval(example)

if __name__ == '__main__':
    tests()
