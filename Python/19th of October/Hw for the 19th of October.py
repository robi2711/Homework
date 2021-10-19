"""
a list is a variable that stores more than one item
It is more neat and fast
list1 = [1, 2]
items
list2 = []
list
1
.count
to start a list
they can be changed
22
inserts 1 in the 13th space
list4 = [1]
list5 = [2]
list4 + list5
list4 * 4
"""

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
while counter != 7:
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
