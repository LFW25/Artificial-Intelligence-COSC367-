'''
Write a function joint_prob(network, assignment) that takes a belief network and a complete assignment of all the variables in the network,
and returns the probability of the assignment.
The data structure of the network is as described above.
The assignment is a dictionary where keys are the variable names and the values are either True or False.
'''

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

network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.2
            }},
}

p = joint_prob(network, {'A': True})
print("{:.5f}".format(p))

network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.2
            }},
}

p = joint_prob(network, {'A': False})
print("{:.5f}".format(p))

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
 
p = joint_prob(network, {'A': False, 'B':True})
print("{:.5f}".format(p)) 

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
 
p = joint_prob(network, {'A': False, 'B':False})
print("{:.5f}".format(p))
p = joint_prob(network, {'A': False, 'B':True})
print("{:.5f}".format(p))
p = joint_prob(network, {'A': True, 'B':False})
print("{:.5f}".format(p))
p = joint_prob(network, {'A': True, 'B':True})
print("{:.5f}".format(p)) 


network = {
    'Burglary': {
        'Parents': [],
        'CPT': {
            (): 0.001
            }},
            
    'Earthquake': {
        'Parents': [],
        'CPT': {
            (): 0.002,
            }},
    'Alarm': {
        'Parents': ['Burglary','Earthquake'],
        'CPT': {
            (True,True): 0.95,
            (True,False): 0.94,
            (False,True): 0.29,
            (False,False): 0.001,
            }},

    'John': {
        'Parents': ['Alarm'],
        'CPT': {
            (True,): 0.9,
            (False,): 0.05,
            }},

    'Mary': {
        'Parents': ['Alarm'],
        'CPT': {
            (True,): 0.7,
            (False,): 0.01,
            }},
    }

p = joint_prob(network, {'John': True, 'Mary': True,
                         'Alarm': True, 'Burglary': False,
                         'Earthquake': False})
print("{:.8f}".format(p))