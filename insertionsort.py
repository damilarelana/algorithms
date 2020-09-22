import random
import time
#
# Generate Random Unsorted List
ulist = [x for x in range(0, 12276, 96)]
random.shuffle(ulist)
loopRange = len(ulist)                      # avoids repeating len() on large lists
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("")
print("A python implementation of Insertion Sort algorithm :")
print("  - using random generated data")
print("  - of an array of integer values")
print("  - with {} elements".format(loopRange))
print("")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


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


# start time counter
start_time = time.time()
leSorted = insertionSort(ulist)
print("Insertion Sort gives: %s\n" % leSorted)
print("runtime: %s seconds\n" % (time.time() - start_time))