# Arash Nouri
# Data Science, Deep Learning, & Machine Learning with Python
# Activity 6

# Understanding skew: change the normal distribution to be centered around 10 instead of 0, and see what effect that has
#  on the moments.

# Loading the toolboxes_________________________________________________________________________________________________
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp

# The effect of the data center on the skewness_________________________________________________________________________
skew = []                               # Skewness value
for i in range(9):
    np.random.seed(12)
    vals = np.random.normal(i, 0.5, 10000)
    sk = sp.skew(vals)
    skew.append(np.array(sk))

print("                                                                                                               ")
print("---------------------------------------------------------------------------------------------------------------")
print("Skewness values are:-------------------------------------------------------------------------------------------")
print(skew)
print("---------------------------------------------------------------------------------------------------------------")

# Plotting______________________________________________________________________________________________________________
plt.scatter(range(9),skew)

plt.xlabel("Center of the distrinbution")
plt.ylabel("Skewness value")
plt.show()

#=======================================================================================================================
print("End of the code")
#=======================================================================================================================