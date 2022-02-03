#pg 42 Tasks
# Task 1
a = 0
List = []
while a != 5:
    b = int(input("Write a random number > "))
    List.append(b)
    a += 1
print(List)

# Task 2
hours = [12, 7, 9, 9, 8, 2]
v = 'placeholder'
counter = 0
f = 0
c = 0
while counter != 6:
    if counter == 0:
        v = 'Monday'
    elif counter == 1:
        v = 'Tuesday'
    elif counter == 2:
        v = 'Wednesday'
    elif counter == 3:
        v = 'Thursday'
    elif counter == 4:
        v = 'Friday'
    elif counter == 5:
        v = 'Saturday'
    else:
        v = 'Sunday'
    print(f"{hours[counter] * 0.5} litres drank on {v}")
    print(f"{hours[counter] * 0.5 * 1.75} euro to milk on {v}")
    f += hours[counter] * 0.5
    c += hours[counter] * 0.5 * 1.75
    counter += 1
print(f"{f} litres drank in total")

# Task 3
z = 0
List2 = []
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
counter1 = 0
while counter1 != 6:
    counter1 += 1
    d = int(input(f"What is the amount of rainfall on {days[counter1]}"))
    List2.append(d)
    z += d
print(f"Total rainfall = {z}")
print(f"Average rainfall = {z/7}")

# Task 4
names = []
sales = []
digitChecker = 'placeholder'
totalSales = 0
iterations = int(input("How many workers > "))
counter2 = 0
while counter2 != iterations:
    digitChecker = 'placeholder'
    name = input("Name of worker? ")
    while not digitChecker.isdigit():
        digitChecker = input("Sales in euro >  ")
    totalSales += int(digitChecker)
    names.append(name)
    sales.append(int(digitChecker))
    counter2 += 1
user = input("""
What would you like to see?
average = Average of all sales
sales = Total of all sales
workers = all workers and their sales
min = worker with the least amount of sales
max = worker with the most amount of sales

> 
""")
if user.lower() == "average":
    print(f"{totalSales/iterations} euro average sales")
elif user.lower() == "total":
    print(f"{totalSales} euro total sales")
elif user.lower() == "workers":
    counter2 = 0
    while counter2 != len(names):
        print(f"Name: {names[counter2]} Sales: {sales[counter2]} euro")
        counter2 += 1
elif user.lower() == "min":
    minNum = min(sales)
    minLoc = sales.index(minNum)
    print(f"Name: {names[minLoc]} Sales: {sales[minLoc]}")
elif user.lower() == "max":
    maxNum = max(sales)
    maxLoc = sales.index(maxNum)
    print(f"Name: {names[maxLoc]} Sales: {sales[maxLoc]}")
else:
    print("Sorry I don't understand that...")
