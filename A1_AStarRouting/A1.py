# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 11:37:01 2022

@author: Lily Williams
"""

from search import *
import math
import heapq as hp

DEFAULT_MOVE_COST = 5
QUESTION_TWO_ECTG = False

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

 

class RoutingGraph(Graph):
    
    def __init__(self, mapString):
        
        mapList = mapString.strip('\t').splitlines()
        for i, row in enumerate(mapList):
            mapList[i] = row.strip('\t')
        
        
        startNodes = []
        goalNodes = []
        portalNodes = []
        
        numRows = len(mapList)
        numCols = len(mapList[0])
        
        for row in range(numRows - 1):
            
            for col in range(numCols - 1):
                
                currentChar = mapList[row][col]
                
                if currentChar == 'S': # Solar Agent
                
                    startNodes.append((row, col, math.inf))
                    
                elif currentChar.isdigit() == True: # Gas Agent
                
                    startNodes.append((row, col, int(currentChar)))
                
                elif currentChar == 'G': # Goal
                
                    goalNodes.append((row, col))
                
                elif currentChar == 'P': # Portal
                    portalNodes.append((row, col))

        
        
        self.mapList = mapList
        
        self._startNodes = startNodes
        self.goalNodes = goalNodes
        self.portalNodes = portalNodes


                    
    def starting_nodes(self):
        
        return self._startNodes
        

    def is_goal(self, node):
        
        mapList = self.mapList
        row, col = node[0], node[1]
        return mapList[row][col] == 'G'

    
    def outgoing_arcs(self, node):
        
        row, col, fuel = node[0], node[1], node[2]
        mapList = self.mapList
        portalNodes = self.portalNodes
        
        moves = [('N' , -1, 0),
                 ('E' ,  0, 1),
                 ('S' ,  1, 0),
                 ('W' ,  0, -1)]
        
        obstacles = ['+', '|', '-', 'X']
        outgoingArcs = []
        
        if fuel > 0:
            # Add Regular moves
            for direction in moves:
                dAction, rowMove, colMove = direction
                if mapList[row + rowMove][col + colMove] not in obstacles:
                    outgoingArcs.append(Arc(tail = node, head=(row + rowMove, col + colMove, fuel - 1), action = dAction, cost = 5))
                    
        # Add Portals
        if mapList[row][col] == 'P':
            for portal in portalNodes:
                if portal != (row, col):
                    outgoingArcs.append(Arc(tail = node, head=(portal[0], portal[1], fuel), action = 'Teleport to {}'.format(portal), cost = 10))
        
        # Add Fuel-Ups
        if mapList[row][col] == 'F' and fuel < 9:
            outgoingArcs.append(Arc(tail = node, head=(node[0], node[1], 9), action = 'Fuel up', cost = 15))
        
        return outgoingArcs
    
    def estimated_cost_to_goal(self, node):
        if QUESTION_TWO_ECTG == True:
            return 0
        else:
            # Since the agent can only move vertically/horizontally, use Manhattan distance
            
            NodeRow, NodeCol, fuel = node
            goalDistances = []
            
            for goalNode in self.goalNodes:
                goalRow, goalCol = goalNode
                goalDistances.append(abs(goalRow - NodeRow) + abs(goalCol - NodeCol))
                
            return min(goalDistances)*DEFAULT_MOVE_COST


class AStarFrontier(Frontier):
    """Implements a frontier container appropriate for an A* Search Algorithm."""

    def __init__(self,  graph):
        """The constructor takes no argument. It initialises the
        container to an empty heap."""
        self.itemIter = 0
        self.container = []
        self.graph = graph
        
        # Keep track of expanded nodes for pruning purposes
        self.expandedSet = []

    def add(self, path):
        expandedSet = self.expandedSet
        graph = self.graph
        
        if path[-1].head not in expandedSet:  # Implement the pruning
        # Don't expand any nodes that have already been looked at
            self.itemIter += 1
            cost = 0
                    
            for arc in path:
                cost += arc.cost
                        
            cost += graph.estimated_cost_to_goal(path[-1].head)  # Estimated cost to goal = 0 for Q2
                    
            hp.heappush(self.container, (cost, self.itemIter, path)) 

    def __iter__(self):
        """The object returns itself because it is implementing a __next__
        method and does not need any additional state for iteration."""
        return self
        
    def __next__(self):
        
        expandedSet = self.expandedSet
        
        
        if self.container:
            path = hp.heappop(self.container)[-1]
            
            while path[-1].head in expandedSet:
                if len(self.container) > 0:
                    path = hp.heappop(self.container)[-1]
                else:
                    raise StopIteration
                
            if path[-1].head not in expandedSet:
                # Add node to expanded set
                expandedSet.append(path[-1].head)
    
            return path
        
        else:
            raise StopIteration   # don't change this one
    
    
def print_map(map_graph, frontier, solution):
    '''
    Takes three parameters: an instance of RoutingGraph, an instance of AStarFrontier which has just been used to run a graph search on the given graph, and the result of the search, and then prints a map such that:
    
        - the position of the walls, obstacles, agents, and the goal points are all unchanged and they are marked by the same set of characters as in the original map string;
        - those free spaces (space characters) that have been expanded during the search are marked with a '.' (a period character); and
        - those free spaces (spaces characters) that are part of the solution (best path to the goal) are marked with '*' (an asterisk character).
    
    '''
    for expandedNode in frontier.expandedSet:
        if expandedNode is not None:
            row, col, cost = expandedNode
            
            currentChar = map_graph.mapList[row][col]
            if currentChar not in ['G', 'S'] and not currentChar.isdigit():
                # Replace currentChar in map with '.'
                currentRow = map_graph.mapList[row]
                newRow = currentRow[:col] + '.' + currentRow[col+1:]
                map_graph.mapList[row] = newRow

    if solution is not None:
        for solutionNode in solution:
            row, col, fuel = solutionNode.head
            
            currentChar = map_graph.mapList[row][col]
            
            if currentChar not in ['G', 'S'] and not currentChar.isdigit():
                # Replace currentChar in map with '*'
                currentRow = map_graph.mapList[row]
                newRow = currentRow[:col] + '*' + currentRow[col+1:]
                map_graph.mapList[row] = newRow
    
    for row in map_graph.mapList:
        print(row)
            
    
#%%    Q1 TEST CASES
# =============================================================================
# map_str = """\
# +-------+
# |  9  XG|
# |X XXX P|
# | S  0FG|
# |XX P XX|
# +-------+
# """
# 
# graph = RoutingGraph(map_str)
# 
# print("Starting nodes:", sorted(graph.starting_nodes()))
# print("Outgoing arcs (available actions) at starting states:")
# for s in sorted(graph.starting_nodes()):
#     print(s)
#     for arc in graph.outgoing_arcs(s):
#         print ("  " + str(arc))
# 
# node = (1,1,5)
# print("\nIs {} goal?".format(node), graph.is_goal(node))
# print("Outgoing arcs (available actions) at {}:".format(node))
# for arc in graph.outgoing_arcs(node):
#     print ("  " + str(arc))
# 
# node = (1,7,2)
# print("\nIs {} goal?".format(node), graph.is_goal(node))
# print("Outgoing arcs (available actions) at {}:".format(node))
# for arc in graph.outgoing_arcs(node):
#     print ("  " + str(arc))
# 
# node = (3, 7, 0)
# print("\nIs {} goal?".format(node), graph.is_goal(node))
# 
# node = (3, 7, math.inf)
# print("\nIs {} goal?".format(node), graph.is_goal(node))
# 
# node = (3, 6, 5)
# print("\nIs {} goal?".format(node), graph.is_goal(node))
# print("Outgoing arcs (available actions) at {}:".format(node))
# for arc in graph.outgoing_arcs(node):
#     print ("  " + str(arc))
# 
# node = (3, 6, 9)
# print("\nIs {} goal?".format(node), graph.is_goal(node))
# print("Outgoing arcs (available actions) at {}:".format(node))
# for arc in graph.outgoing_arcs(node):
#     print ("  " + str(arc))
# 
# node = (2, 7, 4)  # at a location with a portal
# print("\nOutgoing arcs (available actions) at {}:".format(node))
# for arc in graph.outgoing_arcs(node):
#     print ("  " + str(arc))
# =============================================================================

