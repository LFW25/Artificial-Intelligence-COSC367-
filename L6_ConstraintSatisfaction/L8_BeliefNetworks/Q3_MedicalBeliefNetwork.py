'''
Consider a medical test for a certain disease that is very rare, striking only 1 in 100,000 people.
Suppose the probability of testing positive if the person has the disease is 99%, as is the probability of testing negative when the person does not have the disease.

Express these facts in the form of a (causal) belief network.
Use variable names 'Disease' and 'Test'. Assign the network to the variable network.
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
    'Disease': {
        'Parents': [],
        'CPT': {
            (): 1/100000,
            }},
            
    'Test': {
        'Parents': ['Disease'],
        'CPT': {
            (True,): 99/100,
            (False,): 1/100,
            }},
    }


answer = query(network, 'Disease', {'Test': True})
print("The probability of having the disease\n"
      "if the test comes back positive: {:.8f}"
      .format(answer[True]))


answer = query(network, 'Disease', {'Test': False})
print("The probability of having the disease\n"
      "if the test comes back negative: {:.8f}"
      .format(answer[True]))