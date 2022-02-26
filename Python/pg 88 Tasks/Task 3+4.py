
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
names = ["Henry", "Robert", "Bob", "Joseph", "Doople", "Sam"]
num = [1.7, 1.5, 1.8, 1.2, 1.9, 1.2]
ax.bar(names,num)
plt.title("Heights of students")
plt.show()