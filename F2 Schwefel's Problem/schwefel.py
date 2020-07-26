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
with open('schwefel.txt', "rt") as f:
  for line in f:
    x = line.split(',')
    for v in x:
      if v != '\n':
        data.append(float(v)) 

schwefel_data = np.array(data)
f_bias = np.array([-450.0 , -450.0 , 390.0 , -330.0 , -180.0 , -140.0])

# Definition of objective function to be optimised

class Schwefel:
    
  def fitness(self,x):
    z = np.subtract(x[:dim], schwefel_data[:dim])
    F = np.max(np.abs(x[:dim] - schwefel_data[:dim])) + f_bias[1]
    return [F]
  def get_bounds(self):
    return ([-100]*dim, [100]*dim)

# Defining the optimisation function

def Opt_Gen_Alg(sch_prob= None, pop_size=None, generations=None, exp_opt=None):
          
    time_begin = time.time()
    
    # Algoritm initialisation, settings, problem definition

    simple_GA = sga(gen = generations, cr = 0.90, eta_c = 1.0, m = 0.02,                          param_m = 1.0, param_s = 2, crossover = "exponential",                          mutation = "polynomial", selection = "tournament", seed = 100)
    algo = algorithm(simple_GA)
    algo.set_verbosity(1)
    prob = problem(sch_prob())
    
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
    plt.title("Schwefel Problem - Convergence Curve (dim = "+str(dim)+")")

    plt.plot(Gen, Best_fit, label="Observed Optimum: "+str(pop.champion_f[0]))
    plt.axhline(y=exp_opt, color="green", label="Expected Optimum "+str(exp_opt))
    plt.legend()
    plt.xlabel("Generations")
    plt.ylabel("Best Fitness")
    plt.show()
    print("Computation time : {}".format(time_end-time_begin))
    print("Observed fitness at optimum : {:.4f} ".format(pop.champion_f[0]))
    print("Expected fitness at optimum : {:.4f} ".format(exp_opt))
    print("Function evaluations : {}".format(Eval[-1]))
    print('\n'*2)

dim = 50
Opt_Gen_Alg(sch_prob=Schwefel, pop_size=500, generations=2500, exp_opt=f_bias[1])

dim = 500
Opt_Gen_Alg(sch_prob=Schwefel, pop_size=1000, generations=7000, exp_opt=f_bias[1])

