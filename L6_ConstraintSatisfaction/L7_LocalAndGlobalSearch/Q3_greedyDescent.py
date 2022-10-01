# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 10:52:33 2022

@author: Lily Williamss
"""

# =============================================================================
# Write a function greedy_descent(initial_state, neighbours, cost)
# that takes an initial state and two functions to compute the neighbours
# and cost of a state, and then iteratively improves the state until a local
# minimum (which may be global) is reached.
# The function must return the list of states it goes through
# (including the first and last one) in the order they are encountered.
# The algorithm should move to a new state only if the cost improves.
# If there is a tie between multiple states, the first one
# (in the order they appear in the sequence returned by neighbours) must be used.
# =============================================================================

def greedy_descent(initial_state, neighbours, cost):
    '''
    Parameters
    ----------
    initial_state : TYPE
        the state from which the search starts
    neighbours : FUNCTION
        a function that takes a state and returns a list of neighbours
    cost : FUNCTION
        a function that takes a state returns its cost (e.g. number of conflicts).

    Returns
    -------
    None.

    '''
    change = True
    minCost = cost(initial_state)
    minState = [initial_state]
    possMinState = None
    
    
    while change == True:
        change = False
        possibleStates = neighbours(minState[-1])
        
        for i in range(len(possibleStates)):
            stateCost = cost(possibleStates[i])
            if stateCost < minCost:
                minCost = stateCost
                possMinState = possibleStates[i]
                change = True
                
        if minState[-1] != possMinState and possMinState != None:
            minState.append(possMinState)
                
    
    return tuple(minState)
        
# =============================================================================
# 
# def cost(x):
#     return x**2
# 
# def neighbours(x):
#     return [x - 1, x + 1]
# 
# for state in greedy_descent(4, neighbours, cost):
#     print(state)
#     
# 
# def cost(x):
#     return x**2
# 
# def neighbours(x):
#     return [x - 1, x + 1]
# 
# for state in greedy_descent(-6.75, neighbours, cost):
#     print(state)
# 
# 
# def cost(x):
#     return x**2
# 
# def neighbours(x):
#     return [x - 1, x + 1, x - 2, x + 2]
# 
# for state in greedy_descent(-6.75, neighbours, cost):
#     print(state)
#     
# 
# def cost(state):
#     x, y = state
#     return abs(x) + abs(y)
# 
# def neighbours(state):
#     x, y = state
#     return [(x - 1, y - 1),
#             (x - 1, y + 1),
#             (x + 1, y - 1),
#             (x + 1, y + 1),]
# 
# for state in greedy_descent((0,8), neighbours, cost):
#     print(state)
# =============================================================================
