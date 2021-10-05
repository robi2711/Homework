import random
import time
while True:
    start_time = time.time()
    num1 = random.randint(1, 12)
    num2 = random.randint(1, 12)
    answer = num1*num2
    user = int(input(f"What is the sum of {num1} and {num2}? "))
    if user == answer:
        print("Thats right!")
    else:
        print(f"Thats wrong... \nThe answer is {answer}")
        elapsed_time = time.time() - start_time
        print(f"{elapsed_time} seconds taken")
