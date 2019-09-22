import math
import random
import time

#define nestedSum function
def nestedSum(nestedList):
    nestedSumValue = 0
    for element in nestedList:
        if isinstance(element,list):
            nestedSumValue += nestedSum(element)
        else:
            nestedSumValue += element
    return nestedSumValue

#define nestedSum function
def nestedLength(nestedList):
    counter = 0
    for element in nestedList:
        if isinstance(element,list):
            counter += nestedLength(element)
        else:
            counter += 1
    return counter

# Generate Random List
nestedListtemp = [x for x in range(0,128976453,8)]
random.shuffle(nestedListtemp)
nestedList = [1, 2, [11, 13], 8, nestedListtemp]
start_time = time.time()

# call functions
print("\nNested list has: %s elements" % nestedLength(nestedList))
print("Sum (of elements): %d" % nestedSum(nestedList))
print("Time (to add elements): %f seconds\n" % (time.time() - start_time))