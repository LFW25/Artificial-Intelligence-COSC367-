# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 17:57:30 2022

@author: lilyw
"""

# =============================================================================
# Provide an instance of CSP class named cryptic_puzzle that represents the following cryptarithmetic problem:
# 
#   two
# + two
# ------
#  four
# The objective is to find what digit each letter can represent.
# Each letter is associated to exactly one digit and each digit is associated to up to one letter.
# The letters on the left (t and f) cannot be zero (if they were they wouldn't be there).
# =============================================================================

from csp import *
import itertools, copy 


def generate_and_test(csp):
    names, domains = zip(*csp.var_domains.items())
    for values in itertools.product(*domains):
        assignment = {x: v for x, v in zip(names, values)}
        if all(satisfies(assignment, constraint) for constraint in csp.constraints):
            yield assignment
            
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


domains = {var: set(range(10)) for var in 'twofur'}
domains.update({'carry1': {0, 1}, 'carry2': {0, 1}})

cryptic_puzzle = CSP(
    var_domains = domains,
    constraints = {
        lambda t, f: t != 0 and f != 0,
        lambda t, f, w, o, r, u: len({t, f, w, o, r, u}) == 6,
        lambda o, r, carry1: o + o == r + 10*carry1,
        lambda w, u, carry1, carry2: w + w + carry1 == u + 10 * carry2,
        lambda t, o, f, carry1, carry2: t + t + carry2 == o + 10 * f
        })

print(set("twofur") <= set(cryptic_puzzle.var_domains.keys()))
print(all(len(cryptic_puzzle.var_domains[var]) == 10 for var in "twour"))

new_csp = arc_consistent(cryptic_puzzle)
print(sorted(new_csp.var_domains['r']))

new_csp = arc_consistent(cryptic_puzzle)
print(sorted(new_csp.var_domains['w']))