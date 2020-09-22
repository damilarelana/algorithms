import math
import random
import time

rlist = [x for x in range(0, 1247635, 96)]    # Generate Random Unsorted List
random.shuffle(rlist)
loopRange = len(rlist)                      # avoids repeating len() on large lists
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("")
print("A python implementation of Merge Sort algorithm:")
print("  - using randomly generated data")
print("  - of an array of integer values")
print("  - with {} elements".format(loopRange))
print("")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

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
        demarcationIndex = int(math.ceil(temploopRange/2))          # words for even, odd and prime temploopRange values
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
#


start_time = time.time()                    # start time counter
mergeSorted = mergeSort(rlist)
print("Merge Sort gives [first 15 elements as]: %s" % mergeSorted[:15])
print("runtime: %s seconds" % (time.time() - start_time))
print("largest number is : {}".format(mergeSorted[loopRange-1]))
print("smallest number is : {}\n".format(mergeSorted[0]))