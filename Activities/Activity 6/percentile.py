# Arash Nouri
# Data Science, Deep Learning, & Machine learning with Python
# Activity 6

# Experiment with different parameters when creating the test data. What effect does it have on the percentiles?

# Importing toolboxes___________________________________________________________________________________________________
import numpy as np
import matplotlib.pyplot as plt

# Effect of changing the mean___________________________________________________________________________________________
prc_20 = []                                 # 20% percentiles for constant variance
prc_50 = []                                 # 50% percentiles for constant variance
prc_90 = []                                 # 90% percentiles for constant variance
for m in range(9):
    vals = np.random.normal(m, .5, 10000)
    prc_20.append(np.percentile(vals,20))
    prc_50.append(np.percentile(vals, 50))
    prc_90.append(np.percentile(vals, 90))

# Plotting the results--------------------------------------------------------------------------------------------------
plt.figure("mean")
plt.scatter(np.arange(1,10), prc_20)
plt.scatter(np.arange(1,10), prc_50)
plt.scatter(np.arange(1,10), prc_90)

plt.xlabel("Mean value")
plt.ylabel("Percentiles values")
plt.legend(["20% percentiles", "50% percentiles", "90% percentiles"], loc = 2)
plt.show()

# Effect of changing the variance_______________________________________________________________________________________
v_range = np.arange(0,4.5,.5)     # Range of the variance changes

prc_20v = []                      # 20% percentiles for constant mean
prc_50v = []                      # 50% percentiles for constant mean
prc_90v = []                      # 90% percentiles for constant mean
for i in v_range:
    vals = np.random.normal(0, i, 10000)
    prc_20v.append(np.percentile(vals, 20))
    prc_50v.append(np.percentile(vals, 50))
    prc_90v.append(np.percentile(vals, 90))



# Plotting the results--------------------------------------------------------------------------------------------------
plt.figure("var")
plt.scatter(v_range, prc_20v)
plt.scatter(v_range, prc_50v)
plt.scatter(v_range, prc_90v)

plt.xlabel("Variance value")
plt.ylabel("Percentiles values")
plt.legend(["20% percentiles", "50% percentiles", "90% percentiles"], loc = 2)
plt.show()

#=======================================================================================================================
print("End of the code")
#=======================================================================================================================