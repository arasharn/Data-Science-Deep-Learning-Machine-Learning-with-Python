# Arash Nouri
# Activity 11
# Data Science, Deep Learning, & Machine Learning with Python

# Mess around with the fake input data, and see if you can create a measurable influence of number of doors on price.
# Have some fun with it - why stop at 4 doors?

# Importing libraries___________________________________________________________________________________________________
import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder

# Loading data__________________________________________________________________________________________________________
df = pd.read_excel('http://cdn.sundog-soft.com/Udemy/DataScience/cars.xls')

print('                                                                                                               ')
print("Data-----------------------------------------------------------------------------------------------------------")
print(df.head())
print("---------------------------------------------------------------------------------------------------------------")

# Changing the doors number---------------------------------------------------------------------------------------------
door_num = np.random.randint(1,10,len(df["Doors"]))
df["Doors"] = door_num
# Defining outputs and inputs___________________________________________________________________________________________
X = df.iloc[:,1:]
y = df.iloc[:,0]

print('                                                                                                               ')
print("X--------------------------------------------------------------------------------------------------------------")
print(X.head())
print("---------------------------------------------------------------------------------------------------------------")
print("y--------------------------------------------------------------------------------------------------------------")
print(y.head())
print("---------------------------------------------------------------------------------------------------------------")

# Categorical data______________________________________________________________________________________________________
labelencoder = LabelEncoder()
X.iloc[:,1] = labelencoder.fit_transform(X.iloc[:,1])
X.iloc[:,2] = labelencoder.fit_transform(X.iloc[:,2])
X.iloc[:,3] = labelencoder.fit_transform(X.iloc[:,3])
X.iloc[:,4] = labelencoder.fit_transform(X.iloc[:,4])

# One hot encoding------------------------------------------------------------------------------------------------------
onehotencode = OneHotEncoder()
onehotencode.fit_transform(X.iloc[:,1:4])

X = X.astype(float)
print('                                                                                                               ')
print("New X----------------------------------------------------------------------------------------------------------")
print(X.head())
print("---------------------------------------------------------------------------------------------------------------")

# Scaling the inputs____________________________________________________________________________________________________
scale = StandardScaler()
X[['Mileage', 'Cylinder', 'Doors']] = scale.fit_transform(X[['Mileage', 'Cylinder', 'Doors']].as_matrix())

# Fitting a MLR model___________________________________________________________________________________________________
est = sm.OLS(y,X).fit()
print(est.summary())


