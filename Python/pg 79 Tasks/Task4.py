import lib as m
file = "Task4.csv"
file1 = "Task3.csv"
data = m.fr(file1)
m.fw(file, "")
dataList = data.split(",")
unsortedList = []
del dataList[-1]
counter = 0
while counter != len(dataList):
    num = int(dataList[counter])
    if num >= 50:
        unsortedList.append(num)
    counter += 1
unsortedList.sort()
counter = 0
while counter != len(unsortedList):
    m.fa(file ,f"{unsortedList[counter]}, ")
    counter += 1