import random
a = 0
w = 0
low  = random.randint(1,100) 
high = random.randint(low,100)
num = int(input("How many random numbers do you want to generate? "))
average = input("Do you want to get the average of these numbers")
while a != num:
    n = random.randint(low, high)
    w += n
    print(w)
    a += 1
