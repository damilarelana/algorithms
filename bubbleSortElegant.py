import random
import time
#
# Generate Random Unsorted List
#
inputList = [x for x in range(0, 1247635, 96)]
random.shuffle(inputList)
1247635

# elegantBubbleSort() is an elegant implementation BUT slower


def elegantBubbleSort(inputList: list):
    inputListLength = len(inputList)
    oCount = 0  # initialize the outer counter i.e. which controls repetition after bubbling previous largest values
    while oCount < len(inputList):  # this does not use rlistLength, to ensure we test all elements for largeness
        iCount = 0   # initialize the inner counter i.e. to move one selected element through the list
        while iCount < (inputListLength - 1):
            if inputList[iCount] > inputList[iCount+1]:
                inputList[iCount], inputList[iCount+1] = inputList[iCount+1], inputList[iCount]
            iCount += 1  # so as to move on the the next adjacent elements to test
        oCount += 1  # increment outer loop i.e. number of times we have so far bubbled up the largest value
        inputListLength -= 1  # decrement list length before next iteration, since previous largest value does not need to be involved in next iterations 

    return inputList  # returning a now sorted input List


#
# Timed execution for elegantBubbleSort()
#


start_time = time.time()
elegantlyBubbleSorted = elegantBubbleSort(inputList)
print(" ================ ")
print("\n Elegant Bubble Sort gives: %s\n" % elegantlyBubbleSorted[:15])
print("runtime: %f seconds\n" % (time.time() - start_time))