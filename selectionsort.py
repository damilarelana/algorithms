import random
import time

rlist = [x for x in range(0, 12276, 96)]    # Generate Random Unsorted List
random.shuffle(rlist)
loopRange = len(rlist)                      # avoids repeating len() on large lists
print("\nGiven random unsorted list (%s elements): \n%s\n" % (loopRange, rlist))

start_time = time.time()                    # start time counter
def selectionSort(rlist):
    global loopRange                        # declare loopRange as global to ensure its same within selectionSort(rlist)
    if loopRange == 1:
        return rlist
    else:
        outerCount = 0                      # initialise inner and out loop counters
        minElement = outerCount             # assume first index "0" is temporary minimum (changes with each pass)
        while outerCount < loopRange:       # using "for ... in ... range()" would give same result
            innerCount = outerCount + 1     # make (or reset) innerCount to current "outerCount + 1"
            while innerCount < loopRange:
                if rlist[innerCount] < rlist[minElement]:
                    minElement = innerCount
                innerCount += 1             # increase inner counter i.e. reducing unsorted set
            rlist[outerCount], rlist[minElement] = rlist[minElement], rlist[outerCount]  # confirm actual minimum by swapping
            outerCount += 1                 # increase outer counter i.e. expanding the sorted set
            minElement = outerCount         # reset new temporary minimum
            if outerCount == loopRange - 1: # i.e. only one unsorted element remains, break outer loop
                break
        return rlist
selectionsorted = selectionSort(rlist)
print("Selection Sort gives: %s\n" % selectionsorted)
print("runtime: %s seconds\n" % (time.time() - start_time))