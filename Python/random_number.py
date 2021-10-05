import random
import time

a = 0
w = 0
num = int(input("How many random numbers do you want to generate? > "))
average = input("Do you want to get the average of these numbers(y/n)? > ")
start_time = time.time()
while a != num:
    n = random.randint(1, 100)
    w += n
    print(n)
    a += 1
elapsed_time = time.time() - start_time
print(f"Time elapsed: {round(elapsed_time, 2)} seconds passed")
if average == "y":
    print(f"The average is {w/num}")
