# Metaheuristics

## Question 2 : Solve the travelling salesman problem with 194 cities (Qatar)

* **Data file** : qatar.csv (extracted from http://www.math.uwaterloo.ca/tsp/world/qa194.tsp)
* **Choice of algorithm** : Genetic algorithm based on selection criteria, crossover and mutation operators has been used, since it gives good approximations for NP-hard problems like travelling salesman problem.
* **Parameters used** : Population size, Elite Size, Mutation rate, Generations
* **Stopping criterion** : A good approximation close to the best available solution for the problem. In this case the number of cities have been scaled down to 50 due to system constraints.
* **Result** : 
<img width="362" alt="tsp Qatar" src="https://user-images.githubusercontent.com/35540215/88482567-5ea77980-cf62-11ea-8ac4-cc3ab78301d0.PNG">


* **References** : 

1. https://towardsdatascience.com/evolution-of-a-salesman-a-complete-genetic-algorithm-tutorial-for-python-6fe5d2b3ca35
                   
2. https://www.hindawi.com/journals/cin/2017/7430125/
