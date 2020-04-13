import random
import time
#
# Generate Random Unsorted List
#
rlist = [x for x in range(0, 1247635, 96)]
random.shuffle(rlist)
loopRange = len(rlist)                      # avoids repeating len() on large lists
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("")
print("A python implementation of a Bubble Sort algorithm:")
print("  - using randomly generated data")
print("  - of an array of integer values")
print("  - with {} elements".format(loopRange))
print("")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

# kindaBubbleSort() is a less elegant solution BUT faster
# - it uses a swap flag AND break point
# - WITHOUT even reducing the inputListLength, after each inner loop iteration
# - it 10x-100x faster than bubbleSortElegant.py
# - sometimes marginally faster (or marginally slower) than bubbleSortHybrid.py


def kindaBubbleSort(inputList: list):
    oCount = 0  # outer counter initialization
    while oCount < len(inputList):
        # handles already sorted input and sorting completion
        swapflag = False
        iCount = 0  # inner counter initialization
        while iCount < (len(inputList)-1):
            if inputList[iCount] > inputList[iCount+1]:  # this sorts in ascending order
                inputList[iCount], inputList[iCount+1] = inputList[iCount+1], inputList[iCount]
                swapflag = True
            iCount += 1
        # break from loop if already sorted input and sorting completion
        if not(swapflag):
            break
        oCount += 1
    return inputList

#
# Timed execution for kindaBubbleSort()
#


start_time = time.time()
kindaBubblesorted = kindaBubbleSort(rlist)
print(" ================ ")
print("\n Kinda Bubble Sort gives: %s\n" % kindaBubblesorted)
print("runtime: %f seconds\n" % (time.time() - start_time))
