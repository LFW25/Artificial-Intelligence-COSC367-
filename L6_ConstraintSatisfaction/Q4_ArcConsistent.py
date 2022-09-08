# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 15:46:58 2022

@author: lilyw
"""


# =============================================================================
# Write a function arc_consistent that takes a CSP object
# and returns a new CSP object that is arc consistent
# (and also consequently domain consistent).
# =============================================================================


import itertools, copy 
from csp import *

def arc_consistent(csp):
    csp = copy.deepcopy(csp)
    # x is a Variable
    # c is a Constraint
    to_do = {(x, c) for c in csp.constraints for x in scope(c)}
    while to_do:
        x, c = to_do.pop()
        ys = scope(c) - {x}
        new_domain = set()
        for xval in csp.var_domains[x]:
            assignment = {x: xval}
            for yvals in itertools.product(*[csp.var_domains[y] for y in ys]):
                assignment.update({y: yval for y, yval in zip(ys, yvals)})
                if satisfies(assignment, c):
                    new_domain.add(xval)
                    break
        if csp.var_domains[x] != new_domain:
            for cprime in set(csp.constraints) - {c}:
                # cprime is another Constraint
                if x in scope(cprime):
                   for z in scope(cprime):
                       # z is another Variable
                       if x != z:
                           to_do.add((z, cprime))
            csp.var_domains[x] = new_domain
    return csp


# =============================================================================
# Test Cases
# =============================================================================

simple_csp = CSP(
    var_domains={x: set(range(1, 5)) for x in 'abc'},
    constraints={
        lambda a, b: a < b,
        lambda b, c: b < c,
        })

csp = arc_consistent(simple_csp)
for var in sorted(csp.var_domains.keys()):
    print("{}: {}".format(var, sorted(csp.var_domains[var])))
    
    
csp = CSP(var_domains={x:set(range(10)) for x in 'abc'},
          constraints={lambda a,b,c: 2*a+b+2*c==10}) 

csp = arc_consistent(csp)
for var in sorted(csp.var_domains.keys()):
    print("{}: {}".format(var, sorted(csp.var_domains[var])))