#%%    Q2 TEST CASES

# =============================================================================
# from search import *
# 
# map_str = """\
# +-------+
# |   G   |
# |       |
# |   S   |
# +-------+
# """
# 
# map_graph = RoutingGraph(map_str)
# frontier = AStarFrontier(map_graph)
# solution = next(generic_search(map_graph, frontier), None)
# print_actions(solution)
# 
# 
# map_str = """\
# +-------+
# |  GG   |
# |S    G |
# |  S    |
# +-------+
# """
# 
# map_graph = RoutingGraph(map_str)
# frontier = AStarFrontier(map_graph)
# solution = next(generic_search(map_graph, frontier), None)
# print_actions(solution)
# 
# 
# map_str = """\
# +-------+
# |     XG|
# |X XXX  |
# | S     |
# +-------+
# """
# 
# map_graph = RoutingGraph(map_str)
# frontier = AStarFrontier(map_graph)
# solution = next(generic_search(map_graph, frontier), None)
# print_actions(solution)
# 
# map_str = """\
# +-------+
# |  F  X |
# |X XXXXG|
# | 3     |
# +-------+
# """
# 
# map_graph = RoutingGraph(map_str)
# frontier = AStarFrontier(map_graph)
# solution = next(generic_search(map_graph, frontier), None)
# print_actions(solution)
# 
# map_str = """\
# +--+
# |GS|
# +--+
# """
# map_graph = RoutingGraph(map_str)
# frontier = AStarFrontier(map_graph)
# solution = next(generic_search(map_graph, frontier), None)
# print_actions(solution)
# 
# map_str = """\
# +---+
# |GF2|
# +---+
# """
# map_graph = RoutingGraph(map_str)
# frontier = AStarFrontier(map_graph)
# solution = next(generic_search(map_graph, frontier), None)
# print_actions(solution)
# 
# 
# map_str = """\
# +---------+
# |         |
# |    G    |
# |         |
# +---------+
# """
# 
# map_graph = RoutingGraph(map_str)
# frontier = AStarFrontier(map_graph)
# solution = next(generic_search(map_graph, frontier), None)
# print_actions(solution)
# 
# 
# map_str = """\
# +------------+
# |    P       |
# | 7          |
# |XXXX        |
# |P F X  G    |
# +------------+
# """
# 
# map_graph = RoutingGraph(map_str)
# frontier = AStarFrontier(map_graph)
# solution = next(generic_search(map_graph, frontier), None)
# print_actions(solution)
# 
# 
# map_str = """\
# +----------+
# |    X     |
# | S  X  G  |
# |    X     |
# +----------+
# """
# 
# map_graph = RoutingGraph(map_str)
# frontier = AStarFrontier(map_graph)
# solution = next(generic_search(map_graph, frontier), None)
# print_actions(solution)
# 
# map_str = """\
# +----------------+
# |2              F|
# |XX     G 123    |
# |3XXXXXXXXXXXXXX |
# |  F             |
# |          F     |
# +----------------+
# """
# 
# map_graph = RoutingGraph(map_str)
# frontier = AStarFrontier(map_graph)
# solution = next(generic_search(map_graph, frontier), None)
# print_actions(solution)
# =============================================================================
#%%    Q3 TEST CASES

