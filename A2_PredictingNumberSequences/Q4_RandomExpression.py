# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 16:06:44 2022

@author: OEM

Write a function random_expression(function_symbols, leaves, max_depth) that randomly generates an expression. The function takes the following arguments:

function_symbols: a list of function symbols (strings)
leaves: a list of constant and variable leaves (integers and strings)
max_depth: a non-negative integer that specifies the maximum depth allowed for the generated expression.
"""

def is_valid_expression(object, function_symbols, leaf_symbols):
    '''
    We define an object to be an expression if it is either:
        a constant leaf: a Python integer (for example 3);
        a variable leaf: a Python string (for example 'y') from a pre-specified set of leaf symbols;
        a Python list such that:
            the list has exactly 3 elements; and
            the first element is a string (for example '*') from a pre-specified set of function symbols; and
            the remaining two elements of the list are expressions themselves; these two serve as the arguments of the function.'
    '''
    isValid = False
    
    if type(object) == int or object in leaf_symbols:
        # Single object (not list)
        # Integer or leaf symbol
        isValid = True
    
    elif type(object) != list or len(object) != 3 or object[0] not in function_symbols:
        pass
    
    elif ( type(object[1]) == int or object[1] in leaf_symbols ) and ( type(object[2]) == int or object[2] in leaf_symbols ):
        # Other items are ints or leaf symbols
        isValid = True

    else:
        # Recurse on next element
        isValid = is_valid_expression(object[1], function_symbols, leaf_symbols) and is_valid_expression(object[2], function_symbols, leaf_symbols)
    
    
    return isValid

import random

def random_expression(function_symbols, leaves, max_depth):
    coin = random.randint(0, 1) == 1
	if coin or max_depth <= 0:
		return random.choice(leaves)
	else:
		return [random.choice(function_symbols), random_expression(function_symbols, leaves, max_depth - 1), random_expression(function_symbols, leaves, max_depth - 1)]


function_symbols = ['f', 'g', 'h']
constant_leaves =  list(range(-2, 3))
variable_leaves = ['x', 'y', 'i']
leaves = constant_leaves + variable_leaves
max_depth = 4

for _ in range(10000):
    expression = random_expression(function_symbols, leaves, max_depth)
    if not is_valid_expression(expression, function_symbols, leaves):
        print("The following expression is not valid:\n", expression)
        break
else:
    print("OK")
    

function_symbols = ['f', 'g', 'h']
leaves = ['x', 'y', 'i'] + list(range(-2, 3))
max_depth = 4

expressions = [random_expression(function_symbols, leaves, max_depth)
               for _ in range(10000)]

# Out of 10000 expressions, at least 1000 must be distinct
_check_distinctness(expressions)