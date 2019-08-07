from pprint import pprint

def bounded_lists(upper_bounds):
    rngs = (range(n + 1) for n in upper_bounds)
    ll = [[]]
    for rng in rngs:
        ll = [lst + [n] for lst in ll for n in rng]
    return ll

def main():
    ll = bounded_lists([2, 1, 2])
    pprint(ll)

if __name__ == '__main__':
    main()
