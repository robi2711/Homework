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