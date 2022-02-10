import lib as m
import random

file = "Task3.csv"
counter = 0
m.fw(file, "")

while counter != 100:
    randint = random.randint(1, 100)
    m.fa(file, f"{randint},")
    counter += 1