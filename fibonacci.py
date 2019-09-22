import math
import time

#define nestedSum function
def fibonnaci(testnumber):
    if testnumber in [0, 1]:
        fibonnaciValue = testnumber
    elif testnumber < 0:
        testnumber = int(input("Enter a non-negative sequence index: "))
        print("New sequence index: %d" % testnumber)
        fibonnaciValue = fibonnaci(testnumber)
        return fibonnaciValue
    else:
        fibonnaciValue = fibonnaci(testnumber-1) + fibonnaci(testnumber-2)
    return fibonnaciValue


# call functions
start_time = time.time()
testfigure = 10
print("Fibonacci value is: %d" % fibonnaci(testfigure))
print("Time: %f seconds" % (time.time() - start_time))
print("Initial Sequence index: %s" % testfigure)
