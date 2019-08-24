#!/usr/bin/env python3

import numpy as np

class NeuralNet:
    def __init__(self, X, Y, inner_layers=[]):
        self.X = X
        self.Y = Y
        layers = [X.shape[1]] + inner_layers + [Y.shape[1]]
#         np.random.seed(1)
        self.As = [X] + [np.zeros((X.shape[0], n)) for n in layers[1:]]
        self.Thetas = [np.random.rand(l, r) for l, r in zip(layers[:-1], layers[1:])]
    
    def _back_propagation(self, g, alpha):
        """ Still don't really understand what's going on here.
            Therefore, the code is still a little untidy.
        """
        temp = 2 * (self.As[-1] - self.Y) * g(self.As[-1])
        Ds = [self.As[-2].T @ temp]
        for i, Theta in enumerate(self.Thetas[:0:-1]):
            Al = self.As[-(3 + i)]
            Ar = self.As[-(2 + i)]
            temp = temp @ Theta.T * g(Ar)
            Ds.append(Al.T @ temp)
        for Theta, D in zip(self.Thetas, Ds[::-1]):
            Theta -= alpha * D
    
    def _forward_propagation(self, g):
        for i, Theta in enumerate(self.Thetas):
            self.As[i + 1] = g(self.As[i] @ Theta)
        self.output = self.As[-1]
    
    def train(self, iterations, choice, alpha=0.5):
        activations = {
            'sigmoid': lambda x: 1.0 / (1.0 + np.exp(-x)),
            'relu': lambda x: x * (x > 0),
        }
        gradients = {
            'sigmoid': lambda x: x * (1.0 - x),
            'relu': lambda x: 1.0 * (x > 0),
        }
        for i in range(iterations):
            self._forward_propagation(activations[choice])
            self._back_propagation(gradients[choice], alpha)
            score = self.accuracy()
            print(f'Iteration {i + 1}: accuracy = {score * 100:.2f}%')
            if (1 - score) < 0.05:
                break
    
    def accuracy(self):
#         nwrong = ((self.output - self.Y) ** 2).round().sum()
        nwrong = ((self.output.round() - self.Y) ** 2).sum()
        return (1 - (nwrong / len(y)))
    
if __name__ == '__main__':
#     np.random.seed(1)
    X = np.random.rand(100, 2)
    Y = np.random.randint(0, 2, size=(100, 1))
    
    nn = NeuralNet(X, Y, inner_layers=[3, 3])
    nn.train(iterations=100, choice='sigmoid', alpha=1)
    
    print()
    for i, Theta in enumerate(nn.Thetas):
        print(f'Theta_{i + 1}')
        print(np.around(Theta, 3))
