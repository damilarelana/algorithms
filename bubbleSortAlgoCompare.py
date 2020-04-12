import random
import time
#
# Generate Random Unsorted List
#
inputList = [11136, 4896, 5088, 2400, 1824, 4608, 6624, 11904, 6816, 4704, 2688, 9408, 6720, 2016, 7488, 4992, 2880, 2496, 192, 5280, 8928, 2976, 5664, 384, 10944, 10368, 4416, 3456, 480, 1920, 6240, 3168, 8256, 864, 10656, 576, 5184, 1440, 768, 11424, 9600, 9024, 7104, 1248, 5376, 11232, 4320, 7392, 10752, 2304, 2784, 1536, 672, 6912, 9696, 6144, 3648, 1344, 9312, 8064, 5472, 12096, 8352, 3840, 5952, 6528, 9120, 9984, 96, 1152, 4032, 3936, 2592, 11520, 10176, 11328, 12000, 12192, 4224, 8160, 7296, 6432, 1728, 9792, 4512, 10272, 8640, 10464, 8832, 3360, 0, 8736, 10560, 4800, 11616, 1632, 11712, 7872, 10080, 288, 9888, 5568, 9216, 1056, 6336, 7776, 7200, 3552, 11808, 10848, 7680, 8448, 6048, 5760, 11040, 960, 7968, 7584, 3072, 3744, 2112, 2208, 5856, 7008, 3264, 8544, 4128, 9504]
random.shuffle(inputList)

# elegantBubbleSort() is an elegant implementation of the bubble sort algorithm


def elegantBubbleSort(inputList: list):
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


# kindaBubbleSort() is a less elegant solution


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
# checkListEquivalence() checks whether two lists are identical
#


def checkListEquivalence(r: list, k: list):
    result = set(r).intersection(k)
    
    return bool(result)


#
# Timed execution for elegantBubbleSort()
#


start_time = time.time()
elegantlyBubbleSorted = elegantBubbleSort(inputList)
print(" ================ ")
print("\n Elegant Bubble Sort gives: %s\n" % elegantlyBubbleSorted)
print("runtime: %s seconds\n" % (time.time() - start_time))


#
# Timed execution for kindaBubbleSort()
#

start_time = time.time()
kindaBubblesorted = kindaBubbleSort(inputList)
print(" ================ ")
print("\n Kinda Bubble Sort gives: %s\n" % kindaBubblesorted)
print("runtime: %s seconds\n" % (time.time() - start_time))
print("\n ================ ")

#
# Check if both sorted list are equivalent
#
if checkListEquivalence(elegantlyBubbleSorted, kindaBubblesorted) is True:
    print("both algorithms gave the same sorted list")
elif:
    print("both algorithms did NOT give the same sorted list")
