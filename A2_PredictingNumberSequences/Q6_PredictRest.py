# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 17:39:34 2022

@author: OEM


Write a function predict_rest(sequence) that takes a sequence of integers of length at least 5,
finds the pattern in the sequence, and "predicts" the rest by returning a list of the next five integers in the sequence.
Further assumptions:
    - All the sequences in the test cases have patterns that can be expressed as a function of x, y, and i as described before.
    - All the patterns (functions) can be constructed by combining three binary functions: addition, subtraction, and multiplication.
    - Using integers between -2 and 2 (inclusive) as constant leafs should be enough to represent the patterns in the test cases.
    - All the patterns (functions) can  be constructed by expression trees not deeper than 3.
    - Your algorithm must be able to solve all the problems given in the example test cases in less than 2 seconds (collectively).
        Following the guidelines given in the assignment should naturally achieve this.
"""

import random

def random_expression(function_symbols, leaves, max_depth):
    coin = random.randint(0, 1) == 1
    if coin or max_depth <= 0:
        return random.choice(leaves)
    else:
        return [random.choice(function_symbols), random_expression(function_symbols, leaves, max_depth - 1), random_expression(function_symbols, leaves, max_depth - 1)]

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

def predict_rest(sequence):
    match = False
    
    seqInit = sequence[0:2]
    seqRemaining = sequence[2:]
    
    operators = ['+', '-', '*']
    variables = ['x', 'y', 'i', -2, -1, 0, 1, 2]
    
    while not match:
        randExp =  random_expression(operators, variables, 3)
        otherExp = generate_rest(seqInit, randExp, len(seqRemaining))
        
        if otherExp == seqRemaining:
            match = True
    
    return generate_rest(sequence, randExp, 5)


sequence = [0, 1, 2, 3, 4, 5, 6, 7]
the_rest = predict_rest(sequence)
print(sequence)
print(the_rest)

sequence = [0, 2, 4, 6, 8, 10, 12, 14]
print(predict_rest(sequence))