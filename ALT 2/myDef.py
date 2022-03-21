#Def's
import matplotlib.pyplot as plt
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

def dataclean(dataIn, output):
    counter2 = 0
    twice = False
    once = False
    file = open(dataIn, "r")
    dataz = file.read()
    file.close
    dataListz = dataz.split("\n")
    file = open(output, "w")
    file.write("")
    file.close
    file = open(output, "a")
    for x in dataListz:
        dataz = x.split("\"\"")
        for idx, ele in enumerate(dataz):
            dataz[idx] = ele.replace("\"", '')
        while counter2 != len(dataz):
            file.write(f"{dataz[counter2]},")
            counter2 += 1
        file.write("\n")
        counter2 = 0
        twice = False
        once = False
    file.close



def plot(inp, typ, nam, xlab, ylab):
    plt.plot(inp, typ)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.title(nam)
    plt.show()
    

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