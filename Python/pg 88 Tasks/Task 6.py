import matplotlib.pyplot as plt

names = ["Lionel", "Steph", "Conor", "Serena", "Danica", "Katie"]
ages = [32, 31, 30, 37, 37, 33]
money = [127, 79, 47, 18, 7.5, 1.1]

plt.plot(names, money)
plt.plot(ages, "bs")
plt.xlabel("names")
plt.legend(["money made in millions", "ages"])
plt.show()