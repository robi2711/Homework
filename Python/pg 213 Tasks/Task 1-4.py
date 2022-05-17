# Task 1
# look at the first value... if the value is not the key then look at the next value etc.
# Task 2
# look at the middle value of the list... if the key is smaller than the value look at the first half of the list... if the key is bigger than the value then look at the second half of the list. etc.
# Task 3
# Explained in the questions
# Task 4

inList = [19, 87, 1, -1, 11, 0, -1, 33, 19]
key = int(input("What is the key"))
section = input("What part of the question do you want to do?")
if section == "a":
  counter = 0
  while counter != len(inList):
    if key == inList[counter]:
      found = True
      print(f"The key can be found at loc: {counter+1}")
    counter += 1
    if found != True:
      print(f"key:{key} was not found!")
if section == "d":
  low = 0
  high = len(inList) - 1
  mid = 0
  while low <= high:
    mid = (high + low) // 2
    if inList[mid] < key:
        low = mid + 1
    elif inList[mid] > key:
        high = mid - 1
    else:
      answer = mid
  print(answer)
      
