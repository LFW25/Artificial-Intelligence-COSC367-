# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 11:47:09 2022

@author: Lily Williams
"""

# =============================================================================
# Write a procedure greedy_descent_with_random_restart(random_state, neighbours, cost) that takes three functions,
# one to get a new random state and two to compute the neighbours or cost of a state
# and then uses greedy_descent (you wrote earlier) to find a solution.
# The first state in the search must be obtained by calling the function random_state.
# The procedure must print each state it goes through (including the first and last one) in the order they are encountered.
# When the search reaches a local minimum that is not global, the procedure must print RESTART and restart the search by calling random_state
# =============================================================================
from Q1_nQueensNeighbours import n_queens_neighbours as neighbours
from Q2_nQueensCost import n_queens_cost as cost
from Q3_greedyDescent import greedy_descent

def greedy_descent_with_random_restart(random_state, neighbours, cost):
    '''
    Parameters
    ----------
    random_state : Tuple
        a function that takes no argument and return a random state;.
    neighbours : FUNCTION
        a function that takes a state and returns a list of neighbours;.
    cost : FUNCTION
        a function that takes a state returns its cost (e.g. number of conflicts).

    Returns
    -------
    None.

    '''
    
    initialState = random_state()
    sequence = greedy_descent(initialState, neighbours, cost)
    
    for tup in sequence:
        print(tup)
    
    localMinCost = cost(sequence[-1])
    
    while localMinCost > 0:
        print('RESTART')
        initialState = random_state()
        sequence = greedy_descent(initialState, neighbours, cost)
        
        for tup in sequence:
            print(tup)
        
        localMinCost = cost(sequence[-1])




import random

N = 6
random.seed(0)

def random_state():
    return tuple(random.sample(range(1,N+1), N))   

greedy_descent_with_random_restart(random_state, neighbours, cost)


N = 8
random.seed(0)

def random_state():
    return tuple(random.sample(range(1,N+1), N))   

greedy_descent_with_random_restart(random_state, neighbours, cost)