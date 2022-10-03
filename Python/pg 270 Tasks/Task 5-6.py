# Imports
import random
import matplotlib.pyplot as plt

# Defs
def dice():
    return random.randint(1, 6)

# This is in chapter 3 im pretty sure idk
def freq(name):
    z = []
    y = []
    for item in name:
        if item not in z:
            z.append(item)
    for x in z:
        total = name.count(x)
        y.append(total)
    return z, y

# Change the "times" to get less or more accurate results
times = 2000
counter = 0
numList = []

# main part of the code
while counter != times:
    numList.append(f"{dice()}")
    counter += 1
x,y = freq(numList)

# Plotting stage
x_pos = [i for i, _ in enumerate(x, 1)]
plt.bar(x_pos, y)
plt.show()