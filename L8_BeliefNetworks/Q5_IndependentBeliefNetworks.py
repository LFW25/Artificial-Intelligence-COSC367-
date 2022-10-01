'''
Create a belief network with five random variables A, B, C, D, and E with the following properties:

- A and C are independent of any other variable (and each other).
- D and E depend on each other unless B is given (observed).
'''

network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 2/100,
            }},
            
    'B': {
        'Parents': [],
        'CPT': {
            (True,): 0.2,
            (False,): 0.8
            }},

    'C': {
        'Parents': [],
        'CPT': {
            (): 2/100
            }},
            
    'D': {
        'Parents': ['B'],
        'CPT': {
            (True,): 70/100,
            (False,): 9/100,
            }},

            
    'E': {
        'Parents': ['B'],
        'CPT': {
            (True,): 80/100,
            (False,): 8/100,
            }},

    }

print(sorted(network.keys()))
# [A, B, C, D, E]

print(network['E']['Parents'])
#['B']

bd_dependence = network['D']['CPT'][(False,)] != network['D']['CPT'][(True,)]
be_dependence = network['E']['CPT'][(False,)] != network['E']['CPT'][(True,)]
print(bd_dependence and be_dependence)
# True