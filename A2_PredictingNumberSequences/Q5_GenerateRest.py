# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 16:27:57 2022

@author: OEM

Write a function generate_rest(initial_sequence, expression, length) that takes
an initial sequence of numbers, an expression, and a specified length,
and returns a list of integers with the specified length that is the continuation of the initial list according to the given expression. The parameters are:

    initial_sequence: an initial sequence (list) of integer numbers that has at least two numbers;
    expression: an expression constructed from function symbols '+', '-', and '*' which correspond to the three binary arithmetic functions, and the leaf nodes are integers and 'x', 'y', and 'i' where the intended meaning of these three symbols is described above; 
    length: a non-negative integer that specifies the length of the returned list.
"""

def evaluate(expression, bindings):
    if type(expression) is str:
        # Return the value where the str expression is the key
        return bindings[expression]
    
    elif type(expression) is int:
        # int doesn't have a binding
        return expression
    
    elif type(expression) is list and len(expression) == 3:
        # expression is a list
        # return the first elements binding and then recurse on the other 2 elements
        return bindings[expression[0]](evaluate(expression[1], bindings), evaluate(expression[2], bindings))

def generate_rest(initial_sequence, expression, length):
    
    genList = []
    
    i = len(initial_sequence)
    n = len(initial_sequence)
    
    bindings = {'i': i, 'x': initial_sequence[i - 2], 'y': initial_sequence[i - 1], '+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y}
    
    while len(genList) < length:
        
        intEval = evaluate(expression, bindings)
        genList.append(intEval)
        
        i += 1
        
        bindings['i'] = i
        bindings['x'] = bindings['y']
        bindings['y'] = genList[i - n - 1]
        
    return genList



initial_sequence = [0, 1, 2]
expression = 'i' 
length_to_generate = 5
print(generate_rest(initial_sequence, 
                    expression,
                    length_to_generate))

# no particular pattern, just an example expression
initial_sequence = [-1, 1, 367]
expression = 'i' 
length_to_generate = 4
print(generate_rest(initial_sequence,
                    expression,
                    length_to_generate))

initial_sequence = [4, 6, 8, 10]
expression = ['*', ['+', 'i', 2], 2]
length_to_generate = 5
print(generate_rest(initial_sequence, 
                    expression, 
                    length_to_generate))