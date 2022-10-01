'''
Consider the belief network given with three random variables A, B, and C.
The topology of the network implies the following:

- A influences B
- A influences C
- B and C are conditionally independent given A

network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.1
            }},
    'B': {
        'Parents': ['A'],
        'CPT': {
            (False,): 0.2,
            (True,): 0.3
            }},
            
    'C': {
        'Parents': ['A'],
        'CPT': {
            (False,): 0.4,
            (True,): 0.5
            }},
}

Without modifying the topology of the network, change the CPTs such that B and C become independent (unconditionally).
'''

from itertools import product

def joint_prob(network, assignment):
    p = 1

    for variable in network:
        varList = []

        parent = network[variable].get("Parents")
        if parent:
            for eachVariable in parent:
                varList.append(assignment.get(eachVariable))
            probUpdate = network[variable].get('CPT').get(tuple(varList))
        else:
            probUpdate = network[variable].get('CPT').get(())
        
        if not assignment.get(variable):
            probUpdate = 1 - probUpdate
        
        p *= probUpdate
    
    return p

def query(network, query_var, evidence):
    
    # If you wish you can follow this template
    
    # Find the hidden variables
    hiddenVars = network.keys() - evidence.keys() - {query_var}

    # Initialise a raw distribution to [0, 0]
    rawDist = {True:0, False:0}

    assignment = dict(evidence) # create a partial assignment
    for query_value in {True, False}:
        # Update the assignment to include the query variable
        assignment[query_var] = query_value;
        assigmentRef = assignment[query_var]

        for values in product((True, False), repeat=len(hiddenVars)):
            # Update the assignment (we now have a complete assignment)
            hiddenAss = {var:val for var, val in zip(hiddenVars, values)}
            assignment.update(hiddenAss)
            
            # Update the raw distribution by the probability of the assignment.
            rawDist[query_value] += joint_prob(network, assignment)

    # Normalise the raw distribution and return it
    normVal = 1/(rawDist[True] + rawDist[False])
    rawDist[True] *= normVal
    rawDist[False] *= normVal

    return rawDist

network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.1
            }},
    'B': {
        'Parents': ['A'],
        'CPT': {
            (False,): 0.7,
            (True,): 0.7
            }},
            
    'C': {
        'Parents': ['A'],
        'CPT': {
            (False,): 0.9,
            (True,): 0.56
            }},
}


print(sorted(network.keys()))
# ['A', 'B', 'C']

import itertools

# We use the definition of independence here. B and C are
# independent if P(B,C) = P(B) * P(C). We sum over the joint
# to determine these values.

for b,c in itertools.product({True,False}, repeat=2):
    p_b_and_c = sum(joint_prob(network,{'A':a, 'B':b, 'C':c})
                    for a in {True, False})
    p_b = sum(joint_prob(network,{'A':a, 'B':b, 'C':c})
              for a, c in itertools.product({True, False}, repeat=2))
    p_c = sum(joint_prob(network,{'A':a, 'B':b, 'C':c})
              for a, b in itertools.product({True, False}, repeat=2))
    if abs(p_b_and_c - p_b * p_c) > 1e-10:
        print("It looks like B and C are still dependent.")
        break
else:
    print("OK")
# OK