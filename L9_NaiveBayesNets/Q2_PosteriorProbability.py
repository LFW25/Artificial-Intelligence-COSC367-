'''
Write a function posterior(prior, likelihood, observation)
that returns the posterior probability of the class variable being true, given the observation; that is, it returns p(Class=true|observation).
The argument observation is a tuple of n Booleans such that observation[i] is the observed value (True or False) for the input feature X[i].
The arguments prior and likelihood are as described above.
''' 

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



prior = 0.05
likelihood = ((0.001, 0.3),(0.05,0.9),(0.7,0.99))

observation = (True, True, True)

class_posterior_true = posterior(prior, likelihood, observation)
print("P(C=False|observation) is approximately {:.5f}"
      .format(1 - class_posterior_true))
print("P(C=True |observation) is approximately {:.5f}"
      .format(class_posterior_true))  



prior = 0.05
likelihood = ((0.001, 0.3),(0.05,0.9),(0.7,0.99))

observation = (True, False, True)

class_posterior_true = posterior(prior, likelihood, observation)
print("P(C=False|observation) is approximately {:.5f}"
      .format(1 - class_posterior_true))
print("P(C=True |observation) is approximately {:.5f}"
      .format(class_posterior_true))  
