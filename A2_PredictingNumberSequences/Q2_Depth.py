# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 15:23:38 2022

@author: OEM

Write a function depth(expression) that takes an expression (that follows our definition of expression)
and returns the depth of the expression tree.
The depth of a tree is the depth of its deepest leaf.
"""

def depth(expression):
	if type(expression) == int or type(expression) == str:
		return 0
	else:
		return max(depth(expression[1]), depth(expression[2])) + 1


expression = 12
print(depth(expression))

expression = ['add', 12, 'x']
print(depth(expression))

expression = ['add', ['add', 22, 'y'], 'x']
print(depth(expression))