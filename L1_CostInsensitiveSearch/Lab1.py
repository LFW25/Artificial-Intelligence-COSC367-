# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 10:32:23 2022

@author: Lily
"""

"""This module contains classes and functions related to graph
search. It is specifically written for the course COSC367: Artificial
Intelligence. Most of the code here is abstract.  The normal usage is
to write concrete subclasses for particular problems.

Author: Kourosh Neshatian
Last modified: 13 Jul 2019

"""

#%% Question 8
from search import *

class DFSFrontier(Frontier):
    """Implements a frontier container appropriate for depth-first
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = deque([])

    def add(self, path):
        self.container.append(path)

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self
        
    def __next__(self):
        if len(self.container) > 0:
            return self.container.pop(-1)
        else:
            raise StopIteration   # don't change this one


#%% Question 9
from search import *
from collections import deque 

class BFSFrontier(Frontier):
    """Implements a frontier container appropriate for breadth-first
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = deque([])

    def add(self, path):
        self.container.append(path)

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self
        
    def __next__(self):
        if len(self.container) > 0:
            return self.container.popleft()
        else:
            raise StopIteration   # don't change this one

#%% Question 10
from search import *
from collections import deque

class BFSFrontier(Frontier):
    """Implements a frontier container appropriate for breadth-first
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = deque([])

    def add(self, path):
        self.container.append(path)

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self
        
    def __next__(self):
        if len(self.container) > 0:
            return self.container.popleft()
        else:
            raise StopIteration   # don't change this one

class FunkyNumericGraph(Graph):
    """A graph where nodes are numbers. A number n leads to n-1 and
    n+2. Nodes that are divisible by 10 are goal nodes."""
    
    def __init__(self, starting_number):
        self.starting_number = starting_number

    def outgoing_arcs(self, tail_node):
        """Takes a node (which is an integer in this problem) and returns
        outgoing arcs (always two arcs in this problem)"""
        return [Arc(tail_node, tail_node - 1, action="1down", cost=1),
                Arc(tail_node, tail_node + 2, action = "2up", cost=1)]
        
    def starting_nodes(self):
        """Returns a sequence (list) of starting nodes. In this problem
        the sequence always has one element."""
        return [self.starting_number]

    def is_goal(self, node):
        """Determine whether a given node (integer) is a goal."""
        return node % 10 == 0


#%% Question 11
from search import *
from collections import deque
import copy

BLANK = ' '

class SlidingPuzzleGraph(Graph):
    """Objects of this type represent (n squared minus one)-puzzles.
    """

    def __init__(self, starting_state):
        self.starting_state = starting_state

    def outgoing_arcs(self, state):
        """Given a puzzle state (node) returns a list of arcs. Each arc
        represents a possible action (move) and the resulting state."""
        
        n = len(state) # the size of the puzzle
        
        # Find i and j such that state[i][j] == BLANK
        i, j = 0, 0
        
        for x in range(0, n):
            for y in range(0, n):
                if state[x][y] == ' ':
                    i = x
                    j = y
        
        arcs = []
        if i > 0:
            action = "Move {} down".format(state[i-1][j]) # or blank goes up
            new_state = copy.deepcopy(state) 
            new_state[i][j], new_state[i-1][j] = new_state[i-1][j], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        if i < n - 1:
            action = "Move {} up".format(state[i+1][j]) # or blank goes down
            new_state = copy.deepcopy(state) 
            new_state[i][j], new_state[i+1][j] = new_state[i+1][j], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        if j > 0:
            action = "Move {} right".format(state[i][j-1]) # or blank goes left
            new_state = copy.deepcopy(state) 
            new_state[i][j], new_state[i][j-1] = new_state[i][j-1], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        if j < n - 1:
            action = "Move {} left".format(state[i][j+1]) # or blank goes left
            new_state = copy.deepcopy(state) 
            new_state[i][j], new_state[i][j+1] = new_state[i][j+1], BLANK
            arcs.append(Arc(state, new_state, action, 1))
        return arcs

    def starting_nodes(self):
        return [self.starting_state]
    
    def is_goal(self, state):
        """Returns true if the given state is the goal state, False
        otherwise. There is only one goal state in this problem."""
        
        n = len(state)
        checkValue = 0
        
        for x in range(0, n):
            for y in range(0, n):
                if checkValue == 0:
                    if state[x][y] != ' ':
                        return False
                    else:
                        checkValue += 1
                else:
                    if state[x][y] == checkValue:
                        checkValue+= 1
                    else:
                        return False
        
        return True
        

class BFSFrontier(Frontier):
    """Implements a frontier container appropriate for breadth-first
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = deque([])

    def add(self, path):
        self.container.append(path)

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self
        
    def __next__(self):
        if len(self.container) > 0:
            return self.container.popleft()
        else:
            raise StopIteration   # don't change this one
            
            
graph = SlidingPuzzleGraph([[1, 2, 5],
                            [3, 4, 8],
                            [6, 7, ' ']])

solutions = generic_search(graph, BFSFrontier())
print_actions(next(solutions))