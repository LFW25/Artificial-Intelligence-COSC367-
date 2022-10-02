#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 11:04:40 2022

@author: lfw25

Bayesian Spam Filter

Write a function learn_likelihood(file_name, pseudo_count=0)
that takes the file name of a training set (for the spam detection problem) and an optional pseudo-count parameter
and returns a sequence of pairs of likelihood probabilities.
As described in the representation of likelihood, the length of the returned sequence (list or tuple) must be 12.
Each element in the sequence is a pair (tuple) of real numbers such that likelihood[i][False] is P(X[i]=true|Spam=false) and likelihood[i][True] is P(X[i]=true|Spam=true ).
"""

import csv

def learn_likelihood(file_name, pseudo_count = 0):
    
    with open(file_name) as in_file:
        training_examples = [tuple(row) for row in csv.reader(in_file)]
    
    numCols = len(training_examples[0])
    rawLike = [[0, 0, 0, 0] for n in range(numCols - 1)]
    
    for i in range(len(training_examples)):
        row = training_examples[i]
        
        if row[-1] not in ['0', '1']:
            pass
        
        else:

            # Determine SPAM value
            yVal = int(row[-1]) # SPAM False --> yVal = 0; SPAM True --> yVal = 1
            
            for j in range(numCols - 1): # For each of the 12 variables
                if row[j] == '1':
                    # Variable is True, add to count
                    rawLike[j][yVal] += 1
                    
                if yVal == 1:
                    # If SPAM is True, add to [2]th element
                    rawLike[j][2] += 1
                else:
                    # SPAM False, add to [3]th element
                    rawLike[j][3] += 1
    
    likelihoods = []
    #print(rawLike)
    for k in range(len(rawLike)):
        variable = rawLike[k]
        
        spamTrue = (variable[1] + pseudo_count) / (variable[2] + pseudo_count * 2)
        spamFalse = (variable[0] + pseudo_count) / (variable[3] + pseudo_count * 2)
        
        likelihoods.append((spamFalse, spamTrue))
    
    return likelihoods
                    
                



likelihood = learn_likelihood("spam-labelled.csv")
print(len(likelihood))
print([len(item) for item in likelihood])



likelihood = learn_likelihood("spam-labelled.csv")
print("P(X1=True | Spam=False) = {:.5f}".format(likelihood[0][False]))
print("P(X1=False| Spam=False) = {:.5f}".format(1 - likelihood[0][False]))
print("P(X1=True | Spam=True ) = {:.5f}".format(likelihood[0][True]))
print("P(X1=False| Spam=True ) = {:.5f}".format(1 - likelihood[0][True]))


likelihood = learn_likelihood("spam-labelled.csv", pseudo_count=1)
print("With Laplacian smoothing:")
print("P(X1=True | Spam=False) = {:.5f}".format(likelihood[0][False]))
print("P(X1=False| Spam=False) = {:.5f}".format(1 - likelihood[0][False]))
print("P(X1=True | Spam=True ) = {:.5f}".format(likelihood[0][True]))
print("P(X1=False| Spam=True ) = {:.5f}".format(1 - likelihood[0][True]))