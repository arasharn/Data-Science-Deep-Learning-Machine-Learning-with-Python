# Arash Nouri
# Data Science, Deep Learning, & Machine Learning with Python
# Activity 8

# numpy also has a numpy.cov function that can compute Covariance for you. Try using it for the pageSpeeds and
# purchaseAmounts data above. Interpret its results, and compare it to the results from our own covariance function
# above.

# Importing toolboxes___________________________________________________________________________________________________
import numpy as np

# Generating the data___________________________________________________________________________________________________
pageSpeeds = np.random.normal(3.0, 1.0, 1000)
purchaseAmount = np.random.normal(50.0, 10.0, 1000)

# Writing our own covariance function___________________________________________________________________________________
def de_mean(x):
    xmean = np.mean(x)
    return [xi - xmean for xi in x]

def covariance(x, y):
    n = len(x)
    return np.dot(de_mean(x), de_mean(y)) / (n-1)

# Calculating the covariance of the data by using the numpy and our own code____________________________________________
cov_np = np.cov(pageSpeeds, purchaseAmount)
print("                                                                                                               ")
print('numpy result---------------------------------------------------------------------------------------------------')
print(cov_np)
print("---------------------------------------------------------------------------------------------------------------")
cov = covariance(pageSpeeds, purchaseAmount)
print('our code result------------------------------------------------------------------------------------------------')
print(cov_np)
print("---------------------------------------------------------------------------------------------------------------")