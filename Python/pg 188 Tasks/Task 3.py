from datetime import date
d = date.today()
month = int(d.strftime("%m"))

bd = int(input("What month is your birthday?(in numbers) : "))
m1 = bd-month
if m1 >= 0:
    print(f"Your birthday is in {m1} months (This Year)")
elif m1 <= -1:
    print(f"Your birthday is in {12-m1} months (Next Years)")
else:
    exit()