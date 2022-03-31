bags = int(input("How many bags did you buy?| : "))
gold = input("Are you a gold?| : ")
if gold.upper == "Y" or "YES":
    gold = True
else:
    gold = False

if bags >= 100:
    if gold:
        sale = (2.23*bags)-((2.23*bags)/13.5)
    else:
        sale = (2.23*bags)-((2.23*bags)/10)
elif bags >= 25:
    if gold:
        sale = (2.23*bags)-((2.23*bags)/8.5)
    else:
        sale = (2.23*bags)-((2.23*bags)/5)
else:
    if gold:
        sale = (2.23*bags)-((2.23*bags)/3.5)
    else:
        sale = (2.23*bags)

print(f"Your total is £{round(sale, 2)}")