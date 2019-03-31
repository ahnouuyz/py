class Matrix:
    def __init__(self, ll):
        self.ll = ll
    
    def __repr__(self):
        sll = [list(map(str, row)) for row in self.ll]
        cws = [max(map(len, col)) for col in zip(*sll)]

        txt = ''
        for i, row in enumerate(sll):
            line = '[[' if i == 0 else ' ['
            for cw, val in zip(cws, row):
                pad = (cw - len(val)) * ' '
                line += pad + val + ' '
            line = line[:-1]
            line += ']' if i < len(sll) - 1 else ']]'
            txt += line + '\n'
        return txt[:-1]
    
    def __str__(self):
        return self.__repr__()
    
    def __matmul__(self, rm):
        lm = self.ll
        rm = rm.ll

        rm_T = tuple(zip(*rm))
        if len(lm[0]) == len(rm):
            dot = lambda v1, v2: sum(map(lambda a, b: a * b, v1, v2))
            result = [[dot(lm[r], rm_T[c]) for c in range(len(rm_T))] for r in range(len(lm))]
            return result
        else:
            print('Unable to multiply matrices: ncols(left) != nrows(right).')
            return None

    def transpose(self):
        return Matrix(list(zip(*self.ll)))

A = [[1, 2, 3, 10],
     [4, 5, 6, 11],
     [7, 8, 9, 12]]

B = [[5], 
     [5],
     [2],
     [1]]

A = Matrix(A)
B = Matrix(B)

print(A)
print(A.transpose())
print(B)
print(B.transpose())

C = Matrix(A @ B)
print(C)
D = Matrix(B @ B.transpose())
print(D)
