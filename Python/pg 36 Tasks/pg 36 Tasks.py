#pg 26 Tasks
#Task 1
for y in range(1, 11):
    print(y)
b = 0
while b != 10:
    b += 1
    print(b)
#Task 2
a =  int(input("Input a number > "))
for y in range(0,a+1):
    print(y)

#Task 3
sentence = input("Write a sentence > ")
counter = 0
z = 0
while counter < len(sentence):
    if sentence[counter] == "a":
        z += 1
    if sentence[counter] == "e":
        z += 1
    if sentence[counter] == "i":
        z += 1
    if sentence[counter] == "o":
        z += 1
    if sentence[counter] == "u":
        z += 1
    counter += 1
print(z)

#Task 4
sentence = input("Write a sentence > ")
print(sentence[::-1])

#Task 5
sentence = input("Write a sentence > ")
b = input("Write a char: ")
counter = 0
z = 0
while counter < len(sentence):
    if sentence[counter] == b:
        z += 1
    counter += 1
print(z)
