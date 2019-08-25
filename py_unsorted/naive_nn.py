#!/usr/bin/env python3

import numpy as np

class NeuralNet:
    def __init__(self, X, Y, inner_layers=[]):
        np.random.seed(1)
        self.X = X
        self.Y = Y
        layers = [X.shape[1]] + inner_layers + [Y.shape[1]]
        self.As = [X] + [np.zeros((X.shape[0], n)) for n in layers[1:]]
        self.Thetas = [np.random.rand(l, r) for l, r in zip(layers[:-1], layers[1:])]
    
    def _fprop(self, g):
        for i, Theta in enumerate(self.Thetas):
            self.As[i + 1] = g(self.As[i] @ Theta)
        self.output = self.As[-1]
    
    def _bprop(self, g, alpha):
        d_layer = 2 * (self.output - self.Y) * g(self.output)
        for i in range(len(self.Thetas)):
            A_prev = self.As[-(2 + i)]
            Theta = self.Thetas[-(1 + i)]
            if i > 0:
                Theta_next = self.Thetas[-i]
                A = self.As[-(1 + i)]
                d_layer = d_layer @ Theta_next.T * g(A)
            d_theta = A_prev.T @ d_layer
            Theta -= d_theta * (alpha / self.X.shape[0])
    
    def train(self, iterations, func, alpha=1):
        activations = {
            'sigmoid': lambda x: 1.0 / (1.0 + np.exp(-x)),
            'relu': lambda x: x * (x > 0),
        }
        gradients = {
            'sigmoid': lambda x: x * (1.0 - x),
            'relu': lambda x: 1.0 * (x > 0),
        }
        score = 0
        for i in range(iterations):
            if score < 0.99:
                self._fprop(activations[func])
                self._bprop(gradients[func], alpha)
                if self.accuracy() != score:
                    print(f'Iteration {i + 1}: accuracy = {self.accuracy() * 100:.2f}%')
                    score = self.accuracy()
            else:
                break
        else:
            print(f'Iteration {i + 1}: accuracy = {self.accuracy() * 100:.2f}%')
    
    def accuracy(self):
        return (self.output.round() == self.Y).mean()
    
if __name__ == '__main__':
    np.random.seed(1234)
    N = 40
    X = np.random.rand(N, 2)
    Y = np.random.randint(0, 2, size=(N, 1))
    
    nn = NeuralNet(X, Y, inner_layers=[3])
    nn.train(iterations=1000, func='sigmoid', alpha=1)
    
    print()
    for i, Theta in enumerate(nn.Thetas):
        print(f'Theta_{i + 1}')
        print(np.around(Theta, 3))
