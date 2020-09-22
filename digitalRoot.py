import math
import time


#define digitalSum function
def digitalSum(testnumber):
    if testnumber in [x for x in range(0, 10)]:
        digitalSumValue = testnumber
    elif testnumber < 0:
        testnumber = int(input("Enter a non-negative number: "))
        print("New test number: %d" % testnumber)
        digitalSumValue = digitalSum(testnumber)
        return digitalSumValue
    else:
        digitalSumValue = testnumber % 10 + (digitalSum(testnumber // 10))
    return digitalSumValue


#define digitalRoot function
def digitalRoot(testnumber):
    if testnumber in [x for x in range(0, 10)]:
        digitalRootValue = testnumber
        return digitalRootValue
    else:
        testnumber = digitalSum(testnumber)
        digitalRootValue = digitalRoot(testnumber)
        return digitalRootValue


# call functions
start_time = time.time()
testfigure = 1900
print("DigitalRoot is: %d" % digitalRoot(testfigure))
print("Time: %f seconds" % (time.time() - start_time))
print("Initial test number: %s" % testfigure)