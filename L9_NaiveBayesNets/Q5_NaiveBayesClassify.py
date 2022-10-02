#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 11:44:45 2022

@author: lfw25

Bayesian Spam Filter

Write a function nb_classify(prior, likelihood, input_vector)
that takes the learnt prior and likelihood probabilities and classifies an (unseen) input vector.
The input vector will be a tuple of 12 integers (each 0 or 1) corresponding to attributes X1 to X12.
The function should return a pair (tuple) where the first element is either "Spam" or "Not Spam" and the second element is the certainty.
The certainty is the (posterior) probability of spam when the instance is classified as spam, or the probability of 'not-spam' otherwise.
If spam and 'not spam' are equally likely (i.e. p=0.5) then choose 'not spam'.

This is a very simple function to implement as it only wraps the posterior function developed earlier.
"""
import csv

def posterior(prior, likelihood, observation):
    
    priorFalse = 1 - prior
    
    for i in range(0, len(likelihood)):
        # Assume prior is True
        Pi = likelihood[i][True]
        if observation[i] == False:
            Pi = 1 - Pi
        prior *= Pi
        
        # Assume prior is False 
        PiFalse = likelihood[i][False]
        if observation[i] == False:
            PiFalse = 1 - PiFalse
        priorFalse *= PiFalse
    
    # Normalise
    prior = prior/(prior + priorFalse)
        
    return prior

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

def nb_classify(prior, likelihood, input_vector):
    spamProb = posterior(prior, likelihood, input_vector)
    
    if spamProb <= 0.5:
        certainty = "Not Spam"
        spamProb = 1 - spamProb
    else:
        certainty = "Spam"
    
    return (certainty, spamProb)


prior = learn_prior("spam-labelled.csv")
likelihood = learn_likelihood("spam-labelled.csv")

input_vectors = [
    (1,1,0,0,1,1,0,0,0,0,0,0),
    (0,0,1,1,0,0,1,1,1,0,0,1),
    (1,1,1,1,1,0,1,0,0,0,1,1),
    (1,1,1,1,1,0,1,0,0,1,0,1),
    (0,1,0,0,0,0,1,0,1,0,0,0),
    ]

predictions = [nb_classify(prior, likelihood, vector) 
               for vector in input_vectors]

for label, certainty in predictions:
    print("Prediction: {}, Certainty: {:.5f}"
          .format(label, certainty))
