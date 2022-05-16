# def FibonnaciIteration(limit):
#     start = 0
#     num2 = 1
#     print(start)
#     print(num2)
#     for i in range(limit):
#         n = start+num2
#         print(n)
#         if i%2 == 0:
#             start = n
#         else:
#             num2 = n
# 
# def addUp(numIn):
#     if numIn > 1:
#         return numIn + addUp(numIn-1)
#     else:
#         return 1
# 


def Fibonnaci(k):
    if k in (1,2):
        return 1
    else:
        return Fibonnaci(k-1)+Fibonnaci(k-2)
for i in range(1,10):
    print(Fibonnaci(i))
    
