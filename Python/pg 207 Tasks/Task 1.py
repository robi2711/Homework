def pi():
    return 22/7
expectedAns = 22/7
testAns = pi()

passed = True
if expectedAns != testAns:
    passed = False
print(passed)