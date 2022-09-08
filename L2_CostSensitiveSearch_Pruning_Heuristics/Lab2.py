# -*- coding: utf-8 -*-
"""
Created on Sat Jul 30 11:13:21 2022

@author: OEM
"""

from search import *
from math import sqrt

#%% Question 8

class LocationGraph(Graph):
    def __init__(self, location, radius, starting_nodes, goal_nodes):
        self.location = location
        self.radius = radius
        self._starting_nodes = starting_nodes
        self.goal_nodes = goal_nodes
    
    def starting_nodes(self):
        return self._starting_nodes
    
    def is_goal(self, node):
        return node in self.goal_nodes
    
    def outgoing_arcs(self, tail):
        
        location = self.location
        
        reachable = []
        outArcs = []
        
        for node in location:
            tailX, tailY = location[tail][0], location[tail][1]
            nodeX, nodeY = location[node][0], location[node][1]
            
            difX, difY = abs(tailX - nodeX), abs(tailY - nodeY)
            dist = sqrt(difX**2 + difY**2)
            
            if dist <= self.radius and dist != 0:
                reachable.append((node, dist))
                
        reachable.sort(key = lambda x: x[0])
        
        for node in reachable:
            action = tail + '->' + node[0]
            outArcs.append(Arc(tail, node[0], action, node[1]))
        
        return outArcs
        

graph = LocationGraph(
    location={'A': (0, 0),
              'B': (3, 0),
              'C': (3, 4),
              'D': (7, 0),},
    radius = 5,
    starting_nodes=['A'],
    goal_nodes={'C'}
)

for arc in graph.outgoing_arcs('A'):
    print(arc)

print()

for arc in graph.outgoing_arcs('B'):
    print(arc)

print()

for arc in graph.outgoing_arcs('C'):
    print(arc)
    
#%% Question 9

class LCFSFrontier(Frontier):
    
    
    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty heap."""
        self.container = []

    def add(self, path):
        check = 0
        added = False
        
        for node in path:
            check += node.cost
            
        for i in range(0, len(self.container)):
            checkIter = 0
            
            for node in self.container[i]:
                checkIter += node.cost    
                
            if check < checkIter:
                self.container.insert(i, path)
                added = True
                
        if added == False:
            self.container.append(path)   

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self
        
    def __next__(self):
        if len(self.container) > 0:
            return self.container.pop(0)
        else:
            raise StopIteration   # don't change this one
    

class LocationGraph(Graph):

    def __init__(self, location, radius, starting_nodes, goal_nodes):
        self.location = location
        self.radius = radius
        self._starting_nodes = starting_nodes
        self.goal_nodes = goal_nodes
    
    def starting_nodes(self):
        return self._starting_nodes
    
    def is_goal(self, node):
        return node in self.goal_nodes
    
    def outgoing_arcs(self, tail):
        
        location = self.location
        
        reachable = []
        outArcs = []
        
        for node in location:
            tailX, tailY = location[tail][0], location[tail][1]
            nodeX, nodeY = location[node][0], location[node][1]
            
            difX, difY = abs(tailX - nodeX), abs(tailY - nodeY)
            dist = sqrt(difX**2 + difY**2)
            
            if dist <= self.radius and dist != 0:
                reachable.append((node, dist))
                
        reachable.sort(key = lambda x: x[0])
        
        for node in reachable:
            action = tail + '->' + node[0]
            outArcs.append(Arc(tail, node[0], action, node[1]))
        
        return outArcs

frontier = LCFSFrontier()
frontier.add((Arc(None, None, None, 17),))
frontier.add((Arc(None, None, None, 11), Arc(None, None, None, 4)))
frontier.add((Arc(None, None, None, 7), Arc(None, None, None, 8)))

for path in frontier:
    print(path)