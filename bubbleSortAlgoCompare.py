import random
import time
#
# Generate Random Unsorted List
#
inputList = [11136, 4896, 5088, 2400, 1824, 4608, 6624, 11904, 6816, 4704, 2688, 9408, 6720, 2016, 7488, 4992, 2880, 2496, 192, 5280, 8928, 2976, 5664, 384, 10944, 10368, 4416, 3456, 480, 1920, 6240, 3168, 8256, 864, 10656, 576, 5184, 1440, 768, 11424, 9600, 9024, 7104, 1248, 5376, 11232, 4320, 7392, 10752, 2304, 2784, 1536, 672, 6912, 9696, 6144, 3648, 1344, 9312, 8064, 5472, 12096, 8352, 3840, 5952, 6528, 9120, 9984, 96, 1152, 4032, 3936, 2592, 11520, 10176, 11328, 12000, 12192, 4224, 8160, 7296, 6432, 1728, 9792, 4512, 10272, 8640, 10464, 8832, 3360, 0, 8736, 10560, 4800, 11616, 1632, 11712, 7872, 10080, 288, 9888, 5568, 9216, 1056, 6336, 7776, 7200, 3552, 11808, 10848, 7680, 8448, 6048, 5760, 11040, 960, 7968, 7584, 3072, 3744, 2112, 2208, 5856, 7008, 3264, 8544, 4128, 9504]
random.shuffle(inputList)

# elegantBubbleSort() is an elegant implementation BUT slower


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


# kindaBubbleSort() is a less elegant solution BUT faster
# - it uses a swap flag AND break point
# - WITHOUT even reducing the inputListLength, after each inner loop iteration
# - it 10x-100x faster than bubbleSortElegant.py
# - sometimes marginally faster (or marginally slower) than bubbleSortHybrid()

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

# hybridBubbleSort() is a combination of the two
# - it is an hybrid in the sense that it dynamically adjusts
# - by reducing the inputListLength, after each inner loop iteration
# - while still using a swap flag AND break point
# - it 10x-100x faster than bubbleSortElegant.py
# - sometimes marginally faster (or marginally slower) than kindaBubbleSort()


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
# checkOrderedListEquivalence() a brutal bruteforce check for whether two lists are identical
# - in terms of:
#   + types of elements
#   + number of elements
#   + order of elements
# - assumes that the lists `r` and `k` are ordered
# - it however cannot check order of elements: since sets are random
# - it works best if the lists are already consisting of unique elements
#   + hence removal of duplicated elements (during intersection) would not be a problem
# - criteria of equivalence:
#   + len(set(r).intersection(k)) == len(set(k)) [solves for when set(r) is {} but set(k) is not]
#   + len(set(r)) == len(set(k))  [solves for the duplication issue]
#   + r == k [solves for element-wise comparison and order]
#   + len(r) == len(k) [also solves for duplication issues]


def checkOrderedListEquivalence(r: list, k: list):

    # intersection test parameters
    resultSet = set(r).intersection(k)
    rSet = set(r)
    kSet = set(k)
    resultSetLength = len(resultSet)
    rSetLength = len(rSet)
    kSetLength = len(kSet)

    # list test parameters
    rLength = len(r)
    kLength = len(k)

    # Test for equivalence
    if (resultSetLength == kSetLength) and (rSetLength == kSetLength) and (r == k) and (rLength == kLength):
        return True
    return False


#
# Timed execution for elegantBubbleSort()
#


start_time = time.time()
elegantlyBubbleSorted = elegantBubbleSort(inputList)
print(" ================ ")
print("\n Elegant Bubble Sort gives: %s\n" % elegantlyBubbleSorted)
print("runtime: %f seconds\n" % (time.time() - start_time))


#
# Timed execution for kindaBubbleSort()
#

start_time = time.time()
kindaBubblesorted = kindaBubbleSort(inputList)
print(" ================ ")
print("\n Kinda Bubble Sort gives: %s\n" % kindaBubblesorted)
print("runtime: %f seconds\n" % (time.time() - start_time))


#
# Timed execution for hybridBubbleSort()
#

start_time = time.time()
hybridBubblesorted = hybridBubbleSort(inputList)
print(" ================ ")
print("\n Hybrid Bubble Sort gives: %s\n" % hybridBubblesorted)
print("runtime: %f seconds\n" % (time.time() - start_time))
print("\n ================ ")


#
# # Check if both sorted list are equivalent
# #
eBSkBS = checkOrderedListEquivalence(elegantlyBubbleSorted, kindaBubblesorted)
hBSkBS = checkOrderedListEquivalence(hybridBubblesorted, kindaBubblesorted)
if eBSkBS and hBSkBS:
    print("\nAll algorithms give the same sorted list")
else:
    print("\nAll algorithms did NOT give the same sorted list")
