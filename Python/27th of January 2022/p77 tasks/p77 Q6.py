import lib as m

names = "Q6 names.csv"
sales = "Q6 sales.csv"

m.fw(names, "")
m.fw(sales, "")
salespeopleNum =  input("How many salespeople are there? ")
counter = 0
counter2 = 0
total = 0


while counter != int(salespeopleNum):
    salespeopleName = input("What is the name of the salesperson? ")
    m.fa(names, f"{salespeopleName},\n")
    counter += 1
counter = 0
data = m.fr(names)
dataList = data.split("\n")
del dataList[-1]
while counter != int(salespeopleNum):
    salesNum = input(f"How many sales did {dataList[counter]} make? ")
    while counter2 != int(salesNum):
        saleAmount = input("How much money did they make? ")
        m.fa(sales, saleAmount + ",")
        counter2 += 1
    m.fa(sales, "\n")
    counter2 = 0
    counter += 1
data2 = m.fr(sales)
dataList2 = data2.split("\n")
del dataList2[-1]
counter = 0
counter2 = 0
while counter != int(salespeopleNum):
    totalList = dataList2[counter].split(",")
    del totalList[-1]
    while counter2 != len(totalList):
        total += int(totalList[counter2])
        counter2 += 1
    counter2 = 0
    print(f"""
Name: {dataList[counter]}
Sales: {dataList2[counter]}
Total: {total}""")
    total = 0
    counter += 1
counter = 0