def bounded_lists(upper_bounds):
    pools = tuple(tuple(range(n + 1)) for n in upper_bounds)
    result = [[]]
    for pool in pools:
        result = [x + [y] for x in result for y in pool]
    return result

def main():
    print(bounded_lists([1, 1, 2]))

if __name__ == '__main__':
    main()
