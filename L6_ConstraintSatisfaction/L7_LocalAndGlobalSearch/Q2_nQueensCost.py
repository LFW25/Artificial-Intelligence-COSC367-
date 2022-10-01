# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 10:24:47 2022

@author: Lily Williams
"""

# =============================================================================
# Write a function n_queens_cost(state) that takes a state (a total assignment)
# for an n-queen problem and returns the number conflicts for that state.
# We define the number of conflicts to be the number of unordered pairs
# of queens (objects) that threaten (attack) each other.
# The state will be given in the form of a sequence (tuple more specifically).
# The state is a permutation of numbers from 1 to n (inclusive).
# The value of n must be inferred from the given state.
#
# 
# =============================================================================

def n_queens_cost(state):
    '''
    Parameters
    ----------
    state : Tuple
        .The number at index i of the array indicates the row number of the object at column i (or the column number of the object at row i).

    Returns
    -------
    None.

    '''
    stateList = list(state)
    collisions = 0
    
    for i in range(len(state)):
        firstItem = stateList[i]
        
        for j in range(i, len(state)):
            secondItem = stateList[j]
            
            if i == j:
                pass
            else:
                dx = secondItem - firstItem
                dy = j - i
                
                if abs(dx) == abs(dy):
                    collisions += 1
    
    return collisions

# =============================================================================
# 
# print(n_queens_cost((1, 2)))
# 
# print(n_queens_cost((1, 3, 2)))
# 
# print(n_queens_cost((1, 2, 3)))
# 
# print(n_queens_cost((1,)))
# 
# print(n_queens_cost((1, 2, 3, 4, 5, 6, 7, 8)))
# =============================================================================
