# Metaheuristics

##  F1 Shifted Sphere Function - Optimisation for dimensions 50 and 500:
<img width="500" alt="ss" src="https://user-images.githubusercontent.com/35540215/88484435-b946d280-cf6e-11ea-9d6f-22861965cddc.PNG">

* **Data file** :  'sphere.txt' (data provided)
* **Usage** : The file 'shifted_sphere.py' which contains the python code, along with the data file 'sphere.txt', may be used in Jupyter notebook/Google Colab
* **Choice of algorithm** : Pygmo package  with Genetic algorithm has been used, since it gives good approximations for this type of problem, in terms of value as well as computation time.
* **Parameters used** : Population size, Generations
* **Stopping criterion** : A good approximation close to the best available solution for the problem
* **Result** : 

<img width="450" alt="spheredim50" src="https://user-images.githubusercontent.com/35540215/88484587-f790c180-cf6f-11ea-80ee-838fabf48286.PNG"> <img width="450" alt="spheredim500" src="https://user-images.githubusercontent.com/35540215/88484599-011a2980-cf70-11ea-9eac-a32a241fd6e9.PNG">


* **Conclusion** : The Genetic algorithm gives a result almost equal to the stipulated optimum for dimension 50 and the convergence is good. For dimension 500, the convergence is good. Though the value may become better with increase in population size and more generations, the computation time may be longer.
* **References** : 
1. https://www.researchgate.net/publication/228932005_Benchmark_functions_for_the_CEC'2008_special_session_and_competition_on_large_scale_global_optimization
2. https://www.hindawi.com/journals/cin/2017/7430125/             
3. https://esa.github.io/pygmo2/algorithms.html?


