import matplotlib.pyplot as plt
name = ["Daredevil", "Money Heist", "Narcos", "Stranger Things", "Godless", "Dark", "Our Planet", "The Fall", "After Life", "Ozark"]
num = [2, 3, 4, 5, 7, 8, 9, 10, 11, 12]


plt.pie(num, labels = name)
plt.title("Top 10 show frequency of favourites")
plt.show()



# fig = plt.figure()
# ax = fig.add_axes([0,0,1,1])2]
# ax.bar(name,num)
# plt.title("Heights of students")
# plt.show()