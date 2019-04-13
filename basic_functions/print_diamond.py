def print_diamond(size):
    q1 = [' ' * (size - i) + '/' * i for i in range(1, size + 1)]
    q3 = [' ' * (size - i) + '\\' * i for i in range(1, size + 1)]
    top = [r1 + r2[::-1] for r1, r2 in zip(q1, q3)]
    bot = [r2 + r1[::-1] for r1, r2 in zip(q1[::-1], q3[::-1])]
    print('\n'.join(top) + '\n' + '\n'.join(bot))
