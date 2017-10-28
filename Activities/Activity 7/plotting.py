# Arash Nouri
# Data Science, Deep Learning, & Machine Learning with Python
# Activity 7

# Try creating a scatter plot representing random data on age vs. time spent watching TV. Label the axes.

# Loading the toolboxes_________________________________________________________________________________________________
import numpy as np
import matplotlib.pyplot as plt

# Generating random data________________________________________________________________________________________________
age = np.random.randint(0,100,1000)        # Age

# Geberating time spent watching TV per day
tv_time = np.random.rand(1000)             # Generating random numbers

TV_time = []                                # Time spent watching TV per day
for i in range(len(tv_time)):
    TV_time.append(tv_time[i]*24)           # 24 hours in each day

# Plotting______________________________________________________________________________________________________________

# Scatter plot----------------------------------------------------------------------------------------------------------
plt.figure("Scatter plot")

plt.scatter(TV_time,age)

plt.xlabel("Time per day")
plt.ylabel("Age")


axes = plt.axes()
axes.set_xlim([0,24])
axes.set_ylim([0,100])
axes.grid()

plt.show()

#=======================================================================================================================
print(                                                                                                                 )
print("===============================================================================================================")
print("End of the code")
print("===============================================================================================================")
#=======================================================================================================================

print(max(TV_time))