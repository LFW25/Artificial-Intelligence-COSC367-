'''
Write a function of the form is_valid_expression(object, function_symbols, leaf_symbols)
that takes an object as its first argument and tests whether it is a valid expression according to our definition of expressions in this assignment.
The function must return True if the given object is valid expression, False otherwise.

The parameters of the function are:

object: any Python object
function_symbols: a collection (list, set, ...) of strings that are allowed to be used in function positions (internal nodes of the tree).
leaf_symbols: a collection of strings that are allowed to be used as variable leaves.
'''

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



function_symbols = ['f', '+']
leaf_symbols = ['x', 'y']
expression = 1

print(is_valid_expression(expression, function_symbols, leaf_symbols))

function_symbols = ['f', '+']
leaf_symbols = ['x', 'y']
expression = 'y'

print(is_valid_expression(
        expression, function_symbols, leaf_symbols))

function_symbols = ['f', '+']
leaf_symbols = ['x', 'y']
expression = 2.0

print(is_valid_expression(
        expression, function_symbols, leaf_symbols))

function_symbols = ['f', '+']
leaf_symbols = ['x', 'y']
expression = ['f', 123, 'x']

print(is_valid_expression(
        expression, function_symbols, leaf_symbols))