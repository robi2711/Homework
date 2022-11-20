import myDef as m
import matplotlib.pyplot as plt
import random as rand

## Basic start up of the code to reset data and split up the data needed
user = input("""----------------------- What would you like to do? --------------------------
> data1 : All the data in the past 18 years of lotto plotted
> data2 : All the data in the past 5 years of lotto plotted
> data3 : All the data in the past year of lotto plotted
> random : Random numbers generated to the users liking plotted
> search: Allows the user to search for a number in the database
---------------------------------------------------------------------------------------
> """)
search = False
if user == "data1":
    data = "data1.csv"
elif user == "data2":
    data = "data2.csv"
elif user == "data3":
    data = "data3.csv"
elif user == "random":
    data = "random.csv"
    lines = int(input("How many lines of numbers would you like (Over 100) > "))
    if lines < 100:
        print("lines are too low... set to 100")
        lines = 100
elif user == "search":
    search = True
    data = "data1.csv"
    usernum = input("  Usage: x;x;x;x;x;y;y \n  Where x is a 'Normal Pick' and y is a 'Lucky Pick' \n > ")
else:
    print("Sorry I dont understand that")


numbers = "numbers.csv"
luckynum = "lucky.csv"

sorted_balls = []
sorted_picks = []

m.fw(luckynum, "")
m.fw(numbers, "")
if user == "random":
    m.fw(data, "")
    for x in range(lines):
        for i in range(0,5):
            n = rand.randint(1,50)
            m.fa(data, f"{n};")
        for i in range(0,2):
            n = rand.randint(1,12)
            m.fa(data, f"{n};")
        m.fa(data, "\n")


## Cleans up the data
dataIn = m.fr(data)
dataIn = dataIn.split("\n")
if user == "random":
    del dataIn[-1]
    for x in dataIn:
        data1 = x.split(";")
        del data1[-1]
        for x in range(5):
            m.fa(numbers, f"{data1[x]},")
    for x in dataIn:
        data1 = x.split(";")
        for x in range(5):
            del data1[0]
        for x in range(2):
            m.fa(luckynum, f"{data1[x]},")
elif search:
    del dataIn[0]
    del dataIn[-1]
    for x in dataIn:
        data1 = x.split(";")
        del data1[-1]
        del data1[-1]
        m.fa(numbers, f"{data1[0]}:")
        for x in range(1,7):
            m.fa(numbers, f"{data1[x]};")
        m.fa(numbers, f"{data1[-1]}")
        m.fa(numbers, "\n")
else:
    del dataIn[0]
    del dataIn[-1]
    for x in dataIn:
        data1 = x.split(";")
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

if search:
    found = False
    f = m.fr(numbers)
    dataList = f.split("\n")
    del dataList[-1]
    #usernum
    for x in dataList:
        y = x.split(":")
        if y[1] == usernum:
            print(f"This number has appeared on the date: {y[0]}")
            found = True
    if found:
        pass
    else:
        print("This number has not appeared before")
else:
    f = m.fr(numbers)
    dataList = f.split(",")
    del dataList[-1]
    x,y = m.freq(dataList)


    ## Normal picks data
    count = 1
    while count != 51:
        n = x.index(f"{count}")
        sorted_balls.append(x[n])
        sorted_picks.append(y[n])
        count += 1
    x_pos = [i for i, _ in enumerate(sorted_balls)]
    plt.bar(x_pos, sorted_picks, color='green')
    plt.xlabel("Ball no.")
    plt.ylabel("No. of picks")
    print(f"highest number won: {sorted_picks.index(max(sorted_picks))+1} at {max(sorted_picks)} wins")
    if data == "data1.csv":
        plt.title("Lottery drawing results over 18 years      NORMAL PICKS")
    elif data == "data2.csv":
        plt.title("Lottery drawing results over 5 years      NORMAL PICKS")
    elif data == "data3.csv":
        plt.title("Lottery drawing results over 1 year      NORMAL PICKS")
    plt.xticks(x_pos, sorted_balls)
    plt.show()
    count = 1


    ## Lucky picks data
    if data == "data1.csv":
        pass #Data 1 does not take into account "Lucky Picks" as they were not incorporated
    else:
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
        print(f"highest number won: {lucky_freq.index(max(lucky_freq))+1} at {max(lucky_freq)} wins")
        if data == "data2.csv":
            plt.title("Lottery drawing results over 5 years      LUCKY PICKS")
        elif data == "data3.csv":
            plt.title("Lottery drawing results over 1 year      LUCKY PICKS")
        plt.xticks(x_pos, lucky_num)
        plt.show()
