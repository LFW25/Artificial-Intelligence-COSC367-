'''
Write a function accuracy(classifier, inputs, expected_outputs)
that passes each input in the sequence of inputs to the given classifier function (e.g. a perceptron)
and compares the predictions with the expected outputs.
The function must return the accuracy of the classifier on the given data.
Accuracy must be a number between 0 and 1 (inclusive).
'''

def construct_perceptron(weights, bias):
    """Returns a perceptron function using the given paramers."""
    def perceptron(input):
        
        a = bias

        for i in range(len(input)):
            a  += (input[i] * weights[i])
        
        return int(a >= 0)
    
    return perceptron


def accuracy(classifier, inputs, expected_outputs):
    accSum = 0
    accCount = 0

    for i in range(len(inputs)):
        accSum += (classifier(inputs[i]) == expected_outputs[i])
        accCount += 1

    return accSum/accCount


perceptron = construct_perceptron([-1, 3], 2)
inputs = [[1, -1], [2, 1], [3, 1], [-1, -1]]
targets = [0, 1, 1, 0]

print(accuracy(perceptron, inputs, targets))