# Write some code that creates a list of integers, loops through each element of the list, and only prints out even
# numbers!

# Loading Packages
import numpy as np

# Generating Numbers
# A random generator is used for that
rand_num = np.random.randint(1, 100, size = 10)
print('Our numbers are:', rand_num)

# Classifying the numbers
for i in rand_num:
    if (i % 2 == 0):
        print(i," is even")
    else:
        print(i, " is odd")
