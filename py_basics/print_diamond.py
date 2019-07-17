def print_diamond(size):
    q1 = [' ' * (size - i) + '/' * i for i in range(1, size + 1)]
    q3 = [' ' * (size - i) + '\\' * i for i in range(1, size + 1)]
    top = [r1 + r2[::-1] for r1, r2 in zip(q1, q3)]
    bot = [r2 + r1[::-1] for r1, r2 in zip(q1[::-1], q3[::-1])]
    print('\n'.join(top) + '\n' + '\n'.join(bot))

def tests():
    examples = ['print_diamond(0)', 
                'print_diamond(1)', 
                'print_diamond(2)', 
                'print_diamond(3)', 
                'print_diamond(4)', 
                'print_diamond(5)', 
                'print_diamond(6)', 
                'print_diamond(7)', 
                'print_diamond(12)']
    for example in examples:
        print(example)
        eval(example)

if __name__ == '__main__':
    tests()
