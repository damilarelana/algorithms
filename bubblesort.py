import random
import time
#
# Generate Random Unsorted List
#
inputList = [x for x in range(0, 12276, 96)]
random.shuffle(inputList)
print("\nGiven random unsorted list (%s elements): \n%s\n" % (len(inputList), inputList))
#
#start time counter
#
start_time = time.time()


def bubbleSort(inputList: list):
    inputListLength = len(inputList)
    oCount = 0  # initialize the outer counter i.e. which controls repetition after bubbling previous largest values
    while oCount < len(inputList):  # this does not use rlistLength, to ensure we test all elements for largeness
        iCount = 0   # initialize the inner counter i.e. to move one selected element through the list
        while iCount < (inputListLength - 1):
            if inputList[iCount] > inputList[iCount+1]:
                inputList[iCount], inputList[iCount+1] = inputList[iCount+1], inputList[iCount]
            iCount += 1
        oCount += 1  # increment outer loop i.e. number of times we have so far bubbled up the largest value
        inputListLength -= 1  # decrement list length before next iteration, since previous largest value does not need to be involved in next iterations 

    return inputList  # returning a now sorted input List


bubblesorted = bubbleSort(inputList)
print("Bubble Sort gives: %s\n" % bubblesorted)
print("runtime: %s seconds\n" % (time.time() - start_time))