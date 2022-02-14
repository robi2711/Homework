#Def's
def fw(name, write):
    file = open(name, "w")
    file.write(write)
    file.close


def fa(name, write):
    file = open(name, "a")
    file.write(write)
    file.close


def fr(name):
    file = open(name, "r")
    return file.read()
    file.close

def freq(name):
    z = []
    y = []
    for item in name:
        if item not in z:
            z.append(item)
    for x in z:
        total = name.count(x)
        y.append(total)
    return z, y
    
