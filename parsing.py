from math import pow

def tokenization(expr):
    symbols = {'+', '-', '*', '/', '^', '(', ')'}
    tokens = []
    number = ''
    for char in expr:
        if char.isnumeric() or char == '.':
#            print('Part of a number:', char)
            number += char
        elif char in symbols:
#            print('Good token:', char)
            if len(number) > 0:
                tokens.append(float(number))
                number = ''
            tokens.append(char)
        else:
            print('Unrecognized character:', char, '<-- has been ignored')
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

def operate(number1, operator, number2):
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    elif operator == '/':
        return number1 / number2
    elif operator == '^':
        return pow(number1, number2)
    else:
        print('Unknown operator:', operator)

def simple_evaluation(tokens):
    # Find the operator with the highest precedence.
    for i in range(1, len(tokens) - 3, 2):
        current_token = tokens[i]
        next_token = tokens[i + 2]
        print(current_token, next_token)
        print(has_precedence(current_token, next_token))
        if has_precedence(current_token, next_token):
            print('We will evaluate here')
            print(tokens[i - 1:i + 2])
            print(operate(tokens[i - 1], tokens[i], tokens[i + 1]))
#    operators = tokens[1::2]
#    print(tokens)
#    print(operators)

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

