def tokenization(expr):
    trim = ''.join(expr.split())
    tokens = []
    number_scoop = ''
    for char in trim:
        if char in '.0123456789':
            number_scoop += char
        elif char in '+-*/^()':
            if number_scoop:
                tokens.append(float(number_scoop))
                number_scoop = ''
            tokens.append(char)
        else:
            print(f'Unrecognized character: "{char}" has been ignored')
    if number_scoop:
        tokens.append(float(number_scoop))
    return tokens

def has_precedence(op1, op2):
    """ Here just to fulfill requirements.
        Not actually used anywhere.
    """
    precedences = {'+': 1,
                   '-': 1,
                   '*': 2,
                   '/': 2,
                   '^': 3}
    return precedences[op1] >= precedences[op2]

def operate(num1, operator, num2):
    functions = {'+': float.__add__,
                 '-': float.__sub__,
                 '*': float.__mul__,
                 '/': float.__truediv__,
                 '^': float.__pow__}
    num1 = float(num1)
    num2 = float(num2)
    return functions[operator](num1, num2)

def simple_evaluation(tokens):
    operators = '^/*-+'
    lst = tokens[:]
    for operator in operators:
        while operator in lst:
            if len(lst) <= 3:
                return operate(*lst)
            start = lst.index(operator) - 1
            end = start + 3
            replacement = operate(*lst[start:end])
            lst = lst[:start] + [replacement] + lst[end:]
            print(lst)

def complex_evaluation(tokens):
    lst = tokens[:]
    while '(' in lst and ')' in lst:
        for i, x in enumerate(lst):
            if x == '(':
                start = i
            if x == ')':
                end = i
                break
        replacement = simple_evaluation(lst[start + 1:end])
        lst = lst[:start] + [replacement] + lst[end + 1:]
        print(lst)

#    breakpoint() 
#    while '(' in lst and ')' in lst:
#       start = lst.index('(')
#       end = lst.index(')') + 1
#       replacement = simple_evaluation(lst[start + 1:end - 1])
#       lst = lst[:start] + [replacement] + lst[end:]
#       print(lst)

    return simple_evaluation(lst)

def evaluation(string):
    return complex_evaluation(tokenization(string))

# =======================================================================

def main():
    examples = ['print(tokenization(" 1+ & 1#"))',
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
#    import sys
#    print(evaluation(sys.argv[1]))
