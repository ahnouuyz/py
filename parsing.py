# Why do we need this?
# from math import pow

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
    if precedences[op1] >= precedences[op2]:
        return True
    else:
        return False

def operate(number1, operator, number2):
    if operator == '+':
        result =  number1 + number2
    elif operator == '-':
        result =  number1 - number2
    elif operator == '*':
        result =  number1 * number2
    elif operator == '/':
        result =  number1 / number2
    elif operator == '^':
        result =  number1 ** number2
    else:
        print('Unknown operator:', operator)
    return float(result)

def simple_evaluation(tokens):
    tokens2 = tokens[:]
    while len(tokens2) > 3:
        for i in range(1, len(tokens2) - 3, 2):
            current_token = tokens2[i]
            next_token = tokens2[i + 2]
            print(current_token, next_token)
            print(has_precedence(current_token, next_token))
            if has_precedence(current_token, next_token):
                res = operate(tokens2[i - 1], tokens2[i], tokens2[i + 1])
                print('We will evaluate here')
                print(tokens2[i - 1:i + 2])
                print(res)
                tokens2.pop(i + 1)
                tokens2.pop(i)
                tokens2.pop(i - 1)
                tokens2.insert(i - 1, res)
                print(tokens2)
                break
            elif i == len(tokens2) - 4:
                i += 2
                res = operate(tokens2[i - 1], tokens2[i], tokens2[i + 1])
                tokens2.pop(i + 1)
                tokens2.pop(i)
                tokens2.pop(i - 1)
                tokens2.insert(i - 1, res)
                break
    return operate(tokens2[0], tokens2[1], tokens2[2])

def complex_evaluation(tokens):
    tokens2 = tokens[:]
    while '(' in tokens2 and ')' in tokens2:
        tokens3 = []
        for i, token in enumerate(tokens2):
            if token == '(':
                start = i
            elif token == ')':
                end = i
                break
        print(start, end)
        for i in range(start + 1, end):
            tokens3.append(tokens2[i])
        print(tokens3)
        print(tokens2)
        for i in range(end, start - 1, -1):
            print(i)
            tokens2.pop(i)
        print(tokens2)
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

