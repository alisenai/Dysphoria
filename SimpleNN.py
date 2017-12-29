import numpy as np

inputData = np.array([[0, 0, 1], [0, 1, 1], [1, 1, 1], [0, 0, 0]])
outputData = np.array([[0], [1], [1], [0]])
np.random.seed(41134)


class NeuralNetwork:
    def __init__(self, inputSize, hiddenSize, hiddenCount, outputSize):
        self.layers, self.synapses = [], []
        self.synapses.append((2 * np.random.random((inputSize, hiddenSize)) - 1))
        for i in range(hiddenCount):
            self.synapses.append((2 * np.random.random((hiddenSize, hiddenSize)) - 1))
        self.synapses.append((2 * np.random.random((hiddenSize, outputSize)) - 1))

    def nonlin(self, inputData, deriv=False):
        return (inputData * (1 - inputData)) if deriv else (1 / (1 + np.exp(-inputData)))

    def predict(self, inputData):
        self.layers = [inputData]
        for i in range(len(self.synapses)):
            self.layers.append(self.nonlin(np.dot(self.layers[i], self.synapses[i])))
        return self.layers[-1]

    def improve(self, inputData, outputData):
        self.predict(inputData)
        deltas = [(outputData - self.layers[-1]) * self.nonlin(self.layers[-1], deriv=True)]
        for i in range(len(self.layers) - 2, -1, -1):
            self.synapses[i] += self.layers[i].T.dot(deltas[-1])
            deltas.append(deltas[-1].dot(self.synapses[i].T) * self.nonlin(self.layers[i], deriv=True))

    def error(self, outputData):
        return np.mean(np.abs(outputData - self.layers[len(self.layers) - 1]))


nn = NeuralNetwork(3, 3, 1, 1)
for i in range(10000):
    nn.improve(inputData, outputData)
    print("\nError:" + str(nn.error(outputData)))
print("\n" + str(np.round(nn.predict(np.array([[0, 1, 0]])))))
