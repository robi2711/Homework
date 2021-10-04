name = input("What is your full name? ")
sname = name.index(" ")
fname = name[:sname]
lname = name[sname+1:]
print(fname)
print(lname)
