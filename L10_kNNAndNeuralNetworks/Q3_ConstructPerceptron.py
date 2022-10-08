'''
A perceptron is a function that takes a vector (list of numbers) of size n and returns 0 or 1 according to the definition of perceptron.

Write a function construct_perceptron(weights, bias)
where weights is a vector (list of numbers) of of length n
and bias is a scalar number and returns the corresponding perceptron function.
'''

def construct_perceptron(weights, bias):
    """Returns a perceptron function using the given paramers."""
    def perceptron(input):
        
        a = bias

        for i in range(len(input)):
            a  += (input[i] * weights[i])
        
        return int(a >= 0)
    
    return perceptron


weights = [2, -4]
bias = 0
perceptron = construct_perceptron(weights, bias)

print(perceptron([1, 1]))
print(perceptron([2, 1]))
print(perceptron([3, 1]))
print(perceptron([-1, -1]))