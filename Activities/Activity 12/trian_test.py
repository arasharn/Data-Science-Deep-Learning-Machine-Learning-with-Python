# Arash Nouri
# Data Science, Deep Learning, & Machine Learning with Python
# Activity 12

# Try measuring the error on the test data using different degree polynomial fits. What degree works best?

# Importing the libraries_______________________________________________________________________________________________
import numpy as np
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split
import matplotlib.pylab as plt

# Generating data_______________________________________________________________________________________________________
np.random.seed(2)

pageSpeeds = np.random.normal(3.0, 1.0, 100)
purchaseAmount = np.random.normal(50.0, 30.0, 100) / pageSpeeds

plt.figure(1)
plt.scatter(pageSpeeds, purchaseAmount)
plt.ylabel("Purchase amount")
plt.xlabel("Page speeds")
plt.show()

# Splitting train and test sets_________________________________________________________________________________________
X = pageSpeeds
y = purchaseAmount

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

plt.figure(2)
plt.subplot(2,1,1)
plt.scatter(X_train,y_train)
plt.title("Training data")
plt.ylabel("Purchase amount")
plt.xlabel("Page speeds")
plt.subplot(2,1,2)
plt.scatter(X_test, y_test)
plt.ylabel("Purchase amount")
plt.xlabel("Page speeds")
plt.title("Test data")

# Making the model______________________________________________________________________________________________________
for i in range(1,11):
    mdl = np.poly1d(np.polyfit(X_train, y_train, i))
    plt.figure(3)
    plt.subplot(2,5,i)
    plt.scatter(X_train,y_train)
    plt.plot(np.sort(X_train), mdl(np.sort(X_train)), c = 'r')
plt.show()
#=======================================================================================================================
print('                                                                                                               ')
print('===============================================================================================================')
print("End of the code")
print('===============================================================================================================')

