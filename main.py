class Neuron:
    def __init__(self, w, b):
        self.weights = w #weight list
        self.bias = b

    def out(self, inputs): #list
        sum = 0
        for i in range(len(inputs)):
            sum += self.weights[i] * inputs[i]

        return 0 if sum + self.bias <= 0 else 1



def main():

    w = [-2, -2]
    n = Neuron(w, 3) #NAND

    print(n.out([0, 0]))
    print(n.out([0, 1]))
    print(n.out([1, 0]))
    print(n.out([1, 1]))


if __name__ == "__main__":
    main()