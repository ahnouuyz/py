from math import pow

def tokenization(expr):
    operators_and_brackets = {'+', '-', '*', '/', '^', '(', ')'}
    short_expr = ''.join(expr.split())
    tokens = []
    print(list(short_expr))
#    for i, char in enumerate(short_expr):
#        if char in operators_and_brackets:
#            short_expr = short_expr[i + 1 - len(tokens):]
#            tokens.append(char)
#            print(tokens)
#            print(short_expr)
#        else:
#            continue

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

