# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 15:41:27 2022

@author: OEM

Write a function evaluate(expression, bindings) that takes an expression
and a dictionary of bindings and returns an integer that is the value of the expression.

The parameters of the function are:
    expression: an expression according to our definition of expressions;
    bindings: a dictionary where all the keys are strings and are either a function symbol or a variable leaf.
                A function symbol is mapped to a function that takes two arguments. A leaf symbol is mapped to an integer.
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



bindings = {}
expression = 12
print(evaluate(expression, bindings))


bindings = {'x':5, 'y':10, 'time':15}
expression = 'y'
print(evaluate(expression, bindings))

bindings = {'x': 5, 'y': 10, 'time': 15, 'add': lambda x, y: x + y}
expression = ['add', 12, 'x']
print(evaluate(expression, bindings))

import operator

bindings = dict(x = 5, y = 10, blah = 15, add = operator.add)
expression = ['add', ['add', 22, 'y'], 'x']
print(evaluate(expression, bindings))