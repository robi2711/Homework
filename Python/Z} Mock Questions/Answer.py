# print("This program can find the perimeter or area of a quadrilateral")
# lenght = float(input("Please enter the length: "))
# width = float(input("Please enter the width: "))
# userName = input("Please enter your user name: ")
# choice = input("Do you want to find the (p)erimiter or (a)rea? ")
# 
# if choice == "p":
#     print(f"A quadrilateral with the lenght of {lenght} and a width of {width} has an perimeter of: {round(lenght*2+width*2, 2)}")
# elif choice == "a":
#     print(f"A quadrilateral with the lenght of {lenght} and a width of {width} has an area of: {round((length*width, 2))}")




#Q16
import random


pchoice = input("Enter rock, paper or scissors: ")
print(f"player choose: {pchoice}")
computer_options = ["rock", "paper", "scissors"]
cchoice = computer_options[random.randint(0,2)]
