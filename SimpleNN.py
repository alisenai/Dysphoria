import numpy as np

inputData = np.array([[0, 0, 1], [0, 1, 1], [1, 1, 1], [0, 0, 0]])
outputData = np.array([[0], [1], [1], [0]])
np.random.seed(41134)


class NeuralNetwork:
    def __init__(self, inputSize, hiddenSize, hiddenCount, outputSize):
        self.layers, self.synapses = [], []
        self.synapses.append((2 * np.random.random((inputSize, hiddenSize)) - 1))
        for i in range(hiddenCount - 1):
            self.synapses.append((2 * np.random.random((hiddenSize, hiddenSize)) - 1))
        self.synapses.append((2 * np.random.random((hiddenSize, outputSize)) - 1))

    def nonlin(self, inputData, deriv=False):
        return abs(inputData * (1 - inputData)) if deriv else abs(1 / (1 + np.exp(-inputData)))

    def predict(self, inputData):
        self.layers = [inputData]
        for j in range(len(self.synapses)):
            self.layers.append(self.nonlin(np.dot(self.layers[j], self.synapses[j])))
        return self.layers[-1]

    def improve(self, inputData, outputData):
        self.predict(inputData)
        deltas = [(outputData - self.layers[-1]) * self.nonlin(self.layers[-1], deriv=True)]
        for k in range(len(self.layers) - 2, -1, -1):
            self.synapses[k] += self.layers[k].T.dot(deltas[-1])
            deltas.append(deltas[-1].dot(self.synapses[k].T) * self.nonlin(self.layers[k], deriv=True))

    def error(self, outputData):
        return np.mean(np.abs(outputData - self.layers[len(self.layers) - 1]))


nn = NeuralNetwork(3, 3, 1, 1)
for _ in range(10000):
    nn.improve(inputData, outputData)
    print("\nError:" + str(nn.error(outputData)))
print("\n" + str(np.round(nn.predict(np.array([[0, 1, 0]])))))
