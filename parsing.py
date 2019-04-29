# Why do we need this?
# from math import pow

def tokenization(expr):
    trim = ''.join(expr.split())
    tokens = []
    number = ''
    for char in trim:
        if char in '.0123456789':
            number += char
        elif char in '+-*/^()':
            if number:
                tokens.append(float(number))
                number = ''
            tokens.append(char)
        else:
            print('Unrecognized character:', char, '<-- has been ignored')
    if number:
        tokens.append(float(number))
    return tokens

def has_precedence(op1, op2):
    precedences = {'+': 1,
                   '-': 1,
                   '*': 2,
                   '/': 2,
                   '^': 3,
                   '(': 4,
                   ')': 4}
    return precedences[op1] >= precedences[op2]

def operate(num1, operator, num2):
    num1 = float(num1)
    num2 = float(num2)
    operators = {'+': float.__add__,
                 '-': float.__sub__,
                 '*': float.__mul__,
                 '/': float.__truediv__,
                 '^': float.__pow__}
    return operators[operator](num1, num2)

def replace_triple(lst, start):
    new_value = operate(*lst[start:start + 3])
    for _ in range(3):
        lst.pop(start)
    lst.insert(start, new_value)

def simple_evaluation(tokens):
    tokens2 = tokens[:]
    while len(tokens2) > 3:
        for i in range(1, len(tokens2) - 3, 2):
            current_token = tokens2[i]
            next_token = tokens2[i + 2]
#            print(current_token, next_token)
            if has_precedence(current_token, next_token):
                replace_triple(tokens2, i - 1)
                break
            elif i == len(tokens2) - 4:
                i += 2
                replace_triple(tokens2, i - 1)
                break
    return operate(tokens2[0], tokens2[1], tokens2[2])

def complex_evaluation(tokens):
    tokens2 = tokens[:]
    while '(' in tokens2 and ')' in tokens2:
        tokens3 = []
        start = tokens2.index('(')
        end = tokens2.index(')')
        tokens3 = tokens2[start + 1:end]
        print(tokens2)
        for i in range(end, start - 1, -1):
            tokens2.pop(i)
        tokens2.insert(start, simple_evaluation(tokens3))
        print(tokens2)
    return simple_evaluation(tokens2)

def evaluation(string):
    return complex_evaluation(tokenization(string))

# =======================================================================

def main():
    examples = ['print(tokenization("1+1"))',
                'print(tokenization("(3.1 + 6*2^2) * (2 - 1)"))',
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
