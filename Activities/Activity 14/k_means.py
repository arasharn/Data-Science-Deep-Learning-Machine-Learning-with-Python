# Arash Nouri
# Activity 14
# Data Science, Deep Learning, & Machine Learning with Python

# Things to play with: what happens if you don't scale the data? What happens if you choose different values of K? In
# the real world, you won't know the "right" value of K to start with - you'll need to converge on it yourself.

# Loading the libraries_________________________________________________________________________________________________
from numpy import random, array, arange
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
from numpy import random, float
# Generating data_______________________________________________________________________________________________________

#Defining a fuction for creating fake income/age clusters for N people in k clusters------------------------------------
def createClusteredData(N, k):
    random.seed(10)
    pointsPerCluster = float((N)/k)
    X = []
    for i in range (k):
        incomeCentroid = random.uniform(20000.0, 200000.0)
        ageCentroid = random.uniform(20.0, 70.0)
        for j in range(int(pointsPerCluster)):
            X.append([random.normal(incomeCentroid, 10000.0), random.normal(ageCentroid, 2.0)])
    X = array(X)
    return X

# generating the data---------------------------------------------------------------------------------------------------
data = createClusteredData(100, 5)

# Fitting the model_____________________________________________________________________________________________________

# Scale data vs unscaled data-------------------------------------------------------------------------------------------
model = KMeans(n_clusters=5)
model1 = model.fit(scale(data))
model2 = model.fit(data)

plt.figure(1,figsize=(8, 6))
plt.subplot(2,1,1)
plt.scatter(data[:,0], data[:,1], c=model1.labels_.astype(float))
plt.title("Scaled data")

plt.subplot(2,1,2)
plt.scatter(data[:,0], data[:,1], c=model2.labels_.astype(float))
plt.title("Unscaled data")

# Choosing the number of clusters---------------------------------------------------------------------------------------
scores = []
for i in range(1,11):
    model = KMeans(n_clusters=i)
    model = model.fit(scale(data))
    plt.figure(2)
    plt.subplot(2,5,i)
    plt.title(["k = ", i])
    plt.scatter(data[:,0], data[:,1], c=model.labels_.astype(float))
    scores.append(model.score(data))

plt.figure(3)
plt.title("Elbow plot of K-means by using different number of clusters")
plt.plot(scores)
plt.xlabel("Number of clusters")
plt.ylabel("score")
plt.show()
# ======================================================================================================================
print('===============================================================================================================')
print('End of the code')
print('===============================================================================================================')
# ======================================================================================================================
