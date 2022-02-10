import lib as m
file = "Task2.csv"

data = m.fr(file)
dataList = data.split(",")
dataList.sort(reverse = True)
print(f"Highest number = {dataList[0]}")
print(f"Lowest number = {dataList[-1]}")
