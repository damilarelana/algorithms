import math
import time

#define nestedSum function
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


# call functions
start_time = time.time()
testfigure = 234535675757523
print("DigitalSum is: %d" % digitalSum(testfigure))
print("Time: %f seconds" % (time.time() - start_time))
print("Initial test number: %s" % testfigure)