import math
import time

#define nestedSum function
def factorial(testnumber):
    if testnumber in [0, 1]:
        factorialValue = 1
    elif testnumber < 0:
        testnumber = int(input("Enter a non-negative number: "))
        print("New test number: %d" % testnumber)
        factorialValue = factorial(testnumber)
        return factorialValue
    else:
        factorialValue = testnumber * factorial(testnumber-1)
    return factorialValue


# call functions
start_time = time.time()
testfigure = 3
print("Factorial is: %d" % factorial(testfigure))
print("Time: %f seconds" % (time.time() - start_time))
print("Initial test number: %s" % testfigure)