import random
def dice_roll():
    return random.randint(1,6)
user_guess = int(input("Write a random number between 1 and 6 "))
if user_guess != dice_roll():
    print("Wrong guess!")
else:
    print("Correct")