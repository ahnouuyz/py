from math import pi
from math import sqrt

def basel(precision):
    n, series_sum, pie = 0, 0, 0
    while abs(pie - pi) > precision:
        n += 1
        series_sum += 1 / (n * n)
        pie = sqrt(series_sum * 6)
    return pie, n

def taylor(precision):
    n, series_sum, pie = 0, 0, 0
    while abs(pie - pi) > precision:
        n += 1
        series_sum += 1 / (n * 2 - 1) * (-1, 1)[n % 2]
        pie = series_sum * 4
    return pie, n

def wallis(precision):
    n, series_prod, pie = 0, 1, 0
    while abs(pie - pi) > precision:
        n += 2
        series_prod *= n * n / (n - 1) / (n + 1)
        pie = series_prod * 2
    return pie, int(n / 2)

def spigot(precision):
    n, series_sum, pie = 0, 0, 0
    while abs(pie - pi) > precision:
        n += 1
        term = 1
        for i2 in range(2, n + 1):
            term *= (i2 - 1) / (i2 * 2 - 1)
        series_sum += term
        pie = series_sum * 2
    return pie, n

def race(precision, algorithms):
    results = []
    for i, algorithm in enumerate(algorithms):
        results.append((i + 1, algorithm(precision)[1]))
    return sorted(results, key=lambda t: t[1])

def print_results(results):
    for i, steps in results:
        print(f'Algorithm {i} finished in {steps} steps')

print(basel(0.1))
print(taylor(0.2))
print(wallis(0.2))
print(spigot(0.1))
print(race(0.01, [taylor, wallis, basel]))
print_results(race(0.01, [taylor, wallis, basel]))