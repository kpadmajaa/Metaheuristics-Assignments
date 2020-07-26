# Metaheuristics

##  F6 Shifted Ackley's Function - Optimisation for dimensions 50 and 500:
<img width="525" alt="ackleysqn" src="https://user-images.githubusercontent.com/35540215/88487468-a2f84100-cf85-11ea-9ca6-fa6ef673383f.PNG">

* **Data file** :  'ackleys.txt' (data provided)
* **Usage** The file 'shifted_ackleys.py' which contains the python code, along with the data file 'ackleys.txt', may be used in Jupyter notebook/Google Colab
* **Choice of algorithm** : Pygmo package  with Genetic algorithm  has been used, since it gives good approximations for this type of problem, in terms of value as well as computation time. 
* **Parameters used** : Population size, Generations
* **Stopping criterion** : A good approximation close to the best available solution for the problem
* **Result** : 

<img width="450" alt="ShiftedAckleydim50" src="https://user-images.githubusercontent.com/35540215/88487474-a986b880-cf85-11ea-820c-61589abfc061.PNG"> <img width="450" alt="ShiftedAckleydim500" src="https://user-images.githubusercontent.com/35540215/88487481-aee40300-cf85-11ea-83d2-b49371a555f2.PNG">







* **Conclusion** : The Genetic algorithm gives a result almost equal to the target optimum for dimension 50 and the convergence is good. For dimension 500, the convergence is good. Though the value may become better with increase in population size and more generations, the computation time may be longer.
* **References** : 
1. https://www.researchgate.net/publication/228932005_Benchmark_functions_for_the_CEC'2008_special_session_and_competition_on_large_scale_global_optimization
2. https://www.hindawi.com/journals/cin/2017/7430125/             
3. https://esa.github.io/pygmo2/algorithms.html?
