# Arash Nouri
## Activity 5: Experiment with different parameters on the normal function, and see what effect it has on the shape of
# the distribution. How does that new shape relate to the standard deviation and variance?


# Loading libraries_____________________________________________________________________________________________________
import numpy as np
import matplotlib.pyplot as plt

# Effetc of moving the mean_____________________________________________________________________________________________
np.random.seed(1)                               # Defining a random seed
incomes = []                                    # output
j = 1                                           # Subpot counter
m = [50,100,200]                                # Different values of mean
for i in m:
    incomes = np.random.normal(i, 50.0, 10000)  # Generating the normal random numbers
    plt.subplot(1,3,j)                          # Creating subplots
    plt.hist(incomes, 50)                       # Creating the plot
    j = j+1                     

# Plotting the results
plt.show()

# Effect of changing the standard deviation_____________________________________________________________________________
incomes = []                                    # output
j = 1                                           # Subpot counter
STD = [25, 50, 75]                              # Standard deviations
for i in STD:
    incomes = np.random.normal(100,i,10000)
    plt.subplot(1,3,j)
    plt.hist(incomes, 50)
    j += 1
    
# Plotting the results
plt.show()



#=======================================================================================================================
print('                                                                                                               ')
print("===============================================================================================================")
print("End of the code")
print("===============================================================================================================")