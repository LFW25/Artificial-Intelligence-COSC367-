# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 15:40:42 2022

@author: Lily Williams
"""

# =============================================================================
# Write a function n_queens_neighbours(state) that takes a state (total assignment)
# for an n-queen problem and returns a sorted list of states that are the neighbours of the current assignment.
# A neighbour is obtained by swapping the position of two numbers in the given permutation.
# 
# The number at index i of the array indicates the row number of the object at column i (or the column number of the object at row i).
# =============================================================================
import itertools

def n_queens_neighbours(state):
    '''
    Parameters
    ----------
    state : Tuple
        Position of a queen in the n-Queens problem

    Returns
    -------
    neighboursList : List of Tuples
        Possible neighbours of the original setup
    '''
    
    neighboursList = []

    for firstEl, secondEl in itertools.combinations(range(len(state)), 2):
        newState = list(state)
        newState[firstEl], newState[secondEl] = newState[secondEl], newState[firstEl]
        neighboursList.append(tuple(newState))
    return sorted(neighboursList)
            
# =============================================================================
#             
# 
# print(n_queens_neighbours((1, 2)) == [(2, 1)])
# 
# print(n_queens_neighbours((1, 3, 2)) == [(1, 2, 3), (2, 3, 1), (3, 1, 2)])
# 
# print(n_queens_neighbours((1, 2, 3)) == [(1, 3, 2), (2, 1, 3), (3, 2, 1)])
# 
# print(n_queens_neighbours((1,)) == [])
# =============================================================================
