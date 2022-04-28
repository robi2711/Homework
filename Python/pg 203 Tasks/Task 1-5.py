#1
def pi():
    return 22/7

#2
def divide(num1, num2):
    return num1/num2

#3
def countSpaces(body):
    l1 = body.split(" ")
    return len(l1)

#4
def floor_divide(num1, num2):
    z = num1&num2
    if z == 0:
        return True
    else:
        return False

#5
def countList(listInput, searchQuery):
    value = 0
    for item in listInput:
        if item == searchQuery:
            value += 1
    return value

#7
def tempChange(C, F):
    if F == 0:
        x = (C*1.8)+32
        return x
    elif C == 0:
        x = (F-32)*0.5666
        return x
