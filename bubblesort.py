import random
import time
#
# Generate Random Unsorted List
#
rlist = [x for x in range(0, 12276, 96)]
random.shuffle(rlist)
print("\nGiven random unsorted list (%s elements): \n%s\n" % (len(rlist), rlist))
#
#start time counter
#
start_time = time.time()
def bubblesort(rlist):
    ocount = 0
    while ocount < len(rlist):
        # handles already sorted input and sorting completion
        swapflag = False
        icount = 0
        while icount < (len(rlist)-1):
            if rlist[icount] > rlist[icount+1]:
                temp = rlist[icount+1]
                rlist[icount+1] = rlist[icount]
                rlist[icount] = temp
                swapflag = True
            icount += 1
        # break from loop if already sorted input and sorting completion
        if not(swapflag):
            break	
        ocount += 1
    return rlist
bubblesorted = bubblesort(rlist)
print("Bubble Sort gives: %s\n" % bubblesorted)
print("runtime: %s seconds\n" % (time.time() - start_time))