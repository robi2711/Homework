import myDef as m
import matplotlib.pyplot as plt


## Basic start up of the code to reset data and split up the data needed
## switch between data 2 and 1 to get dates before and after 12 as a lucky number was implementated
data = "data2.csv"
numbers = "numbers.csv"
dates = "dates.csv"
luckynum = "lucky.csv"
count = 1
sorted_balls = []
sorted_picks = []
won = []
m.fw(numbers, "")
m.fw(dates, "")
m.fw(luckynum, "")
dataIn = m.fr(data)
dataIn = dataIn.split("\n")



## Cleans up the data
del dataIn[0]
del dataIn[-1]
for x in dataIn:
    data1 = x.split(";")
    m.fa(dates, f"{data1[0]},")
    won.append(data1[9])
    del data1[0]
    del data1[-1]
    del data1[-1]
    for x in range(5):
        m.fa(numbers, f"{data1[x]},")
for x in dataIn:
    data1 = x.split(";")
    for x in range(6):
        del data1[0]
    del data1[-1]
    del data1[-1]
    for x in range(2):
        m.fa(luckynum, f"{data1[x]},")
f = m.fr(numbers)
dataList = f.split(",")
del dataList[-1]
x,y = m.freq(dataList)


##Gets mean
total = 0
counter = 0
while counter != len(won):
    total += int(won[counter])
    counter += 1
mean = total/counter
counter = 0


## Normal picks data
while count != 51:
    n = x.index(f"{count}")
    sorted_balls.append(x[n])
    sorted_picks.append(y[n])
    count += 1
date = m.fr(dates)
date2 = date.split(",")
x_pos = [i for i, _ in enumerate(sorted_balls)]
plt.bar(x_pos, sorted_picks, color='green')
plt.xlabel("Ball no.")
plt.ylabel("No. of picks")
print(f"""Average no. of how much money won per game: {round(mean)}
highest number won: {sorted_picks.index(max(sorted_picks))+1} at {max(sorted_picks)} wins
median date: {date2[round(len(date2)/2)]}""")
if data == "data1.csv":
    plt.title("Lottery drawing results over 18 years      NORMAL PICKS")
elif data == "data2.csv":
    plt.title("Lottery drawing results over 5 years      NORMAL PICKS")
else:
    plt.title("Lottery drawing results over 1 year      NORMAL PICKS")
plt.xticks(x_pos, sorted_balls)
plt.show()
count = 1




## Lucky picks data
lucky_freq = []
lucky_num = []
f = m.fr(luckynum)
dataList = f.split(",")
del dataList[-1]
x,y = m.freq(dataList)
while count != 13:
    n = x.index(f"{count}")
    lucky_num.append(x[n])
    lucky_freq.append(y[n])
    count += 1
x_pos = [i for i, _ in enumerate(lucky_num)]
plt.bar(x_pos, lucky_freq, color='green')
plt.xlabel("Ball no.")
plt.ylabel("No. of picks")
print(f"""Average no. of how much money won per game: {round(mean)}
highest number won: {lucky_freq.index(max(lucky_freq))+1} at {max(lucky_freq)} wins
median date: {date2[round(len(date2)/2)]}""")
if data == "data1.csv":
    plt.title("Lottery drawing results over 18 years      LUCKY PICKS")
elif data == "data2.csv":
    plt.title("Lottery drawing results over 5 years      LUCKY PICKS")
else:
    plt.title("Lottery drawing results over 1 year      LUCKY PICKS")
plt.xticks(x_pos, lucky_num)
plt.show()
