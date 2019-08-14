def tokenization(expr):
    tokens = []
    number = ''
    for char in expr:
        if char in '.0123456789':
            number += char
        elif char in '+-*/^()':
            if number:
                tokens.append(number)
                number = ''
            tokens.append(char)
    if number:
        tokens.append(number)
    return tokens

def operate(num1, operator, num2):
    functions = {
        '+': float.__add__,
        '-': float.__sub__,
        '*': float.__mul__,
        '/': float.__truediv__,
        '^': float.__pow__
    }
    return functions[operator](float(num1), float(num2))

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
            del lst[start:end]
            lst.insert(start, replacement)
#            lst = lst[:start] + [replacement] + lst[end:]
#            print(lst)

def complex_evaluation(tokens):
    lst = tokens[:]
    while '(' in lst and ')' in lst:
        for i, c in enumerate(lst):
            if c == '(':
                start = i
            elif c == ')':
                end = i
                break
#        end = lst.index(')')
#        start = lst.rfind('(', 0, end)
        replacement = simple_evaluation(lst[start + 1:end])
        del lst[start:end + 1]
        lst.insert(start, replacement)
#        lst = lst[:start] + [replacement] + lst[end + 1:]
#        print(lst)
    return simple_evaluation(lst)

def evaluation(expr):
    return complex_evaluation(tokenization(expr))

# =======================================================================

def main():
    examples = ['print(tokenization(" 1+ & 1#"))',
                'print(tokenization("(3.1 + 6*2^2) * (2 - 1)"))',
                'print(simple_evaluation([2, "+", 3, "*", 4, "^", 2, "+", 1]))',
                'print(complex_evaluation(["(", 2, "-", 7, ")", "*", 4, "^", "(", 2, "+", 1, ")"]))',
                'print(evaluation("(2-7) * 4^(2+1)"))',
                'print(evaluation("((1 +2) * 3) ^ (4/5)"))']

    for example in examples:
        print(example)
        eval(example)
        print()

if __name__ == '__main__':
     main()
