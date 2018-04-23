# Data science, Deep Learning, & Machine Learning with Python
# Arash Nouri
# Activity 16
# Support vector machine

# "Linear" is one of many kernels scikit-learn supports on SVC. Look up the documentation for scikit-learn online to
#  find out what the other possible kernel options are. Do any of them work well for this data set?

# Import libraries
import numpy as np
from pylab import *
from sklearn import svm
import matplotlib.pylab as plt
from sklearn.preprocessing import StandardScaler
import seaborn as sns

# Create fake income/age clusters for N people in k clusters____________________________________________________________
def createClusteredData(N, k):
    pointsPerCluster = float(N)/k
    X = []
    y = []
    for i in range (k):
        incomeCentroid = np.random.uniform(20000.0, 200000.0)
        ageCentroid = np.random.uniform(20.0, 70.0)
        for j in range(int(pointsPerCluster)):
            X.append([np.random.normal(incomeCentroid, 10000.0), np.random.normal(ageCentroid, 2.0)])
            y.append(i)
    X = np.array(X)
    y = np.array(y)
    return X, y

(X, y) = createClusteredData(100, 5)

plt.figure(figsize=(8, 6))
plt.scatter(X[:,0], X[:,1], c=y.astype(np.float))
plt.xlabel("Income")
plt.ylabel("Age")
plt.show()

# Scaling data__________________________________________________________________________________________________________
sc_X = StandardScaler()
X = sc_X.fit_transform(X)
# Fit SVM_______________________________________________________________________________________________________________
C = [.1, .5, 1]                                 # Penalty parameter
Kernel = ['linear','rbf', 'sigmoid', 'poly']    # Kernels

Scr = []                                        # Score
for i in C:
    for j in Kernel:
        svc = svm.SVC(kernel=str(j), C=i).fit(X, y)
        Scr.append(svc.score(X, y))
Scr = np.array(Scr)
Scr = Scr.reshape(4, 3)
print('')
print('Scores_________________________________________________________________________________________________________')
print(Scr)
print('_______________________________________________________________________________________________________________')

# Results_______________________________________________________________________________________________________________
plt.figure()
sns.heatmap(Scr, xticklabels = ['C = 0.1', 'C = 0.5', 'C = 1'], yticklabels=['linear','rbf', 'sigmoid', 'poly'],
            annot=True, cbar=False)
plt.show()
#=======================================================================================================================
print('')
print('===============================================================================================================')
print('The end')
print('===============================================================================================================')
#=======================================================================================================================