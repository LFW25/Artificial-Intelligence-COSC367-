# -*- coding: utf-8 -*-
"""
Created on Sun Aug 28 16:54:55 2022

@author: lilyw
"""

# =============================================================================
# Another way of representing a CSP is by a collection of relations.
# There will be one relation per constraint in the problem.
# A relation is basically a table that holds zero or more rows.
# The columns of the table are the variables that are in the scope of the constraint.
# See the documentation of the Relation class in the csp module.
# 
# For example, the following instance of CSP
# 
# 
# CSP(
#    var_domains = {var:{0,1,2} for var in 'ab'},
#    constraints = {
#       lambda a, b:  a > b,
#       lambda b: b > 0,
#    })
# can be represented in relational form as the following:
# [
#     Relation(header=['a', 'b'],
#              tuples={(2, 0),
#                      (1, 0),
#                      (2, 1)}),
#     
#     Relation(header=['b'],
#              tuples={(2,),
#                      (1,)})
# ]
# =============================================================================

from csp import Relation

# =============================================================================
# csp = CSP(
#    var_domains = {var:{-1,0,1} for var in 'abcd'},
#    constraints = {
#       lambda a, b: a == abs(b),
#       lambda c, d: c > d,
#       lambda a, b, c: a * b > c + 1
#       }
#    )
# =============================================================================

relations = [
      Relation(header=['a', 'b'],
               tuples={(1, 1),
                       (1, -1),
                       (0, 0)}),
      
      Relation(header=['c', 'd'],
               tuples={(0, -1),
                      (1, -1),
                      (1, 0)}),
      
      Relation(header=['a', 'b', 'c'],
               tuples={(1, 1, -1),
                       (-1, -1, -1)})
      
      
      ] 

relations_after_elimination = [
    Relation(header=[])
    ]

print(len(relations))
print(all(type(r) is Relation for r in relations))