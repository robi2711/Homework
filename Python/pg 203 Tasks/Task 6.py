def RRP(rrp, discount):
    x = f"{discount}%: {(rrp-(rrp*(discount/100)))*rrp}"
    return x

discountList = [10, 20, 30, 40, 50, 60]
for item in discountList:
    x = RRP(100, item)
    print(x)