import matplotlib.pyplot as plt
def monthlyRepayment(principalAmount, interest, years):
    finalAmount = principalAmount*((1+interest)**years)
    monthlyAmount = (finalAmount/ (years*12))
    return round(monthlyAmount, 2)

def plot(inp, typ, nam, xlab, ylab):
    plt.plot(inp, typ)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.title(nam)
    plt.show()

def fa(name, write):
    file = open(name, "a")
    file.write(write)
    file.close

def fw(name, write):
    file = open(name, "w")
    file.write(write)
    file.close
    
def fr(name):
    file = open(name, "r")
    return file.read()
    file.close

f = "results.csv"
fw(f, "")
i = [0.032, 0.043, 0.037, 0.043, 0.044, 0.029, 0.028, 0.030]
t = [6, 7, 4, 3, 4, 6, 7, 9]

counter = 0
while len(i) != 0:
    print(str(monthlyRepayment(10000, i[0], t[0])))
    fa(f, f"str(monthlyRepayment(10000, i[0], t[0])), ")
    del i[0]
    del t[0]
data = fr(f)
data = data.split(", ")
del data[-1]
plt.bar(data, t, color='green')
plt.xlabel("term")
plt.ylabel("monthly repayment")
plt.title("Loan Approval")
