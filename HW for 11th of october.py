"""
1. Boole worked on the boolean system and worked at Queen's College Cork
2. Boolean logic
3. to compare two numbers or variables
4.  < less than
    > greater than
    <= less than or equal to
5.True or False
6. False
7. comparisons that gie a boolean as an answer
8. values and operators
9. and, or and not
10. every result that can occur when a boolean operator is used
11.
12. if johns age is 20 or aifes age is 17
    if aoifes age is not 17
    if aoifes age is not 15
    if aoifes age is less than 20 and johns age is more than 9
13.conditionals use boolean expressions to tesr if something is true or false
14. when the variable is true
15. if statement
16. if ->
    |    |
    |    |
    +<----
20. if there is a connection between the if and elif
"""
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
