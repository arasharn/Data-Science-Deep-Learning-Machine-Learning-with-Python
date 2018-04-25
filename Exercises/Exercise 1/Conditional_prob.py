# Arash Nouri
# Data Science, Deep Learning, & Machine learning with Python
# Exercise 2

# Modify the code above such that the purchase probability does NOT vary with age, making E and F actually independent.
# Then, confirm that P(E|F) is about the same as P(E), showing that the conditional probability of purchase for a given
# age is not any different than the a-priori probability of purchase regardless of age.

# Importing toolboxes___________________________________________________________________________________________________
import matplotlib.pylab as plt

# Generating data_______________________________________________________________________________________________________
from numpy import random
random.seed(0)

totals = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}
purchases = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}
totalPurchases = 0
for _ in range(100000):
    ageDecade = random.choice([20, 30, 40, 50, 60, 70])
    purchaseProbability = .4
    totals[ageDecade] += 1
    if (random.random() < purchaseProbability):
        totalPurchases += 1
        purchases[ageDecade] += 1

plt.figure(1)
x1, y1 = zip(*purchases.items())
plt.scatter(x1,y1)

plt.figure(2)
x2, y2 = zip(*totals.items())
plt.scatter(x2,y2)

# Calculating P(E|F)____________________________________________________________________________________________________
pef = float(purchases[30]) / float(totals[30])
print('P(purchase | 30s): ' + str(pef))

# Calculating P(F)______________________________________________________________________________________________________
pf = float(totals[30]) / 100000.0
print("P(30's): " +  str(pf))


