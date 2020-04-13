import random
import time
import math
import copy
from matplotlib import pyplot as plt

#
# Generate Random Unsorted List
#
inputList = [x for x in range(0, 1247635, 96)]    # Generate Random Unsorted List
random.shuffle(inputList)

# create distinct copies of the now reshuffled list [so as to ensure objectivity in the sorting]
hBSInputList = copy.deepcopy(inputList)
eBSInputList = copy.deepcopy(inputList)
sSInputList = copy.deepcopy(inputList)
mSInputList = copy.deepcopy(inputList)
iSInputList = copy.deepcopy(inputList)


#
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("")
print("Comparing performance of 5 algorithms [ mergeSort + hybridBubbleSort + elegantBubbleSort + selectionSort + insertionSort]:")
print("  - using randomly generated data")
print("  - of an array of integer values")
print("  - with {} elements".format(len(inputList)))
print("")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


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

# selectionSort()
# - works by:
#   + assume l[0] is minimum
#   + saves the index of l[0] into a temporary placeholder
#   + scans all remaining items i.e. the innerCount being always one index ahead of the outerCount
# - sorts in an ascending order
# - all this is happening in place
#   + we are just using `outcounter` to implement a virtual segregation of what is sorted and unsorted


def selectionSort(rlist):
    loopRange = len(rlist) 
    if loopRange == 1:
        return rlist
    else:
        outerCount = 0                      # initialise outerloop counter
        minElement = outerCount             # assume first index "0" is temporary minimum (changes with each pass)
        while outerCount < loopRange:       # using "for ... in ... range()" would give same result
            innerCount = outerCount + 1     # make (or reset) innerCount to current "outerCount + 1"
            while innerCount < loopRange:   # scanning by looping over all remaining items to test new minimum
                if rlist[innerCount] < rlist[minElement]:  # if any of the items if less than current minimum
                    minElement = innerCount  # swaps out the index of the old with the new i.e. create new temporary minimum for remaining unsorted set
                innerCount += 1             # increase inner counter i.e. reducing unsorted list of items
            rlist[outerCount], rlist[minElement] = rlist[minElement], rlist[outerCount]  # confirm new minimum by swapping [temporary outerCount index with new minimum's index]
            outerCount += 1                 # increase outer counter i.e. expanding the sorted set
            minElement = outerCount         # reset new temporary minimum index e.g. if initial was index `0`, it would now be `1` 
            if outerCount == loopRange - 1:  # i.e. only one unsorted element remains, break outer loop
                break
            # note that we CANNOT use the optimization (loopRange -= 1) since we are shifting values/index around 
            # as such the last value after every iteration can still need to be touched
            # this is one difference with BubbleSort() where the last index can be removed from dataset after every loop
        return rlist


# mergeSort()
# - works by:
#   + splitting the iteratively splitting the original lists into sublists
#   + until you have sublists that are not more than 1 element long i.e. inherently sorted
#   + iteratively compares and determines whether to `append sublist1` to `sublist2` OR `append sublist2 to sublist1`
# - this is NOT happening in place
#   + hence there is a space penalty for the algorithm


def mergeSort(rlist):
    temploopRange = len(rlist)                                      # handles reducing elements, so can't use global

    if temploopRange < 2:                                           # using "<2" instead of "==", handles when rlist=[]
        return rlist
    else:
        demarcationIndex = int(math.ceil(temploopRange/2))          # works for even, odd and prime temploopRange values
        tempListOne = rlist[:demarcationIndex]                      # initialize tempListOne sub-list
        tempListTwo = rlist[demarcationIndex:]                      # initialize tempListTwo sub-list
        tempListOne = mergeSort(tempListOne)                      # recursive call to mergeSorter()
        tempListTwo = mergeSort(tempListTwo)                      # recursive call to mergeSorter()
        return sublistMerge(tempListOne, tempListTwo)


# sublistMerge()
# - is called by mergeSort()
# - to handle list merging operations