from search import *

map_str = """\
+----------------+
|                |
|                |
|                |
|                |
|                |
|                |
|        S       |
|                |
|                |
|     G          |
|                |
|                |
|                |
+----------------+
"""

map_graph = RoutingGraph(map_str)
frontier = AStarFrontier(map_graph)
solution = next(generic_search(map_graph, frontier), None)
print_map(map_graph, frontier, solution)


map_str = """\
+----------------+
|                |
|                |
|                |
|                |
|                |
|                |
|        S       |
|                |
|                |
|     G          |
|                |
|                |
|                |
+----------------+
"""


map_graph = RoutingGraph(map_str)
# changing the heuristic so the search behaves like LCFS
map_graph.estimated_cost_to_goal = lambda node: 0

frontier = AStarFrontier(map_graph)

solution = next(generic_search(map_graph, frontier), None)
print_map(map_graph, frontier, solution)

map_str = """\
+---------------+
|    G          |
|XXXXXXXXXXXX   |
|           X   |
|  XXXXXX   X   |
|  X S  X   X   |
|  X        X   |
|  XXXXXXXXXX   |
|               |
+---------------+
"""

map_graph = RoutingGraph(map_str)
frontier = AStarFrontier(map_graph)
solution = next(generic_search(map_graph, frontier), None)
print_map(map_graph, frontier, solution)