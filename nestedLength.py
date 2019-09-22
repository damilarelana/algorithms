import math
import random
import time

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

# call and print nestedSum
print("\nFound %d elements in nested list" % nestedLength(nestedList))
print("Time (to count elements): %f seconds\n" % (time.time() - start_time))