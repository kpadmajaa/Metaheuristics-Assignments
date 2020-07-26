#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install pygmo')
import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time
from pygmo import *

# Import data

data = []
with open('rosenbrock.txt', "rt") as f:
  for line in f:
    x = line.split(',')
    for v in x:
      if v != '\n':
        data.append(float(v)) 

rosenbrock_data = np.array(data)
f_bias = np.array([-450.0 , -450.0 , 390.0 , -330.0 , -180.0 , -140.0])

# Definition of objective function to be minimised

class Shifted_Rosenbrock:
    
  def fitness(self,x):
    z = np.subtract(x[:dim], rosenbrock_data[:dim])+1
    F = np.sum(100 * np.power(np.subtract(np.power(z[:dim-1], 2), z[1:dim]), 2)+ np.power((z[:dim-1]-1), 2)) + f_bias[2]
    return [F]
  def get_bounds(self):
    return ([-100]*dim, [100]*dim)

# Defining the minimisation function

def Min_cmaes(ros_prob= None, pop_size=None, generations=None, exp_min=None):
          
    time_begin = time.time()
    
    # Algoritm initialisation, settings, problem definition

    pyg_cmaes = cmaes(gen = generations,  cc=-1, cs=- 1, c1=-1, cmu=-1, sigma0=0.5, ftol=1e-06, xtol=1e-06, memory=False, force_bounds=False, seed=100)
    algo = algorithm(pyg_cmaes)
    algo.set_verbosity(100)
    prob = problem(ros_prob())
    
    # Creating populations, crossover,mutation

    pop = population(prob, size=pop_size, seed=100)
    pop = algo.evolve(pop)
    time_end = time.time()
    
    # Log extraction
    uda = algo.extract(cmaes)
    log = uda.get_log()
        
    # Creating vectors of Evaluation and Fitness for each gneneration
    Gen = [x[0] for x in log]
    Eval = [x[1] for x in log]
    Best_fit = [x[2] for x in log]
        
    
    # Graphs of computations
    #print("Number of dimensions : {}".format(dim))
    plt.title("Shifted Rosenbrock's - Convergence Curve (dim = "+str(dim)+")")

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
Min_cmaes(ros_prob=Shifted_Rosenbrock, pop_size=500, generations=2000, exp_min=f_bias[2])

dim = 500
Min_cmaes(ros_prob=Shifted_Rosenbrock, pop_size=200, generations=500, exp_min=f_bias[2])

