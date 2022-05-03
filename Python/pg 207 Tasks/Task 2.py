def multiply(num1, num2):
    return num1*num2

testnum1 = 3
testnum2 = 4
expectedAns = testnum1*testnum2
testAns = multiply(testnum1, testnum2)

passed = True
if expectedAns != testAns:
    passed = False
print(passed)