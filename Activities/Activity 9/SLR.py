# Arash Nouri
# Activity 9
# Data Science, Deep Learning, & Machine learning with Python

# Try increasing the random variation in the test data, and see what effect it has on the r-squared error value.

# Importing libraries
import numpy as np
import matplotlib.pylab as plt
from scipy import stats

# Generating the data___________________________________________________________________________________________________
pageSpeeds = np.random.normal(3.0, 1.0, 1000)
purchaseAmount = 100 - (pageSpeeds + np.random.normal(0, 0.1, 1000)) * 3

plt.figure(1)
plt.scatter(pageSpeeds, purchaseAmount)
plt.xlabel("Page speed")
plt.ylabel("Purchase amount")
plt.show()

# Adding variation
purchamnt = np.zeros((3, 1000))
n = 0
for j in range(1,4):
    k = 0
    for i in purchaseAmount:
        pa = i + (j*np.random.normal(0, 1, 1))
        purchamnt[n,k] = pa
        k = k+1
    n = n+1

plt.figure(2)
plt.subplot(1,3,1)
plt.scatter(pageSpeeds, purchamnt[0,:])
plt.xlabel("Page speed")
plt.ylabel("Purchase amount")

plt.subplot(1,3,2)
plt.scatter(pageSpeeds, purchamnt[1,:])
plt.xlabel("Page speed")
plt.ylabel("Purchase amount")

plt.subplot(1,3,3)
plt.scatter(pageSpeeds, purchamnt[2,:])
plt.xlabel("Page speed")
plt.ylabel("Purchase amount")
plt.show()

# Fitting SLR model_____________________________________________________________________________________________________
slope1, intercept1, r_value1, p_value1, std_err1 = stats.linregress(pageSpeeds, purchamnt[0,:])
slope2, intercept2, r_value2, p_value2, std_err2 = stats.linregress(pageSpeeds, purchamnt[1,:])
slope3, intercept3, r_value3, p_value3, std_err3 = stats.linregress(pageSpeeds, purchamnt[2,:])

plt.figure(3)
plt.scatter([1], r_value1**2)
plt.scatter([2], r_value2**2)
plt.scatter([3], r_value3**2)
plt.legend(['Low variance', 'Medium variance', 'High variance'])
plt.show()
