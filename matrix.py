class Matrix:
    def __init__(self, ll):
        self.ll = [[float(val) for val in row] for row in ll]
        self.shape = len(ll), len(ll[0])

    def __str__(self):
        sll = [[str(val) for val in row] for row in self.ll]
        cws = [max(map(len, col)) for col in zip(*sll)]
        sll = [[(cw - len(val)) * ' ' + val 
                for cw, val in zip(cws, row)] 
                for row in sll]
        render = [('[[', ' [')[i > 0] 
                  + '  '.join(row) 
                  + (']]', ']')[i < len(sll) - 1] 
                  for i, row in enumerate(sll)]
        return '\n'.join(render)

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Matrix([[val + other for val in row] for row in self.ll])

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return Matrix([[val - other for val in row] for row in self.ll])

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            return Matrix([[other - val for val in row] for row in self.ll])

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Matrix([[val * other for val in row] for row in self.ll])

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Matrix([[val / other for val in row] for row in self.ll])

    def __rtruediv__(self, other):
        if isinstance(other, (int, float)):
            return Matrix([[other / val for val in row] for row in self.ll])

    def __matmul__(self, other):
        if self.shape[1] != other.shape[0]:
            print('Unable to multiply matrices.')
            print(f'Left matrix: {self.shape[0]} x {self.shape[1]}')
            print(f'Right matrix: {other.shape[0]} x {other.shape[1]}')
            return None
        dot = lambda v1, v2: sum(map(float.__mul__, v1, v2))
        lm = self.ll
        rm = list(zip(*other.ll))
        return Matrix([[dot(lr, rc) for rc in rm] for lr in lm])

    def transpose(self):
        return Matrix(list(zip(*self.ll)))

    def flatten(self):
        return [val for row in self.ll for val in row]

    def g_elimination(self):
        raise NotImplementedError

        r, c = 0, 0
        while r in range(self.shape[0]) and c in range(self.shape[1]):
            # Find the row with the largest absolute leading number.

            pass

        ll = self.ll
        pivot_row = self.ll.index(max(lambda x: abs(x[0])))

        return None

    def gj_elimination(self):
        raise NotImplementedError

    def determinant(self):
        raise NotImplementedError

    def invert(self):
        raise NotImplementedError

    @classmethod
    def zeros(cls, n):
        return Matrix([[0 for c in range(n)] for r in range(n)])

    @classmethod
    def ones(cls, n):
        return Matrix([[1 for c in range(n)] for r in range(n)])

    @classmethod
    def eye(cls, n):
        return Matrix([[(0, 1)[r == c] for c in range(n)] for r in range(n)])

    __radd__ = __add__
    __rmul__ = __mul__
    T = property(transpose)
    ref = property(g_elimination)
    rref = property(gj_elimination)
    det = property(determinant)

    # ========== End of Matrix class ==========

def main():
    A = Matrix([[1, 2], 
                [3, 4], 
                [5, 6]])
    B = Matrix([[1], 
                [2], 
                [3]])

    examples = ['print(A)', 
                'print(A.T)', 
                'print(A.T.T)', 
                'print(A.T @ A)', 
                'print(A / 2)', 
                'print(A.T @ B)', 
                'print(B.T @ A)', 
                'print(B.T @ B)', 
                'print(Matrix.eye(4))', 
                'print(Matrix.eye(4) + 2)', 
                'print(3 + Matrix.eye(4))', 
                'print(A.flatten())']

    for example in examples:
        print(example)
        eval(example)

    bigA = Matrix([[i for i in range(200)] for i in range(200)])
    bigB = bigA @ bigA

if __name__ == '__main__':
    main()

