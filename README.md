# GeneticAlgorithm101
Step by Step tutorial into Genetic algorithm (Follow through with function codes)

## Function A
Function A generates a gene pool consisting of 5000 equally spaced items from -1 to 80 inclusively. Each chromosome is the solution to the regression line to a dataset by looking for the two coefficients of the line. The tuple 'dimensions' indicates two parameters: the initial population size which is the initial number of chromosomes, and the length of chromosomes. Next, we randomly generate an initial population of 100 chromosomes from 5000 items in the original gene pool; each chromosome has the length of 2 or each chromosome consists of 2 genes. Sampling is without replacement.
Creating an initial population is the first step in conducting a genetic algorithm.


## Function B
Function B aims at returning the mean squared error (MSE) of the regression line, which is the objective function for optimization in our genetic algorithm. In this case, the goal is to find the minimum mean squared error of the regression model.
We start assigning k as the total number of items in the training dataset and set the total squared errors equal to 0. Next, we loop through all items in the dataset range to build an equation representing observations predicted by the regression model y. The difference between this predicted response y and the observed response in the training dataset is the residual. Returned MSE equation established through dividing the sum of squared errors over the number of chromosomes in the dataset.


## Function C

Function C initially creates an empty list called 'fitlist' to store information. For each chromosome from the gene pool, which is now assigned as current population, we will calculate its corresponding mean squared error. This information will be saved to the list afterward. In general, the inputs are chromosomes from the gene pool and their MSE, and the output is an array with that information.
This step is to generate an array consisting of fitness scores of each chromosome to determine how fit the chromosome is for the regression model. The probability that an individual will be selected for reproduction in genetic algorithm is determined by its fitness score.

## Function D
Function D essentially aims at finding the local minimum of MSE by returning the index of the chromosome with the smallest MSE. It does that by considering 25 survivors at a time from the range of 100 chromosomes in the 'fitness_vector' to return the index of the chromosome with the smallest MSE. In order to find that chromosome index, the locally smallest MSE and its index are found in advance.
This is one detail that shows the efficiency of genetic algorithm compared to traditional methods such as hill climbing because finding different local optima and then making a comparison between them is faster than going through all iterations to find a global optimum in the end.


## Function E

Function E carries out the cross-over step in the genetic algorithm. First, we calculate how many chromosomes we need to add after having survivors. As the new population is 5 times the number of survivors (observed in the main loop), we will duplicate the columns 4 times to generate 200 chromosomes left. The np.random.permutation represents cross-over by shuffling copy the array of duplicates and return duplicate_survivors. np.random.permutation is different from random shuffling because this method ensures that there are no two chromosomes that share the same gene pattern, which explains why cross-over is the most important step in the genetic algorithm. After this step, new offsprings are stored in a list.
Cross-over is very important because chromosomes with the highest fitness scores will exchange genes to produce the next generation of offspring.


## Function F
Function F operates the last step in the genetic algorithm which is a mutation. Without mutation, our algorithm can be stuck in local optima without finding a global optimum.
This is why mutation works in a random manner using random.random() to explore the untouched areas of the search space, or in another term, to main diversity in the next generations. We loop through every chromosome in the new population after cross-over and loop through every gene in each chromosome as the small mutation rate of 0.05 can create a small probability that the randomized number would be the same one. One scenario in this process would be one of the optimal coefficients is paired up with another nonoptimal coefficient, therefore does not survive. We can ultimately find the coefficients mutating through enough number of generations or iterations. It is also possible that our iteration ends before we can find a globally optimum solution for the 2 coefficients.

## Main program
This main program depicts main steps in the genetic algorithm. Step 1 - Initial population: We start with creating an initial population of chromosomes as current population, and our goal is to create a tuple of new population with 250 chromosomes, each chromosome with 2 genes.
Step 2 - Fitness function: Fitness function in function C() gives each chromosome a fitness score, which is later saved in fitness_vector(). Each chromosome will be selected for reproduction based on their fitness score.
Step 3 - Selection: We create a tuple called "survivors" that has 50 rows (number of survivors) and 2 columns (number of genes in each chromosome). The goal is to select the fittest individuals and let them pass to the next generation through finding local optima in function D().
Step 4 - Cross-over: The array of chromosomes in the tuple "survivors" is shuffled in order to carry out crossover though function E().
Step 5 - Muation: The new population achived after cross-over goes through mutation to ensure diversity in the later generations through function F. As the new population is 5 times larger than the number of survivors, we multiplies number of survivors by 5.
The algorithm terminates when the population has converged to the best solution through the use of np.argmin to find the least mean squared errors among all the local optima. Then it is said that the genetic algorithm has provided a set of solutions to our problem.



