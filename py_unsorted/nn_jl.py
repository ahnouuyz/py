""" https://towardsdatascience.com/how-to-build-your-own-neural-network-from-scratch-in-python-68998a08e4f6
"""

def sigmoid(x):
    return 1.0 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1.0 - x)

def get_attrs(obj):
    names = [x for x in dir(obj) if (x[0] != '_' and x != 'losses')]
    attrs = {x: getattr(obj, x) for x in names if (hasattr(obj, x) and not callable(getattr(obj, x)))}
    return attrs

def plot_losses(nn):
    fig, ax = plt.subplots(figsize=(16, 6))
    ax.plot(nn.losses)
    ax.set(title='MSE vs. iterations', ylabel='MSE', xlabel='iteration')
    plt.show()

class NeuralNetwork:
    def __init__(self, x, y):
        self.input = x
        self.weights1 = np.absolute(np.random.rand(self.input.shape[1], 4))
        self.weights2 = np.absolute(np.random.rand(4, 1))
        self.y = y
        self.output = np.zeros(y.shape)
        self.losses = []
    
    def squared_error(self):
        errs = self.output - self.y
        sses = errs * errs
        return sses.sum()
    
    @property
    def loss(self):
        return self.squared_error()
    
    def feedforward(self):
        self.layer1 = sigmoid(self.input @ self.weights1)
        self.output = sigmoid(self.layer1 @ self.weights2)
    
    def backprop(self):
        # application of the chain rule to find derivative of the loss function with respect to weights2 and weights1
        d_weights2 = np.dot(self.layer1.T, (2 * (self.y - self.output) * sigmoid_derivative(self.output)))
        d_weights1 = np.dot(self.input.T,  (np.dot(2 * (self.y - self.output) * sigmoid_derivative(self.output), self.weights2.T) * sigmoid_derivative(self.layer1)))

        # update the weights with the derivative (slope) of the loss function
        self.weights1 += d_weights1
        self.weights2 += d_weights2

if __name__ == '__main__':
    X = np.array([[0, 0, 1],
                  [0, 1, 1],
                  [1, 0, 1],
                  [1, 1, 1]])
    y = np.array([0, 1, 1, 0])[:, np.newaxis]
    nn = NeuralNetwork(X, y)

    for i in range(1500):
        nn.feedforward()
        nn.backprop()
        nn.losses.append(nn.loss)

    print(nn.output)
    
    plot_losses(nn)
    
    attrs = get_attrs(nn)
    for name, val in attrs.items():
        print(name)
        print(val)
        print()
