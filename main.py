import math
import random

class SigmoidNeuron:
    def __init__(self, w, b, activateFunction):
        self.weights = w #weight list
        self.bias = b
        self.activateFunction = activateFunction #with this realisation each neuron could have different activation function
        self.output = 0 #0 to 1

    def out(self, inputs): #list
        self.output = self.activateFunction(sum([self.weights[i]*inputs[i] for i in range(len(inputs))]) + self.bias) #output = f(∑jwjxj + b)
        return self.output
        


class NetworkLayer: #the layer of neurons
    def __init__(self, neuronList):
        self.neuronList = neuronList
        self.len = len(neuronList)


class NeuralNetwork:
    def __init__(self, layerList):
        self.layerList = layerList

    def release(self, inputs): #inputs is like list of lists of inputs for each neuron in first layer [[x1, x2], [x1, x2], ...]
        outputList = [] #list of outputs for each layer

        for neuronIndex in range(self.layerList[0].len): #getting first layer outputs
            outputList.append(self.layerList[0].neuronList[neuronIndex].out(inputs[neuronIndex]))

        for layerIndex in range(len(self.layerList)):
            if layerIndex == 0:
                continue

            #now outputList is inputs for each layer
            layerOutputList = [] #outputs of that layer
            for neuronIndex in range(self.layerList[layerIndex].len):
                layerOutputList.append(self.layerList[layerIndex].neuronList[neuronIndex].out(outputList))

            outputList = layerOutputList

        return outputList


#activation functions
def sigmoid(z): 
    return 1/(1 + math.exp(-z))

def stepFunction(z):
    return 1 if z>=0 else 0



def main():
    #initiating network
    network = [] #layers
    for i in range(3):
        layer = [] #neurons
        if i == 0:
            for j in range(4): #3 layers, 4 neurons on each
                layer.append(SigmoidNeuron(
                    [random.randint(-10, 10), random.randint(-10, 10)],
                    random.randint(-10, 10),
                    sigmoid
                ))
        else:
            for j in range(4):
                layer.append(SigmoidNeuron(
                    [random.randint(-10, 10) for t in range(4)], #4 neurons in each layer so 4 inputs in each neurons besides the first layer
                    random.randint(-10, 10),
                    sigmoid
                ))
        layer = NetworkLayer(layer) #list of Neuron class becomes layer class
        network.append(layer)
    network = NeuralNetwork(network)


    inputs = [[random.randint(-10, 10) for j in range(2)] for i in range(4)] #two inputs for each neuron in first layer

    print(network.release(inputs))


if __name__ == "__main__":
    main()