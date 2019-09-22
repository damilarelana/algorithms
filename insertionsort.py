import random
import time
#
# Generate Random Unsorted List
ulist = [x for x in range(0, 12276, 96)]
random.shuffle(ulist)
loopRange = len(ulist)                      # avoids repeating len() on large lists
print("\nGiven random unsorted list (%s elements): \n%s\n" % (loopRange, ulist))

#
#start time counter
start_time = time.time()
def insrtsort(ulist):
    ocount = 1                       # initialising unsorted list index to the first one to be removed from unsorted
    while ocount < loopRange:        # handles if len(ulist)=1, unsorted loop index
        icount = ocount              # re-initialising sorted list's max index to allow countdown
        while icount > 0:            # handles inner loop, sorted loop index
            if ulist[icount-1] > ulist[icount]:           # this already carters for assuming list[0] is sorted
                ulist[icount - 1], ulist[icount] = ulist[icount], ulist[icount-1]
            icount -= 1
        ocount += 1
    return ulist

lesorted = insrtsort(ulist)
print("Insertion Sort gives: %s\n" % lesorted)
print("runtime: %s seconds\n" % (time.time() - start_time))