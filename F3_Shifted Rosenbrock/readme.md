# Metaheuristics

##  F3 Sifted Rosenbrock's Function - Optimisation for dimensions 50 and 500:
<img width="525" alt="RosenbrockQn" src="https://user-images.githubusercontent.com/35540215/88486518-8c9ab700-cf7e-11ea-9cec-9c7c118835a4.PNG">

* **Data file** :  'rosenbrock.txt' (data provided)
* **Usage** The file 'shifted_rosenbrock.py' which contains the python code along with the data file 'rosenbrock.txt' may be used in Jupyter notebook/Google Colab
* **Choice of algorithm** : Pygmo package  with Covariance Matrix Adaptation Evolution Strategy (CMA-ES) algorithm has been used, since it gives good approximations for this type of problem, in terms of value as well as computation time. The Genetic algorithm and Particle Swarm Optimisation(PSO) , though converge, the values are way off the target optimum
* **Parameters used** : Population size, Generations
* **Stopping criterion** : A good approximation close to the best available solution for the problem
* **Result** : 

<img width="450" alt="rosenbrock dim 50" src="https://user-images.githubusercontent.com/35540215/88486520-94f2f200-cf7e-11ea-8bf7-9259be56db36.PNG"> <img width="450" alt="rosenbrock dim 500" src="https://user-images.githubusercontent.com/35540215/88486522-9a503c80-cf7e-11ea-860f-afd442e22c40.PNG">




* **Conclusion** : The CMA-ES algorithm gives a result almost equal to the target optimum for dimension 50 and the convergence is good. For dimension 500, the convergence is good. Though the value may become better with increase in population size and more generations, the computation time may be longer.
* **References** : 
1. https://www.researchgate.net/publication/228932005_Benchmark_functions_for_the_CEC'2008_special_session_and_competition_on_large_scale_global_optimization
2. https://www.hindawi.com/journals/cin/2017/7430125/             
3. https://esa.github.io/pygmo2/algorithms.html?

