import statistics
def taskTwo(name):
    z = []
    y = []
    name.sort()
    total = 0
    minimum = name[0]
    maximum = name[-1]
    for item in name:
        total += item
        if item not in z:
            z.append(item)
    for x in z:
        total2 = name.count(x)
        y.append(total2)
    mean = total/len(name)
    median = (name[int(len(name)/2)]+name[int(len(name)/2+1)])/2
    
    
    return print(f"""
Minimum = {minimum}
Maximum = {maximum}
Mean = {mean}
Median = {median}
Frequency =
{z}
{y}
///
""")
undefined = [1, 9, 3, 2, 3, 7, 6, 5, 8, 9, 1, 10]
taskTwo(undefined)
#Mode = {statistics.mode(name)}