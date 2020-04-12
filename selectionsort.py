import random
import time

rlist = [x for x in range(0, 12276, 96)]    # Generate Random Unsorted List
random.shuffle(rlist)
loopRange = len(rlist)                      # avoids repeating len() on large lists
print("\nGiven random unsorted list (%s elements): \n%s\n" % (loopRange, rlist))

start_time = time.time()                    # start time counter

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


selectionsorted = selectionSort(rlist)
print("Selection Sort gives: %s\n" % selectionsorted)
print("runtime: %s seconds\n" % (time.time() - start_time))