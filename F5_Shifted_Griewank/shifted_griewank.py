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
with open('griewank.txt', "rt") as f:
  for line in f:
    x = line.split(',')
    for v in x:
      if v != '\n':
        data.append(float(v)) 

griewank_data = np.array(data)
f_bias = np.array([-450.0 , -450.0 , 390.0 , -330.0 , -180.0 , -140.0])

# Definition of objective function to be minimised

class Shifted_Griewank:
    
  def fitness(self,x):
    z = np.subtract(x[:dim], griewank_data[:dim])
    F1 = np.sum(np.divide(np.power(z, 2), 4000))
    F2 = np.prod(np.cos(z/np.sqrt(np.arange(1,dim+1))))
    F = F1 - F2 + 1 + f_bias[4]
    return [F]
  def get_bounds(self):
    return ([-600]*dim, [600]*dim)

# Defining the minimisation function

def Min_pso(grie_prob= None, pop_size=None, generations=None, exp_min=None):
          
    time_begin = time.time()
    
    # Algoritm initialisation, settings, problem definition

    pyg_pso = pso(gen = generations, omega=0.7298, eta1=2.05, eta2=2.05, max_vel=0.5, variant=5, neighb_type=2, neighb_param=4, memory=False, seed = 100)
    algo = algorithm(pyg_pso)
    algo.set_verbosity(50)
    prob = problem(grie_prob())
    
    # Creating populations, crossover,mutation

    pop = population(prob, size=pop_size, seed=100)
    pop = algo.evolve(pop)
    time_end = time.time()
    
    # Log extraction
    uda = algo.extract(pso)
    log = uda.get_log()
        
    # Creating vectors of Evaluation and Fitness for each gneneration
    Gen = [x[0] for x in log]
    Eval = [x[1] for x in log]
    Best_fit = [x[2] for x in log]
    
    # Graphs of computations
    #print("Number of dimensions : {}".format(dim))
    plt.title("Shifted Griewank - Convergence Curve (dim = "+str(dim)+")")

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
Min_pso(grie_prob=Shifted_Griewank, pop_size=200, generations=1000, exp_min=f_bias[4])

dim = 500
Min_pso(grie_prob=Shifted_Griewank, pop_size=1000, generations=3000, exp_min=f_bias[4])

