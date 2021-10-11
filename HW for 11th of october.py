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

