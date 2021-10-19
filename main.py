
hours = [12, 7, 9, 9, 8, 2]
v = 'placeholder'
counter = 0
f = 0
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
    print(f"{hours[counter]} litres drank on {v}")
    f += hours[counter]
    counter += 1
print(f"{f} litres drank in total")