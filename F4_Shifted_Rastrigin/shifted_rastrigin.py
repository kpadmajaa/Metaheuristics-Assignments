#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!pip install pygmo
import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time
from pygmo import *

# Import data

get_ipython().system('pip install pygmo')
import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time
from pygmo import *

# Import data

data = []
with open('rastrigin.txt', "rt") as f:
  for line in f:
    x = line.split(',')
    for v in x:
      if v != '\n':
        data.append(float(v)) 

rastrigin_data = np.array(data)
f_bias = np.array([-450.0 , -450.0 , 390.0 , -330.0 , -180.0 , -140.0])

# Definition of objective function to be minimised

class Shifted_Rastrigin:
    
  def fitness(self,x):
    z = np.subtract(x[:dim], rastrigin_data[:dim])
    F = np.sum(np.subtract(np.power(z,2),10*np.cos(2*np.pi*z))+10) + f_bias[3]
    return [F]
  def get_bounds(self):
    return ([-5]*dim, [5]*dim)

# Defining the minimisation function

def Min_Gen_Alg(ras_prob= None, pop_size=None, generations=None, exp_min=None):
          
    time_begin = time.time()
    
    # Algoritm initialisation, settings, problem definition

    simple_GA = sga(gen = generations, cr = 0.90, eta_c = 1.0, m = 0.02,                          param_m = 1.0, param_s = 2, crossover = "exponential",                          mutation = "polynomial", selection = "tournament", seed = 100)
    algo = algorithm(simple_GA)
    algo.set_verbosity(1)
    prob = problem(ras_prob())
    
    # Creating populations, crossover,mutation

    pop = population(prob, size=pop_size, seed=100)
    pop = algo.evolve(pop)
    time_end = time.time()
    
    # Log extraction
    uda = algo.extract(sga)
    log = uda.get_log()
        
    # Creating vectors of Evaluation and Fitness for each gneneration
    Gen = [x[0] for x in log]
    Eval = [x[1] for x in log]
    Best_fit = [x[2] for x in log]
        
    
    # Graphs of computations
    #print("Number of dimensions : {}".format(dim))
    plt.title("Shifted Rastrigin - Convergence Curve (dim = "+str(dim)+")")

    plt.plot(Gen, Best_fit, label="Observed Minimum: "+str(pop.champion_f[0]))
    plt.axhline(y=exp_min, color="r", label="Expected Minimum "+str(exp_min))
    plt.legend()
    plt.xlabel("Generations")
    plt.ylabel("Best Fitness")
    plt.show()
    print("Computation time : {}".format(time_end-time_begin))
    print("Observed fitness at minimum : {:.4f} ".format(pop.champion_f[0]))
    print("Expected fitness at minimum : {:.4f} ".format(exp_min))
    print("Function evaluations : {}".format(Eval[-1]))
    print('\n'*2)

dim = 50
Min_Gen_Alg(ras_prob=Shifted_Rastrigin, pop_size=500, generations=1000, exp_min=f_bias[3])

dim = 500
Min_Gen_Alg(ras_prob=Shifted_Rastrigin, pop_size=1000, generations=2000, exp_min=f_bias[3])

