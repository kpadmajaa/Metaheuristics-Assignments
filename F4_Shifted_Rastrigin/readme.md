# Metaheuristics

##  F3 Shifted Rastrigin's Function - Optimisation for dimensions 50 and 500:
<img width="525" alt="rastriginqn" src="https://user-images.githubusercontent.com/35540215/88486843-e8663f80-cf80-11ea-83f8-8f25415edc9b.PNG">

* **Data file** :  'rastrigin.txt' (data provided)
* **Usage** The file 'shifted_rastrigin.py' which contains the python code, along with the data file 'rastrigin.txt', may be used in Jupyter notebook/Google Colab
* **Choice of algorithm** : Pygmo package  with Genetic algorithm has been used, since it gives good approximations for this type of problem, in terms of value as well as computation time. 
* **Parameters used** : Population size, Generations
* **Stopping criterion** : A good approximation close to the best available solution for the problem
* **Result** : 

<img width="450" alt="rastrigindim50" src="https://user-images.githubusercontent.com/35540215/88486847-eef4b700-cf80-11ea-96df-9fdb7bdb9a0d.PNG"> <img width="450" alt="rastrigindim500" src="https://user-images.githubusercontent.com/35540215/88486850-f320d480-cf80-11ea-868f-893a488b3062.PNG">





* **Conclusion** : The Genetic algorithm gives a result almost equal to the target optimum for dimension 50 and the convergence is good. For dimension 500, the convergence is good. Though the value may become better with increase in population size and more generations, the computation time may be longer.
* **References** : 
1. https://www.researchgate.net/publication/228932005_Benchmark_functions_for_the_CEC'2008_special_session_and_competition_on_large_scale_global_optimization
2. https://www.hindawi.com/journals/cin/2017/7430125/             
3. https://esa.github.io/pygmo2/algorithms.html?
