### Genetic algorithm to fit a regression line of the form y=ax+b to a 2-variable datas et 
import random import numpy as np 
# load the data my_data_file = 'temp_data.npy' data = np.load(my_data_file) 
# parameters initial_pop_size = 100 #creating an initial population size
mutation_rate = 0.05 
num_generations = 10  
chromosome_length = 2 
num_survivors = 50


def A():    
  gene_pool = np.linspace(-1,80,num = 5000)  
  #use linspace to create an array of mating pool with 5000 equally spaced values        
  #starting from -1 and ends with 80    
  dimensions = (initial_pop_size, chromosome_length)        
  #create a tuple with two variables: number of chromosomes        
  #and the length of chromosomes    
  return np.random.choice(gene_pool, size=dimensions, replace=False)         
#From the gene pool, randomly generate an intial population         
#of 100 chromosomes, each chromosome has 2 genes

def B(coefficients):    
  k = len(data) #k is the total number of chromosomes in the training dataset    
  tot = 0 #Set the initial sum of squared errors to 0    
  for j in range(k): #loop through j in the range of k        
    y = coefficients[0] * data[j,0] + coefficients[1]            #y represents the linear regression funtion        
    res = data[j,1] - y            #find residual by calculating the differencebetween observed response in dataset             
                                    #and response predicted by model fit y.        
    tot += res**2            #tot is the sum of squared errors/residuals    
  return tot/k #return mean squared error
  
  
def C():    
  fitlist = [] #create an empty list    
  for x in range(len(current_pop)):         #loop through every item in the current population 
       fitlist.append(np.array([x,B(current_pop[x])])) #calls function B to return value of solution with their fitness value            
  return np.array(fitlist)        
    #return an array to store the information above        
    #fitness value of each solution 

def D():    
  random_selection = np.random.choice(range(len(fitness_vector)), num_survivors//2, r eplace=False)        
    #randomly choose half of the survivors from         
    #the range of fitness_vector without replacement        
    #fitness_vector is assigned as the array in function C    
  best = np.argmin(fitness_vector[random_selection,1])  #find the smallest mean squared error (MSE)    
  best_index = random_selection[best]        #find the index of the smallest MSE in 'best'    
  return current_pop[int(fitness_vector[best_index][0])]   
    #find the index of the chromosome with the smallest MSE        
    #based on the index of the smallest MSE
    

def E(): #crossover function     
  duplicate_size = len(new_population) - len(survivors)     
     #calculate the difference between the number of the new population and the survivor s     
    duplicate_survivors = np.zeros((duplicate_size, chromosome_length))    
      #create an array of chromosomes with the size as above, with all chromosomes as zer os by default    
    for x in range(chromosome_length):         #interate over the length of the chromosome (2 collumns)        
      duplicate_survivors[:, x] = np.repeat(survivors[:, x], 4, axis=0)
        # duplicate the columns 4 times of survivors to generate 200 chromosomes         
      duplicate_survivors[:, x] = np.random.permutation(duplicate_survivors[:, x])         
        #crossover step with permutating the order of the chromosomes     
     return duplicate_survivors
     
import random 
def F(array): # currently does nothing    
  for x in range(len(array)): #loop through every chromosome        
    for a in range(chromosome_length):    
      #mutate both genes in the chromosome due to small probability            
      #that the randomized number would be the same one.            
      #This loop ensures that the mutated coefficient is different.            
      if random.random() < mutation_rate:                
        mutation = array[x,a]             #Let the mutated coefficient equals to array[x,a]:                
        while mutation == array[x,a]:            #while loop through all mutated coefficients                    
          mutation = np.random.choice(np.linspace(-1,80,num = 5000))     
          #Generate a random number in the range [-1,80]            
          #np.random.choice allows array[x,a] to have the chance to mutated randomly                
        array[x,a]=mutation         
    return array #return new population of mutated offspring
   
   
### Start of main program
current_pop = A() #assign current_pop as function A 
new_population = np.zeros((num_survivors * 5, chromosome_length))  
#create an empty array of 200 rows and 2 columes 
# main loop 
for i in range(num_generations):    #interate through all generations because those are    
                                #the number of iterations until termination        
   fitness_vector = C()     #assign function C as fitness_vector that store fitness values     
   survivors = np.zeros((num_survivors, chromosome_length))  #create an empty array of 'survivors' with 50 rows, 2 columes    
   for n in range(len(survivors)): #loop through every chromosome in range 'survivors'        
    survivors[n] = D() #parent selection with chromosomes            
    new_population[:len(survivors)] = survivors     #First 50 values will store the best-fit solutions from the current generation 
    new_population[len(survivors):] = E()    #Other 200 values from empty array are the duplicates     
                                          #created in D() after crossover        
    new_population = F(new_population)        #To new generation - call F() to mutate a portion of the solutions 
    current_pop = new_population        #Redefine current_pop with new values  
    new_population = np.zeros((num_survivors * 5, chromosome_length))    #Create empty array for the new generation with specific dimensions  
fitness_vector = C() #Call C() to obtain fitness values from last generation 
best_solution = current_pop[np.argmin(fitness_vector[:,1])] #Uses method np.argmin to obtain the value  
                                                                  #with the least error sum squared to print it 
print("The best solution is", best_solution) #Print the two genes of the best solution 
print("with error equal to approximately", B(best_solution)) #Call B() to print the sum error squared of this same solution
   
