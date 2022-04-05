hours = int(input("How many hours are you going to drive for? : "))
mtype = input("50cc or 250cc? ")
weekend = input("Is it weekday or weekend? 1/2 ")
threeless = False
if hours <= 3:
    hours-=3
    threeless = True
else:
    hours-=3
if mtype == "50cc" and weekend == "1":
    if threeless:
        pay = 15
    if not threeless:
        pay = 15 + (2.50*hours)
elif mtype == "50cc" and weekend == "2":
    if threeless:
        pay = 30
    if not threeless:
        pay = 30 + (3*hours)
elif mtype == "250cc" and weekend == "1":
    if threeless:
        pay = 25
    if not threeless:
        pay = 25 + (3.50*hours)
elif mtype == "250cc" and weekend == "2":
    if threeless:
        pay = 35
    if not threeless:
        pay = 35 + (5*hours)
