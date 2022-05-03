def factorial(num):
    if num == 1:
        return num
    else:
        return num*factorial(num-1)

testInput = 5
testFactorial = 1
for i in range (1,int(testInput)+1):
   testFactorial = testFactorial * i
expectedAns = testFactorial
testAns = factorial(5)

passed = True
if expectedAns != testAns:
    passed = False
print(passed)