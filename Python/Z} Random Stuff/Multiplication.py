import random
import time

while True:
    n1 = random.randint(0,12)
    n2 = random.randint(0,12)
    su = n1 * n2
    t0= time.perf_counter()
    ans = int(input(f"What is the product of {n1} and {n2}? "))
    if ans == su:
        print("well done")
        t1 = time.perf_counter() - t0
        print(f"{round(t1, 1)} Seconds elapsed")
    else:
        print("Ur bad")
        t1 = time.perf_counter() - t0
        print(f"{round(t1, 1)} Seconds elapsed")
