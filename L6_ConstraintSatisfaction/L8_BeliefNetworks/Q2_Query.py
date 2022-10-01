'''
Write a function query(network, query_var, evidence) that given a belief network,
the name of a variable in the network, and some evidence,
returns the distribution of query_var.
The parameter network is a belief network whose data structure was described earlier.
The parameter query_var is the name of the variable we are interested in and is of type string.
The parameter evidence is a dictionary whose elements are assignments to some variables in the network;
the keys are the name of the variables and the values are Boolean.

The function must return a pair of real numbers
where the first element is the probability of query_var being false given the evidence
and the second element is the probability of query_var being true given the evidence.
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
            (): 0.2
            }},
}

answer = query(network, 'A', {})
print("P(A=true) = {:.5f}".format(answer[True]))
print("P(A=false) = {:.5f}".format(answer[False]))

network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.1
            }},
            
    'B': {
        'Parents': ['A'],
        'CPT': {
            (True,): 0.8,
            (False,): 0.7,
            }},
    }
 
answer = query(network, 'B', {'A': False})
print("P(B=true|A=false) = {:.5f}".format(answer[True]))
print("P(B=false|A=false) = {:.5f}".format(answer[False]))