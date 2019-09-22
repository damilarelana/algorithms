import math
import random
import time

rlist = [x for x in range(0, 12276, 96)]    # Generate Random Unsorted List
random.shuffle(rlist)
loopRange = len(rlist)                      # avoids repeating len() on large lists
print("\nGiven random unsorted list (%s elements): \n%s\n" % (loopRange, rlist))
start_time = time.time()                    # start time counter

def mergeSorter(rlist):
    temploopRange = len(rlist)                                      # handles reducing elements, so can't use global

    if temploopRange < 2:                                           # using "<2" instead of "==", handles when rlist=[]
        return rlist
    else:
        demarcationIndex = int(math.ceil(temploopRange/2))          # words for even, odd and prime temploopRange values
        tempListOne = rlist[:demarcationIndex]                      # initialize tempListOne sub-list
        tempListTwo = rlist[demarcationIndex:]                      # initialize tempListTwo sub-list
        tempListOne = mergeSorter(tempListOne)                      # recursive call to mergeSorter()
        tempListTwo = mergeSorter(tempListTwo)                      # recursive call to mergeSorter()
        return sublistMerge(tempListOne,tempListTwo)
#
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
mergeSorted = mergeSorter(rlist)
#print("Merge Sort gives: %s\n" % mergeSorted)
print("runtime: %s seconds\n" % (time.time() - start_time))