class Matrix:
    def __init__(self, ll):
        self.ll = ll
        self.nrows = len(ll)
        self.ncols = len(ll[0])
    
    def __repr__(self):
        sll = [list(map(str, row)) for row in self.ll]
        cws = [max(map(len, col)) for col in zip(*sll)]
        txt = ''
        for i, row in enumerate(sll):
            line = ' [' if i > 0 else '[['
            for cw, val in zip(cws, row):
                spaces = (cw - len(val)) * ' '
                line += spaces + val + ' '
            line = line[:-1]
            line += ']' if i < len(sll) - 1 else ']]'
            txt += line + '\n'
        return txt[:-1]
    
    def __str__(self):
        return self.__repr__()
    
    def __add__(self, other):
        if isinstance(other, (int, float)):
            add_to_all = lambda lst: list(map(lambda a: a + other, lst))
            return Matrix(list(map(add_to_all, self.ll)))
    
    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            sub_from_all = lambda lst: list(map(lambda a: a - other, lst))
            return Matrix(list(map(sub_from_all, self.ll)))
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            mul_to_all = lambda lst: list(map(lambda a: a * other, lst))
            return Matrix(list(map(mul_to_all, self.ll)))
    
    def __rmul__(self, other):
        return self.__mul__(other)

    def __matmul__(self, right_matrix):
        lm = self.ll
        rm = list(zip(*right_matrix.ll))
        if self.ncols == right_matrix.nrows:
            dot = lambda v1, v2: sum(map(lambda a, b: a * b, v1, v2))
            return Matrix([[dot(lrow, rcol) for rcol in rm] for lrow in lm])
        else:
            print('Unable to multiply matrices: ncols(left) != nrows(right).')
            return None

    def transpose(self):
        return Matrix(list(zip(*self.ll)))
    
    T = property(transpose)

if __name__ == '__main__':
    A = [[1, 2],
         [3, 4],
         [5, 6]]
    B = [[1], 
         [2],
         [3]]
    A = Matrix(A)
    B = Matrix(B)

    print(A)
    print(A.T)
    print(A.T.T)
    print(A.T @ B)
    print(B.T @ A)
