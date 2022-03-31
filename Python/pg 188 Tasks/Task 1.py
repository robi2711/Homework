age = input("What age are you? : ")
score = input("What score did you get? : ")
if age <= 16 and score >= 80:
    print("Exellent!")
elif age >= 16 and score >= 80:
    print("Good!")
else:
    print("Try harder next time!")