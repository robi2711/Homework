import random
def fa(name, write):
    file = open(name, "a")
    file.write(write)
    file.close

def fw(name, write):
    file = open(name, "w")
    file.write(write)
    file.close
    
def fr(name):
    file = open(name, "r")
    return file.read()
    file.close

csv = "task5.csv"
GUESS = 2
times = 200
counter = 0

fw(csv, "")

while counter != times:
    pass