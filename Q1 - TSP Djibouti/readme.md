# Metaheuristics

## Question 1 : Solve the travelling salesman problem with 38 cities (Djibouti)

* **Data file** : 'djibouti.csv' (extracted from http://www.math.uwaterloo.ca/tsp/world/dj38.tsp)
* **Usage** : The file 'tsp djibouti.py' containing the python code, can be executed using jupyternotebook/ GoogleColab along with the data file 'djibouti.csv'
* **Choice of algorithm** : Genetic algorithm based on selection criteria, crossover and mutation operators has been used, since it gives good approximations for NP-hard problems like travelling salesman problem.
* **Parameters used** : Population size, Elite Size, Mutation rate, Generations
* **Stopping criterion** : A good approximation close to the best solution available for this problem
* **Result** :
<img width="393" alt="dj 7636 100 1100" src="https://user-images.githubusercontent.com/35540215/88482224-36b71680-cf60-11ea-8062-f999e950e7ae.PNG">

* **References** : 
1. https://towardsdatascience.com/evolution-of-a-salesman-a-complete-genetic-algorithm-tutorial-for-python-6fe5d2b3ca35
2. https://www.hindawi.com/journals/cin/2017/7430125/

