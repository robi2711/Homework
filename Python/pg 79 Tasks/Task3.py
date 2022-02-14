import lib as m
import random

file = "Task3.csv"
counter = 0
m.fw(file, "")

while counter != 100:
    randint = random.randint(1, 100)
    m.fa(file, f"{randint},")
    counter += 1
file2 = "Task3_Impute.csv"
m.fw(file2, "")
data = m.fr(file)
dataList = data.split(",")
del dataList[-1]
for item in dataList:
    if int(item) > 30:
        m.fa(file2, "30,")
    else:
        m.fa(file2,f"{item},")