'''
Consider two medical tests, A and B, for a virus.
Test A is 95% effective at recognising the virus when the virus is present,
but has a 10% false positive rate (indicating that the virus is present, when it is not).
Test B is 90% effective at recognizing the virus, but has a 5% false positive rate. 
The two tests use independent methods of identifying the virus.
The virus is carried by 1% of all people.

Express these facts in the form of a (causal) belief network.
Use variable names 'A',  'B', and 'Virus'. Assign the network to the variable network.
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

    'Virus': {
        'Parents': [],
        'CPT': {
            (): 1/100,
            }},

    'A': {
        'Parents': ['Virus'],
        'CPT': {
            (True,): 95/100,
            (False,): 10/100 
            }},
            
    'B': {
        'Parents': ['Virus'],
        'CPT': {
            (True,): 90/100,
            (False,): 5/100,
            }},

    }

answer = query(network, 'Virus', {'A': True})
print("The probability of carrying the virus\n"
      "if test A is positive: {:.5f}"
      .format(answer[True]))
    

answer = query(network, 'Virus', {'B': True})
print("The probability of carrying the virus\n"
      "if test B is positive: {:.5f}"
      .format(answer[True]))