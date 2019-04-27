from math import pow

def tokenization(expr):
    symbols = {'+', '-', '*', '/', '^', '(', ')'}
    tokens = []
    number = ''
    for char in expr:
        if char == ' ':
#            print('Discarding a space')
            continue
        elif char.isnumeric() or char == '.':
#            print('Part of a number:', char)
            number += char
        elif char in symbols:
#            print('Good token:', char)
            if len(number) > 0:
                tokens.append(float(number))
                number = ''
            tokens.append(char)
        else:
            raise ValueError('Unrecognized character:', char)
    return tokens

def has_precedence(op1, op2):
    precedences = {'+': 1,
                   '-': 1,
                   '*': 2,
                   '/': 2,
                   '^': 3,
                   '(': 4,
                   ')': 4}
    if precedences[op1] > precedences[op2]:
        return True
    else:
        return False

def simple_evaluation(tokens):
    # Find the operator with the highest precedence.
    for i in range(1, len(tokens) - 3, 2):
        current_token = tokens[i]
        next_token = tokens[i + 2]
        print(current_token, next_token)
#    operators = tokens[1::2]
#    print(tokens)
#    print(operators)
    raise NotImplementedError

def complex_evaluation(tokens):
    raise NotImplementedError

def evaluation(string):
    raise NotImplementedError

# =======================================================================

def main():
    examples = ['print(tokenization("(3.1 + 6*2^2) * (2 - 1)"))',
                'print(has_precedence("*", "+"))',
                'print(has_precedence("^", "+"))',
                'print(has_precedence("*", "^"))',
                'print(has_precedence("*", "/"))',
                'print(simple_evaluation([2, "+", 3, "*", 4, "^", 2, "+", 1]))',
                'print(complex_evaluation(["(", 2, "-", 7, ")", "*", 4, "^", "(", 2, "+", 1, ")"]))',
                'print(evaluation("(2-7) * 4^(2+1)"))']

    for example in examples:
        print(example)
        eval(example)
        print()

if __name__ == '__main__':
    main()

