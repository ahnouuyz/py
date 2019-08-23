#!/usr/bin/env python3

import numpy as np
from tqdm import tqdm

def sigmoid(x):
        return 1.0 / (1.0 + np.exp(-x))

def sigmoid_grad(x):
    return x * (1.0 - x)

def relu(x):
    return x * (x > 0)

def relu_grad(x):
    return 1.0 * (x > 0)

activators = {
    'sigmoid': (sigmoid, sigmoid_grad),
    'relu': (relu, relu_grad)
}

class NeuralNet:
    def __init__(self, X, y, random_seed=1):
        np.random.seed(random_seed)
        self.X = X
        self.y = y
        self.W = 2 * np.random.rand(X.shape[1], 1) - 1
        self.b = np.random.rand()
        self.output = np.zeros(y.shape)

    def fprop(self, activation):
        self.output = activators[activation][0](self.X @ self.W + self.b)
    
    def bprop(self, activation):
        error = self.output - self.y
        neg_grad = -activators[activation][1](self.output)
        dW = self.X.T @ (error * neg_grad)
        db = (error * neg_grad).sum()
        self.W += dW
        self.b += db

    def train(self, iterations, activation):
        for i in tqdm(range(iterations)):
            self.fprop(activation=activation)
            self.bprop(activation=activation)

if __name__ == '__main__':
    X = np.random.rand(100, 2)
    y = np.random.randint(0, 2, (100, 1))

    nn = NeuralNet(X, y, random_seed=1)
    nn.train(1000, activation='sigmoid')
    
    print(nn.W)
    print(nn.b)
    print(nn.output[:5])
    print()
    print(((nn.output - y) ** 2).round().sum())