def sublistMerge(tempSubListOne, tempSubListTwo):
    tempMergedList = []                                             # initialise empty List to merge sub-Lists into

    loopRangeSubListOne = len(tempSubListOne)
    loopRangeSubListTwo = len(tempSubListTwo)

    indexSubListOne = 0                                             # avoids using list.pop() to remove element
    indexSubListTwo = 0

    while loopRangeSubListOne > indexSubListOne and loopRangeSubListTwo > indexSubListTwo:      # a=[1]->len(a)=1
        if tempSubListOne[indexSubListOne] > tempSubListTwo[indexSubListTwo]:                   # test smaller element
            tempMergedList.append(tempSubListTwo[indexSubListTwo])                         # add to end of tempMergeList
            indexSubListTwo += 1
        else:
            tempMergedList.append(tempSubListOne[indexSubListOne])                         # add to end of tempMergeList
            indexSubListOne += 1

    while loopRangeSubListOne > indexSubListOne:                                  # no elements to merge in SubListTwo
        tempMergedList.append(tempSubListOne[indexSubListOne])                    # remaining elements are appended
        indexSubListOne += 1

    while loopRangeSubListTwo > indexSubListTwo:                                  # no elements to merge in SubListOne
        tempMergedList.append(tempSubListTwo[indexSubListTwo])                    # remaining elements are appended
        indexSubListTwo += 1
    return tempMergedList

# insertionSort()


def insertionSort(ulist):
    loopRange = len(ulist)
    if loopRange == 1:
        return ulist    # no point wasting CPU cycle to sort one item
    else:
        # we assume that element at index `0` i.e. ocount = 0, is already sorted, hence why the unsorted starts at ocount = 1
        ocount = 1                       # initialising unsorted list index to the first one to be removed from unsorted [we ]
        while ocount < loopRange:        # handles if len(ulist)=1, unsorted loop index
            icount = ocount              # re-initialising sorted list's max index to allow countdown
            while icount > 0:            # handles inner loop i.e. the `sorted list loop`. greater than zero 
                                         # helps to ensure that when you `bring` a new element (from unsorted) to test/loop against `the sorted
                                         # it helps to ensure that the looping down does not go beyond `index 0` within the sorted
                if ulist[icount-1] > ulist[icount]:           # this already carters for assuming list[0] is sorted
                    ulist[icount - 1], ulist[icount] = ulist[icount], ulist[icount-1]
                icount -= 1 # this is different to bubbleSort i.e. where there is an increment. Here we are decreasing the unsorted set

            ocount += 1 # here we are increasing the sorted set boundaries [which weirdly also acts like the next `first element of the now shrinking unsorted set`]
        return ulist


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
# Timed execution for selectionSort()
#


sSStartTime = time.time()
selectionSorted = selectionSort(sSInputList)
sSStopTime = time.time()
print("\nSelection Sort give [first 15 elements as]: %s" % selectionSorted[:15])
print("runtime: %f seconds" % (sSStopTime - sSStartTime))
print("================================")

#
# Timed execution for mergeSort()
#
mSStartTime = time.time()
mergesorted = mergeSort(mSInputList)
mSStopTime = time.time()
print("\nMerge Sort gives [first 15 elements as]: %s" % mergesorted[:15])
print("runtime: %f seconds" % (mSStopTime - mSStartTime))
print("================================")

#
# Timed execution for hybridBubbleSort()
#
hBSStartTime = time.time()
hybridBubblesorted = hybridBubbleSort(hBSInputList)
hBSStopTime = time.time()
print("\nHybrid Bubble Sort gives [first 15 elements as]: %s" % hybridBubblesorted[:15])
print("runtime: %f seconds" % (hBSStopTime - hBSStartTime))
print("================================")


#
# Timed execution for elegantBubbleSort()
#
eBSStartTime = time.time()
elegantBubblesorted = elegantBubbleSort(eBSInputList)
eBSStopTime = time.time()
print("\nElegant Bubble Sort gives [first 15 elements as]: %s" % elegantBubblesorted[:15])
print("runtime: %f seconds" % (eBSStopTime - eBSStartTime))
print("================================")

#
# Timed execution for insertionSort()
#

iSStartTime = time.time()
insertionsorted = insertionSort(iSInputList)
iSStopTime = time.time()
print("\nInsertion Sort gives [first 15 elements as]: %s" % insertionsorted[:15])
print("runtime: %f seconds" % (iSStopTime - iSStartTime))
print("================================")


#
# # Check if both sorted list are equivalent
# #
sShBS = checkOrderedListEquivalence(selectionSorted, hybridBubblesorted)
hBSmS = checkOrderedListEquivalence(hybridBubblesorted, mergesorted)
hBSiS = checkOrderedListEquivalence(hybridBubblesorted, insertionsorted)
hBSeBS = checkOrderedListEquivalence(hybridBubblesorted, elegantBubblesorted)
if sShBS and hBSmS:
    print("\nAll algorithms give the same sorted list")
else:
    print("\nAll algorithms did NOT give the same sorted list")
