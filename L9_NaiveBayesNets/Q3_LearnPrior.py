#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 10:33:54 2022

@author: lfw25

Bayesian Spam Filter

In the next three questions, you are asked to develop the learning and classification components of a naive Bayes classifier (a spam filter).

Write a function learn_prior(file_name, pseudo_count = 0) that takes the file name of the training set
and an optional pseudo-count parameter and returns a real number that is the prior probability of spam being true.
The parameter pseudo_count is a non-negative integer and it will be the same for all the attributes and all the values.
"""

import csv

def learn_prior(file_name, pseudo_count = 0):
    
    with open(file_name) as in_file:
        training_examples = [tuple(row) for row in csv.reader(in_file)]
        
    #print(training_examples)
    
    yTrueCount = 0
    yFalseCount = 0
        
    for row in training_examples:
        if row[-1] == '1':
            yTrueCount += 1
        elif row[-1] == '0':
            yFalseCount += 1
    
    prior = (yTrueCount + pseudo_count) / (yTrueCount + yFalseCount + 2 * pseudo_count)
    
    return prior




prior = learn_prior("spam-labelled.csv")
print("Prior probability of spam is {:.5f}.".format(prior))


prior = learn_prior("spam-labelled.csv")
print("Prior probability of not spam is {:.5f}.".format(1 - prior))


prior = learn_prior("spam-labelled.csv", pseudo_count = 1)
print(format(prior, ".5f"))

prior = learn_prior("spam-labelled.csv", pseudo_count = 2)
print(format(prior, ".5f"))

prior = learn_prior("spam-labelled.csv", pseudo_count = 10)
print(format(prior, ".5f"))

prior = learn_prior("spam-labelled.csv", pseudo_count = 100)
print(format(prior, ".5f"))

prior = learn_prior("spam-labelled.csv", pseudo_count = 1000)
print(format(prior, ".5f"))