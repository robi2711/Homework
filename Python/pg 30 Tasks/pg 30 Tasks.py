#tasks
#Task 1
a = int(input("Write a number? "))
b = int(input("Write a number? "))
if a%b > 0:
    print("This num does not divide into 0")
else:
    print("This number divides perfectly")
    
    
#Task 2
age = int(input("What age are you? "))
if age < 17:
    print("You are not eligible for a driving test")
else:
    print("You are eligible for a driving test")


#Task 3
cost = int(input("What is the cost of the item? "))
if 500 > cost > 10000:
    print("Need quotes")
elif cost < 500:
    print("You can buy it")
else:
    print("Must to tender")


#Task 4

user = input("Write A/B/C > ")
if user.upper() == "A":
    print("You have won a ticket to Dundrum shopping centre")
elif user.upper() == "B":
    print("You have won a ticket to Tallaght")
elif user.upper() == "C":
    print("You have won a ticket to Broombridge")
else:
    print("Invalid input")
    
    
#Task 5

percentage = int(input("What percentage did you get? "))
if 100 >= percentage >= 90:
    print("You got a H1")
elif 89 >= percentage >= 80:
    print("You got a H2")
elif 79 >= percentage >= 70:
    print("You got a H3")
elif 69 >= percentage >= 60:
    print("You got a H4")
elif 59 >= percentage >= 50:
    print("You got a H5")
elif 49 >= percentage >= 40:
    print("You got a H6")
elif 39 >= percentage >= 30:
    print("You got a H7")
elif percentage < 30:
    print("You got a H8")
else:
    print("Sorry i didnt understand that...")

"""
1. When a program runs over itself multiple times
2. a loop puts the prgram in a loop
3. while loop makes program loop while it is not true
4. Bool
5. True
6. :
7.
8.
9. while True:
10. to loop over something a number of times or infinite times
11. When a loop is repeated one time too many
12. add += 1 rin the loop
13. It ends as soon as you want it to
"""

#Task 1
counter = 1000
if counter >= 1000:
    x = True
while counter != 1500 and x:
    print(counter)
    counter += 1

#Task 2
d = 0
w = 0
while a != 6:
    b = int(input("Write a number > "))
    if b <= 0:
        print("Invalid number (Write a number more than 0)")
    else:
        w += b
        d += 1
print(w)


#Task 3
a = input("What is your name? ")
PASSWORD = "1234"
while a.upper() != "MAUREEN":
    print("Welcome!")
    p = input("Write a password")
    if p == PASSWORD:
        print("Access Granted")
        quit(1)
    else:
        print("Access Denied")
print("You are not Maureen...")

#Task 4
idk1 = 0
idk2 = 0
c = int(input("Write the limit > "))
k = 0
while k != c:
    g = k % 2
    if g == 1:
        idk1 += 1
    else:
        idk2 += 1
    k += 1
print(f"{idk1} odd numbers")
print(f"{idk2} even numbers")

#Task 6
r = input("Write a sentence > ")
o = r.count(" ")
print(f"{o} number of spaces")
print(f"{o+1} number of sentence")

#Task 7
z = input("""
What would you like? 
 ---------------
|   curtains    |
|               |
|   cushion     |
|   covers      |
|               |
|   quilts      |
 ---------------
e = exit
 > 
""")
if z.upper() == "CURTAINS":
    print(f"You got {z}")
if z.upper() == "CUSHION COVERS":
    print(f"You got {z}")
if z.upper() == "QUILTS":
    print(f"You got {z}")
if z.upper() == "E":
    print(f"exited")
    quit(1)
