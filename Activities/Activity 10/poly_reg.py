# Arash Nouri
# Activity 10
# Data Science, Deep Learning, & Machine learning with Python

# Try different polynomial orders. Can you get a better fit with higher orders? Do you start to see overfitting, even
# though the r-squared score looks good for this particular data set?

# Importing libraries___________________________________________________________________________________________________
import numpy as np
import matplotlib.pylab as plt
from sklearn.metrics import r2_score

# Generating the data___________________________________________________________________________________________________
np.random.seed(2)
pageSpeeds = np.random.normal(3.0, 1.0, 1000)
purchaseAmount = np.random.normal(50.0, 10.0, 1000) / pageSpeeds

plt.figure (1)
plt.scatter(pageSpeeds, purchaseAmount)
plt.xlabel("Page speed")
plt.ylabel("Purchase amount")
plt.show()

# Fitting the polynomial model__________________________________________________________________________________________
xp = np.linspace(0, 7, 100)

r2 = []
for i in range(1,11):
    p = np.poly1d(np.polyfit(pageSpeeds, purchaseAmount, i))
    plt.figure(2)
    plt.subplot(2,5,i)
    plt.scatter(pageSpeeds, purchaseAmount)
    plt.plot(xp, p(xp), c='r')
    r2.append(r2_score(purchaseAmount, p(pageSpeeds)))
plt.show()

print('                                                                                                                  ')
print("r2 scores are ----------------------------------------------------------------------------------------------------")
print(r2)
print("------------------------------------------------------------------------------------------------------------------")

