class Neuron:
    def __init__(self, w, b):
        self.weights = w #weight list
        self.bias = b

    def out(self, inputs): #list
        sum = 0
        for i in range(len(inputs)):
            sum += self.weights[i] * inputs[i]

        return 0 if sum + self.bias <= 0 else 1


class NAND(Neuron):
    def __init__(self):
        super().__init__([-2, -2], 3)


def main():

    x1 = int(input())
    x2 = int(input())

    nand1 = NAND()
    nand2 = NAND()
    nand3 = NAND()
    nand4 = NAND()

    print("sum " + str(
    nand4.out(
        [nand3.out([x2, nand1.out([x1, x2])]),
        nand2.out([x1, nand1.out([x1, x2])])]
    )))
    # circuit which adds two bits x1 and x2


if __name__ == "__main__":
    main()