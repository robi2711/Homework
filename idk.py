a = []
add = 0
while True:
    cont = input("Would you like to add anything to the Array? y/n > ")
    if cont == "y":
        b = str(input("what would you like to add? >"))
        a.append(b)
    if cont == "n":
        quit(1)
    if cont == "see":
        print(a)
        print("Lenght of array = ", len(a))
