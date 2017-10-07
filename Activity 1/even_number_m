# Write some code that creates a list of integers, loops through each element of the list, and only prints out even
# numbers!

# This code was written for practicing the MATLAB style in Python

# Loading Packages
import numpy as np
from random import randint

# Generating Numbers
# A random generator is used for that
rand_num = []
for i in range(10):
    rand_num.append([randint(1, 100)])
print(rand_num)                                                # Generated random number

res = []                                                       # Residuals
even = []                                                      # Even number
odd = []                                                       # Odd numbers

# Finding residuals
for i in range(len(rand_num)):
    res.append(np.array(rand_num[i]) % 2)

# Classifying the numbers
for i in range(len(res)):
    if res[i] == 1:
        odd.append(rand_num[i])
    else:
        even.append(rand_num[i])
print(["Even number are ", even])                              # Generated random numbe
