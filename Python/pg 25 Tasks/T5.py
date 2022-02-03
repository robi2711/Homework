a = []
b = 0
while b < 5:
    c = input("write random letters > ")
    a.append(c)
    b += 1
b = 0
while b < 5:
    print(f"{a[b]} is {ord(a[b])} in ascii")
    b += 1
