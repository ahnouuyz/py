import numpy as np
from pathlib import Path
from tqdm import tqdm

np.random.seed(1)

class NeuralNet:
    def __init__(self, structure):
        """ structure: list containing number of neurons per layer.
        """
        self.Thetas = []
        self.biases = []
        for x, y in zip(structure[:-1], structure[1:]):
            self.Thetas.append(np.random.rand(x, y))
            self.biases.append(np.random.rand())

    def fprop(self, X, activation):
        self.Zs = []
        A = X.copy()
        self.As = [A]
        for Theta, bias in zip(self.Thetas, self.biases):
            Z = A @ Theta + bias
            A = activation(Z)
            self.Zs.append(Z)
            self.As.append(A)
        self.output = self.As[-1]
    
    def bprop(self, X, y, gradient):
        D = self.output - y
        for i, (Theta, A1, A2) in enumerate(zip(self.Thetas[:0:-1], self.As[-2:0:-1], self.As[:1:-1])):
            J = D * gradient(A2)
            Theta -= A1.T @ D
            self.biases[-(1 + i)] -= J.sum()
            D = J @ Theta.T

    def train(self, X, y, iterations, choice):
        activations = {
            'sigmoid': lambda x: 1.0 / (1.0 + np.exp(-x)),
            'relu': lambda x: x * (x > 0),
        }
        gradients = {
            'sigmoid': lambda x: x * (1.0 - x),
            'relu': lambda x: 1.0 * (x > 0),
        }
        for _ in tqdm(range(iterations)):
            self.fprop(X, activations[choice])
            self.bprop(X, y, gradients[choice])

if __name__ == '__main__':
    X = np.random.rand(1000, 2)
    y = np.random.randint(0, 2, size=(1000, 1))
    
    nn = NeuralNet(structure=[2, 3, 1])
    nn.train(X, y, iterations=100, choice='sigmoid')
    
    print(np.array(nn.Thetas))
    print(nn.biases)
    print()
    print(((nn.output - y) ** 2).sum())
