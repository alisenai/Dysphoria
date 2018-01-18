from tkinter import *
import time
import numpy as np
import math

inputData = np.array([[0, 0, 1, 0, 1, 1, 1], [0, 1, 1, 1, 0, 0, 1], [0, 0, 1, 0, 0, 1, 0], [1, 0, 1, 0, 1, 1, 0], [0, 1, 0, 1, 0, 0, 0]])
outputData = np.array([[1, 1, 0, 1, 0, 0, 0], [1, 0, 0, 0, 1, 1, 0], [1, 1, 0, 1, 1, 0, 1], [0, 1, 0, 1, 0, 0, 1], [1, 0, 1, 0, 1, 1, 1]])
np.random.seed(41134)

window = Tk()
window.title("NN")
canvas = Canvas(window, width=1000, height=1000)
canvas.pack()


def create_circle(x, y, r, **kwargs):
    return canvas.create_oval(x - r, y - r, x + r, y + r, **kwargs)


class NeuralNetwork:
    def __init__(self, inputSize, hiddenCount, hiddenSize, outputSize):
        self.layers, self.synapses = [], []
        self.synapses.append((2 * np.random.random((inputSize, hiddenSize)) - 1))
        for i in range(hiddenCount - 1):
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

    def draw(self):
        xOff = 1000 / (len(self.synapses) + 2)
        yOff = 1000 / (max(max(len(self.synapses[0][0]), len(self.synapses[1][0])), len(self.synapses[-1][0])) + 1)
        r = canvas.create_rectangle(0, 0, 1000, 1000, fill="white")
        for i in range(len(self.layers)):  # Loop through each hidden layer
            for j in range(len(self.layers[i])):  # Loop through each hidden layer's weights
                for k in range(len(self.layers[i][j])):  # Loop through each hidden layer's weight's values
                    a = create_circle(xOff + xOff * i, yOff + yOff * k, 3, width=2)
        for i in range(len(self.synapses)):
            for j in range(len(self.synapses[i])):
                for k1 in range(len(self.synapses[i][j])):
                    l = canvas.create_line(xOff + xOff * i,  # Get current neuron's X position
                                           yOff + yOff * j,  # Get current neuron's Y position
                                           xOff + xOff * (i + 1),  # Get next neuron's X position
                                           yOff + yOff * k1,
                                           width=abs(self.synapses[i][j][k1]))
        canvas.update()


nn = NeuralNetwork(7, 10, 10, 7)
for i in range(1000000):
    nn.improve(inputData, outputData)
    if i % 100 == 0:
        print("\nError:" + str(nn.error(outputData)))
        nn.draw()
print("\n" + str(np.round(nn.predict(np.array([[0, 0, 0, 0, 1, 0, 1]])))))

# redLine = canvas.create_line(0, 100, 200, 50, fill="red")
# canvas.delete(redLine)
canvas.mainloop()
