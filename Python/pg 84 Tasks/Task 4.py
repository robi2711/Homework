import lib as m
text = m.fr("Task 4.txt")
text.replace("\n", " ")
f1, f2 = m.freq(text.split(" "))
del f1[36]
del f2[36]
num = []
var = []
num1 = []
var1 = []
num2 = []
counter = 0
while counter != len(f2):
    if f2[counter] >= 8:
        num.append(f2[counter])
        var.append(f1[counter])
    counter += 1
for item in num:
    if item not in num1:
        num1.append(item)
numsort = num1
numsort.sort()
for item in num1:
    freq = num.count(item)
    if freq != 1:
        while freq != 1:
            freq = num.count(item)
            index = num.index(item)
            num2.append(item)
            var1.append(var[index])
            num[index] = 0
    else:
        num2.append(item)
        var1.append(var[num.index(item)])
counter = -1
while counter != -20:
    print(f"Word: {var1[counter]}                                       Frequency: {num2[counter]}")
    counter -= 1