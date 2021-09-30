add = 0
day = int(input("What day of the month is it? "))
month = int(input("What month is it in numbers? "))
year = int(input("What year is it in nums? "))
if month == 2:
    month = 14
    add += 1
elif month == 1:
    month = 13
    add += 1
else:
    month += 2
y = year % 100
l = year / 100
c = round(l,0)
w = (day + (13 * (month + 1) / 5) + y + (y / 4) + (c / 4) - (2*c)) % 7
print(w)