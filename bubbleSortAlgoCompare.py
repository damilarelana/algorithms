import random
import time
import copy
#
# Generate Random Unsorted List
#
inputList = [x for x in range(0, 1247635, 96)]
random.shuffle(inputList)

# create distinct copies of the now reshuffled list [so as to ensure objectivity in the sorting]
hBSInputList = copy.deepcopy(inputList)
kBSInputList = copy.deepcopy(inputList)
eBSInputList = copy.deepcopy(inputList)

# elegantBubbleSort() is an elegant implementation


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
# - it uses a swap flag AND break point
# - WITHOUT even reducing the inputListLength, after each inner loop iteration


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
elegantlyBubbleSorted = elegantBubbleSort(eBSInputList)
print(" ================ ")
print("\nElegant Bubble Sort gives [first 15 elements as]: %s" % elegantlyBubbleSorted[:15])
print("runtime: %f seconds\n" % (time.time() - start_time))


#
# Timed execution for kindaBubbleSort()
#

start_time = time.time()
kindaBubblesorted = kindaBubbleSort(kBSInputList)
print(" ================ ")
print("\nKinda Bubble Sort gives [first 15 elements as]: %s" % kindaBubblesorted[:15])
print("runtime: %f seconds\n" % (time.time() - start_time))


#
# Timed execution for hybridBubbleSort()
#

start_time = time.time()
hybridBubblesorted = hybridBubbleSort(hBSInputList)
print(" ================ ")
print("\nHybrid Bubble Sort gives [first 15 elements as]: %s" % hybridBubblesorted[:15])
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
