# Metaheuristics

##  F2 Schwefel's Problem 2.21 - Optimisation for dimensions 50 and 500:
<img width="500" alt="schwefelqn" src="https://user-images.githubusercontent.com/35540215/88485079-979c1a00-cf73-11ea-9a43-6f0b381d4fe8.PNG">


* **Data file** :  'schwefel.txt' (data provided)
* **Usage** :  The file 'schwefel.py' which contains the python code along with the data file 'schwefel.txt' may be used in Jupyter notebook/Google Colab
* **Choice of algorithm** : Pygmo package  with Genetic algorithm has been used, since it gives good approximations for this type of problem, in terms of value as well as computation time.
* **Parameters used** : Population size, Generations
* **Stopping criterion** : A good approximation close to the best available solution for the problem
* **Result** : 

<img width="450" alt="schwefeldim50" src="https://user-images.githubusercontent.com/35540215/88485128-01b4bf00-cf74-11ea-8ec0-739a72bf8c7b.PNG"> <img width="450" alt="schwefeldim500" src="https://user-images.githubusercontent.com/35540215/88485129-024d5580-cf74-11ea-8fea-eba23dad73be.PNG">




* **Conclusion** : The Genetic algorithm gives a result almost equal to the stipulated optimum for dimension 50 and the convergence is good. For dimension 500, the convergence is good and the result is close to the stipulated optimum. 
* **References** : 
1. https://www.researchgate.net/publication/228932005_Benchmark_functions_for_the_CEC'2008_special_session_and_competition_on_large_scale_global_optimization
2. https://www.hindawi.com/journals/cin/2017/7430125/             
3. https://esa.github.io/pygmo2/algorithms.html?

