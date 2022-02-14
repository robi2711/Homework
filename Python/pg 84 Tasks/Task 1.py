def taskOne(name):
    name.sort()
    total = 0
    minimum = name[0]
    maximum = name[-1]
    for item in name:
        total += item
    mean = total/len(name)
    return print(f"""
Minimum = {minimum}
Maximum = {maximum}
Mean = {mean}
""")
ages = [32, 31, 30, 37, 37, 33]
earnings = [1270, 7980, 4700, 1810, 750, 110]
taskOne(ages)
taskOne(earnings)