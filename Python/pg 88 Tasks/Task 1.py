import random
import lib as m
import matplotlib.pyplot as plt
num = []
for i in range(20):
    num.append(random.randint(1, 20))
plt.plot(num)
plt.title("Random Numbers")
plt.ylabel("Numbers")
plt.xlabel("idk")
plt.show()
#plt.savefig() #if you want to save the image