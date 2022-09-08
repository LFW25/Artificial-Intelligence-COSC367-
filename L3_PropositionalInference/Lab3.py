# -*- coding: utf-8 -*-
"""
Created on Sat Aug  6 10:49:51 2022

@author: OEM
"""

import re
from search import *


class DFSFrontier(Frontier):
    """Implements a frontier container appropriate for depth-first
    search."""

    def __init__(self):
        """The constructor takes no argument. It initialises the
        container to an empty stack."""
        self.container = []

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

def clauses(knowledge_base):
    """Takes the string of a knowledge base; returns an iterator for pairs
    of (head, body) for propositional definite clauses in the
    knowledge base. Atoms are returned as strings. The head is an atom
    and the body is a (possibly empty) list of atoms.

    -- Kourosh Neshatian - 31 Jul 2019

    """
    ATOM   = r"[a-z][a-zA-z\d_]*"
    HEAD   = rf"\s*(?P<HEAD>{ATOM})\s*"
    BODY   = rf"\s*(?P<BODY>{ATOM}\s*(,\s*{ATOM}\s*)*)\s*"
    CLAUSE = rf"{HEAD}(:-{BODY})?\."
    KB     = rf"^({CLAUSE})*\s*$"

    assert re.match(KB, knowledge_base)

    for mo in re.finditer(CLAUSE, knowledge_base):
        yield mo.group('HEAD'), re.findall(ATOM, mo.group('BODY') or "")

def forward_deduce(kb):
    '''
    takes the string of a knowledge base containing propositional definite
    clauses and returns a (complete) set of atoms (strings) that can be
    derived (to be true) from the knowledge base

    '''
    kbInterp = list(clauses(kb))        # Clean the clauses list using the provided clauses function
    proven = []
    newAtomAdded = True
    
    while newAtomAdded != False:

        newAtomAdded = False
        for tup in kbInterp:            # Iterate through each clause in the knowledge base

            head, body = tup[0], tup[1]
            isProven = False
            
            for el in body:             # For each element on the RHS (the body)
                if el in proven:        # Check if each element has already been proven
                    isProven = True     # If all the elements are proven, you can add the head
                else:
                    isProven = False
            
            if (isProven == True or len(body) == 0) and head not in proven:
                # If all body elements are proven (or there are no body elements)
                # and the head is not already in the proven list
                proven.append(head) # Add it to the list
                newAtomAdded = True     # Tell the while loop to go through the clauses again 
                                        # because there's new proven information
                
    return set(proven)

class KBGraph(Graph):
    def __init__(self, kb, query):
        self.clauses = list(clauses(kb))
        self.query = query

    def starting_nodes(self):
        
        return [list(self.query)]
        
    def is_goal(self, node):
        return len(node) == 0

    def outgoing_arcs(self, body):
        outgoingArcs =  []
        
        bodyEl = body[0]                  # For each element in the body
        for clause in self.clauses:             # For each clause in the knowledge base
            if bodyEl == clause[0]:            # If a body element matches the head of a clause

                newBody = clause[1] + body[1:]           # Replace the body element with the clause
                    
                outgoingArcs.append(Arc(body, newBody, "aajhajg", 1))
                    
        return outgoingArcs


            

kb = """
a :- b, c.
b :- d, e.
b :- g, e.
c :- e.
d.
e.
f :- a,
     g.
"""

query = {'a'}
if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
    print("The query is true.")
else:
    print("The query is not provable.")
    


kb = """
a :- b, c.
b :- d, e.
b :- g, e.
c :- e.
d.
e.
f :- a,
     g.
"""

query = {'a', 'b', 'd'}
if next(generic_search(KBGraph(kb, query), DFSFrontier()), None):
    print("The query is true.")
else:
    print("The query is not provable.")