# Metaheuristics

##  F5 Shifted  Griewank's Function - Optimisation for dimensions 50 and 500:


* **Data file** :  'griewank.txt' (data provided)
* **Usage** The file 'shifted_griewank.py' which contains the python code, along with the data file 'griewank.txt', may be used in Jupyter notebook/Google Colab
* **Choice of algorithm** : Pygmo package  with Particle Swarm Optimisation (PSO) algorithm has been used, since it gives good approximations for this type of problem, in terms of value as well as computation time. PSO makes hardly any assumptions and does not use gradient of the problem and is capable of large searches.
* **Parameters used** : Population size, Generations
* **Stopping criterion** : A good approximation close to the best available solution for the problem
* **Result** : 







* **Conclusion** : The PSO algorithm gives a result almost equal to the target optimum for dimension 50 and the convergence is good. For dimension 500, the convergence is good. and the value is closer to the target optimum, which would improve with higher population size and generations.
* **References** : 
1. https://www.researchgate.net/publication/228932005_Benchmark_functions_for_the_CEC'2008_special_session_and_competition_on_large_scale_global_optimization
2. https://www.hindawi.com/journals/cin/2017/7430125/             
3. https://esa.github.io/pygmo2/algorithms.html?
4. https://en.wikipedia.org/wiki/Particle_swarm_optimization
