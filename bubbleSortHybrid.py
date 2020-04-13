import random
import time
#
# Generate Random Unsorted List
#
rlist = [x for x in range(0, 124763258, 96)]
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

# hybridBubbleSort() is a combination of the bubbleSortElegant.py and bubbleSortKinda.py
# - it is an hybrid in the sense that it dynamically adjusts
# - by reducing the inputListLength, after each inner loop iteration
# - while still using a swap flag AND break point
# - it 10x-100x faster than bubbleSortElegant.py
# - sometimes marginally faster (or marginally slower) than kindaBubbleSort.py


def hybridBubbleSort(inputList: list):
    inputListLength = len(inputList)
    oCount = 0  # outer counter initialization
    while oCount < len(inputList):
        # handles already sorted input and sorting completion
        swapflag = False
        iCount = 0  # inner counter initialization
        while iCount < (inputListLength - 1):
            if inputList[iCount] > inputList[iCount+1]:  # this sorts in ascending order
                inputList[iCount], inputList[iCount+1] = inputList[iCount+1], inputList[iCount]
                swapflag = True
            iCount += 1
        # break from loop if already sorted input and sorting completion
        if not(swapflag):
            break
        oCount += 1
        inputListLength -= 1  # decrement list length before next iteration, since previous largest value does not need to be involved in next iterations 
    return inputList
#
# Timed execution for hybridBubbleSort()
#


start_time = time.time()
hybridBubblesorted = hybridBubbleSort(rlist)
print(" ================ ")
print("\nHybrid Bubble Sort gives [first 15 elements as]: %s\n" % hybridBubblesorted[:15])
print("runtime: %f seconds\n" % (time.time() - start_time))
