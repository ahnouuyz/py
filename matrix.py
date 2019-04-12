import random as rd

class Matrix:
    """ Convenient packaging for a list of lists of numbers.
        Includes some convenient operations.
        Short-term goal: 
            Perform simple linear regression.
    """
    def __init__(self, ll):
        self.ll = [[float(v) for v in row] for row in ll]
        self.shape = len(ll), len(ll[0])

    def __str__(self):
        sll = [[str(v) for v in row] for row in self.ll]
        cws = [max(map(len, col)) for col in zip(*sll)]
        sll = [[(cw - len(v)) * ' ' + v 
                for cw, v in zip(cws, row)] 
                for row in sll]
        render = [' [' + '  '.join(row) + ']' for row in sll]
        return '[' + '\n'.join(render)[1:] + ']'

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Matrix([[v + other for v in row] for row in self.ll])

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return Matrix([[v - other for v in row] for row in self.ll])

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            return Matrix([[other - v for v in row] for row in self.ll])

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Matrix([[v * other for v in row] for row in self.ll])

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Matrix([[v / other for v in row] for row in self.ll])

    def __rtruediv__(self, other):
        if isinstance(other, (int, float)):
            return Matrix([[other / v for v in row] for row in self.ll])

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
        return [v for row in self.ll for v in row]

    def gauss(self):
        ll = self.ll
        det = 1
        r, c = 0, 0
        while r < self.shape[0] - 1 and c < self.shape[1] - 1:
            if max(ll[r:], key=lambda x: abs(x[c]))[c] < 1e-10:
                c += 1
                continue
            disp = ll[r:].index(max(ll[r:], key=lambda x: abs(x[c])))

            if disp:
                ll[r + disp], ll[r] = ll[r], ll[r + disp]
                det *= -1
            
            for i in range(r + 1, self.shape[0]):
                mult = ll[i][c] / ll[r][c]
                for j in range(c, self.shape[1]):
                    ll[i][j] -= ll[r][j] * mult
            det *= ll[r][c]
            r += 1
            c += 1

        # We should have the correct determinant at this point.

        return Matrix(ll)

    def jordan(self):
        raise NotImplementedError

        ll = self.ref.ll
        r, c = self.shape
        while r > 1 and c > 1:
            r -= 1
            c -= 1
            for i in range(r - 1, 0, -1):
                mult = ll[i][c] / ll[r][c]
                for j in range(c, 0, -1):
                    ll[i][j] -= ll[r][j] * mult
        return Matrix(ll)

    def determinant(self):
        raise NotImplementedError

        # Sign is incorrect; Need to note how many swaps take place.
        ll = self.ref.ll
        prod = 1
        for i in range(min(self.shape)):
            prod *= ll[i][i]
        return prod

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

    @classmethod
    def rand(cls, size=(1, 1), randrange=(0, 10)):
        m, n = size
        l, u = randrange
        return Matrix([[rd.randint(l, u) for c in range(n)] for r in range(m)])

    __radd__ = __add__
    __rmul__ = __mul__
    T = property(transpose)
    ref = property(gauss)
    rref = property(jordan)
    det = property(determinant)

    # ========== End of Matrix class ==========

def main():
    A = Matrix([[1, 2], 
                [3, 4], 
                [5, 6]])
    B = Matrix([[1], 
                [2], 
                [3]])
    C = Matrix([[1, 2, 3, 4], 
                [5, 6, 7, 8], 
                [8, 8, 7, 7], 
                [5, 4, 3, 3]])
    D = Matrix([[2, 4], 
                [6, 8]])
    E = Matrix.rand((4, 4))

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
                'print(A.flatten())', 
                'print(C)', 
                'print(C.ref)', 
                'print(Matrix.rand((3, 3)))', 
                'print(E)', 
                'print(E.ref)']

    for example in examples:
        print(example)
        eval(example)

#    bigA = Matrix([[i for i in range(200)] for i in range(200)])
#    bigB = bigA @ bigA

if __name__ == '__main__':
    main()

