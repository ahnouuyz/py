#!/usr/bin/env python3

import numpy as np
from tqdm import tqdm

class NeuralNet:
    def __init__(self, structure):
        # First number in structure should be determined.
        np.random.seed(1)
        self.Thetas = []
        for x, y in zip(structure[:-1], structure[1:]):
            self.Thetas.append(np.random.rand(x, y))

    def fprop(self, X, g):
        self.As = [X]
        A = X.copy()
        for Theta in self.Thetas:
            Z = A @ Theta
            A = g(Z)
            self.As.append(A)
        self.output = self.As[-1]
    
    def bprop(self, X, y, g):
        return
        raise NotImplementedError
        D = self.output - y
        for i, (Theta, A1, A2) in enumerate(zip(self.Thetas[:0:-1], self.As[-2:0:-1], self.As[:1:-1])):
            J = D * g(A2)
            Theta -= A1.T @ D
            D = J @ Theta.T

    def train(self, X, y, iterations, choice):
        def sigmoid(x):
            return 1.0 / (1.0 + np.exp(-x))
        def sigmoid_grad(x):
            return x * (1.0 - x)
        activations = {
            'sigmoid': lambda x: 1.0 / (1.0 + np.exp(-x)),
            'relu': lambda x: x * (x > 0),
        }
        gradients = {
            'sigmoid': lambda x: x * (1.0 - x),
            'relu': lambda x: 1.0 * (x > 0),
        }
        for _ in tqdm(range(iterations)):
            self.fprop(X, sigmoid)
            self.bprop(X, y, sigmoid_grad)

if __name__ == '__main__':
    X = np.random.rand(100, 2)
    y = np.random.randint(0, 2, size=(100, 1))
    
    nn = NeuralNet(structure=[2, 3, 1])
    nn.train(X, y, iterations=50, choice='sigmoid')
    
    print(np.array(nn.Thetas))
    print()
    print(((nn.output - y) ** 2).round().sum())
