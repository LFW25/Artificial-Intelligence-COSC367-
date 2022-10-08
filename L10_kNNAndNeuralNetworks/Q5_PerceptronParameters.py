'''
Write a function learn_perceptron_parameters(weights, bias, training_examples, learning_rate, max_epochs)
that adjusts the weights and bias by iterating through the training data and applying the perceptron learning rule.
The function must return a pair (2-tuple) where the first element is the vector (list) of adjusted weights and second argument is the adjusted bias.

The parameters of the function are:

- weights: an array (list) of initial weights of length n
- bias: a scalar number which is the initial bias
- training_examples: a list of training examples where each example is a pair. The first element of the pair is a vector (tuple) of length n. The second element of the pair is an integer which is either 0 or 1 representing the negative or positive class correspondingly.
- learning_rate: a positive number representing eta in the learning equations of perceptron.
- max_epochs: the maximum number of times the learner is allowed to iterate through all the training examples.
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

def learn_perceptron_parameters(weights, bias, training_examples, learning_rate, max_epochs):
    n = len(weights)
    changed = True
    iter = 0
    while changed == True and iter <= max_epochs:
        iter += 1
        changed = False
        for i in range(len(training_examples)):
            pattern = training_examples[i][0]
            output = construct_perceptron(weights, bias)(pattern)
            target = training_examples[i][1]
            
            if output != target:

                for j in range(n):
                    weights[j] = weights[j] + (learning_rate*pattern[j]*(target-output))
                bias = bias + learning_rate*(target-output)
                changed = True

    return (weights, bias)


weights = [2, -4]
bias = 0
learning_rate = 0.5
examples = [
  ((0, 0), 0),
  ((0, 1), 0),
  ((1, 0), 0),
  ((1, 1), 1),
  ]
max_epochs = 50

weights, bias = learn_perceptron_parameters(weights, bias, examples, learning_rate, max_epochs)
print(f"Weights: {weights}")
print(f"Bias: {bias}\n")

perceptron = construct_perceptron(weights, bias)

print(perceptron((0,0)))
print(perceptron((0,1)))
print(perceptron((1,0)))
print(perceptron((1,1)))
print(perceptron((2,2)))
print(perceptron((-3,-3)))
print(perceptron((3,-1)))

#Weights: [1.0, 0.5]
#Bias: -1.5

#0
#0
#0
#1
#1
#0
#1

weights = [2, -4]
bias = 0
learning_rate = 0.5
examples = [
  ((0, 0), 0),
  ((0, 1), 1),
  ((1, 0), 1),
  ((1, 1), 0),
  ]
max_epochs = 50

weights, bias = learn_perceptron_parameters(weights, bias, examples, learning_rate, max_epochs)
print(f"Weights: {weights}")
print(f"Bias: {bias}\n")

#Weights: [-0.5, -0.5]
#Bias: 0.0