import random
n1 = random.randint(0,12)
n2 = random.randint(0,12)
su = n1 * n2
ans = int(input(f"What is the product of {n1} and {n2}? "))
if ans == su:
    print("well done")
else:
    print("Ur bad")
