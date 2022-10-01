# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 12:09:34 2022

@author: OEM
"""

# =============================================================================
# Write a function roulette_wheel_select(population, fitness, r) that takes a list of individuals,
# fitness function, and a floating-point random number r in the interval [0, 1), 
# and selects and returns an individual from the population using the roulette wheel selection mechanism.
# The fitness function (which will be provided as an argument) takes an individual and returns a non-negative number as its fitness.
# The higher the fitness the better. When constructing the roulette wheel, do not change the order of individuals in the population.
# =============================================================================

def roulette_wheel_select(population, fitness, r):
    '''
    

    Parameters
    ----------
    population : LIST
        A list of inividuals.
    fitness : FUNCTION
        Determines the fitness of a given individual.
    r : FLOAT
        A float between 0 and 1.

    Returns
    -------
    None.

    '''
    

    
    totFitSum = 0
    for person in population:
        totFitSum += fitness(person)

    randomNum = r*totFitSum
    
    fitnessSum = 0
    for person in population:
        #print("Person {}, Sum {}.".format(person, fitnessSum))
        fitnessSum += fitness(person)
        if fitnessSum >= randomNum:
            return person
    
    

population = ['a', 'b']

def fitness(x):
    return 1 # everyone has the same fitness

for r in [0, 0.33, 0.49999, 0.51, 0.75, 0.99999]:
    print(roulette_wheel_select(population, fitness, r))
    
    

population = [0, 1, 2]

def fitness(x):
    return x

for r in [0.001, 0.33, 0.34, 0.5, 0.75, 0.99]:
    print(roulette_wheel_select(population, fitness, r))


population = ['cosc']

def fitness(x):
    return 50

for r in [0, 0.33, 0.49999, 0.5, 0.75, 0.99999]:
    print(roulette_wheel_select(population, fitness, r))


population = [1, 2, 3, 4, 5]

def fitness(x):
    return x

for r in range(14):
    print(roulette_wheel_select(population, fitness, r/14))