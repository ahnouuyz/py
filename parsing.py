from math import pow

def remove_whitespaces(string):
    return ''.join(string.split())

def tokenization(expr):
    operators_and_brackets = {'+', '-', '*', '/', '^', '(', ')'}
    short_expr = remove_whitespaces(expr)
    tokens = []
    for char in short_expr:
        if char in operators_and_brackets:
            tokens.append(
    print(remove_whitespaces(expr))

def has_precedence(op1, op2):
    raise NotImplementedError

def simple_evaluation(tokens):
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

