def evenORodd(num1):
    z = num1&2
    if z == 0:
        return True
    else:
        return False

testNum = 4
expectedAns = True
testAns = evenORodd(testNum)

passed = True
if expectedAns != testAns:
    passed = False
print(passed)