'''
Write a function knn_predict(input, examples, distance, combine, k) that takes an input and predicts the output by combining the output of the k nearest neighbours.
If after selecting k nearest neighbours, the distance to the farthest selected neighbour and the distance to the nearest unselected neighbour are the same,
more neighbours must be selected until these two distances become different or all the examples are selected.

The description of the parameters of the function are as the following:

- input: an input object whose output must be predicted. Do not make any assumption about the type of input other than that it can be consumed by the distance function.
- examples: a collection of pairs. In each pair the first element is of type input and the second element is of type output.
- distance: a function that takes two objects and returns a non-negative number that is the distance between the two objects according to some metric.
- combine: a function that takes a set of outputs and combines them in order to derive a new prediction (output).
- k: a positive integer which is the number of nearest neighbours to be selected. If there is a tie more neighbours will be selected (see the description above).
'''

from math import sqrt
from collections import Counter

def euclidean_distance(v1, v2):

    distSquared = 0
    for i in range(len(v1)):
        distSquared += (v1[i] - v2[i])**2
 
    return sqrt(distSquared)

def majority_element(labels):
    occurrences = Counter(labels)

    return max(sorted(occurrences), key = occurrences.get)

def knn_predict(input, examples, distance, combine, k):

    k -= 1
    if k > len(examples):
        k = len(examples)

    neighbourDistances = []

    for neighbour in examples:
        neighbourDistances.append((distance(input, neighbour[0]), neighbour))
    
    neighbourDistances = sorted(neighbourDistances)

    kthNeighbourDist = neighbourDistances[k][0]

    for i in range(k+1, len(neighbourDistances)):
        if neighbourDistances[i][0] == kthNeighbourDist and k+1 <= len(examples):
            k += 1
        else:
            break
    
    neighbourDistances = neighbourDistances[:k+1]

    kthNeighboursOutputs = []
    for el in neighbourDistances:
        kthNeighboursOutputs.append(el[1][1])

    predictedOutput = combine(kthNeighboursOutputs)

    return predictedOutput



examples = [
    ([2], '-'),
    ([3], '-'),
    ([5], '+'),
    ([8], '+'),
    ([9], '+'),
]

distance = euclidean_distance
combine = majority_element

for k in range(1, 6, 2):
    print("k =", k)
    print("x", "prediction")
    for x in range(0,10):
        print(x, knn_predict([x], examples, distance, combine, k))
    print()