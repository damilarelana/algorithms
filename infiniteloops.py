#import necessary modules
import random
import time

# Generate Random List
#
rlist = [x for x in range(0,128976453,8)]
random.shuffle(rlist)
print("\nGiven a random unsorted list with: %s elements\n" % len(rlist))

#define infiniteloop algorithm
def infiniteloopalgo(rlist):
    #start infinite loop time counter
    start_time = time.time()
    ilcount = 0
    while True:
        # break from loop if number found   
        if rlist[ilcount] == 4096:
            stop_time = time.time()
            break
        ilcount += 1
    time_estimate = stop_time - start_time
    return time_estimate,ilcount
    
#define whileloop algorithm
def whileloopalgo(rlist):
    #start infinite loop time counter
    start_time = time.time()
    wlcount = 0
    while rlist[wlcount] != 4096:
        wlcount += 1
    stop_time = time.time()
    time_estimate = stop_time - start_time
    return time_estimate, wlcount

# call and print infiniteloop algorithm
temp = infiniteloopalgo(rlist)
iflooptime = temp[0]
ifloopcount = temp[1]
print("InfiniteLoop algorithm found number 4096 after %f seconds and %d loops \n" % (iflooptime, ifloopcount))

#call and print while loop algorithm
temp = whileloopalgo(rlist)
wlooptime = temp[0]
wloopcount = temp[1]
print("WhileLoop algorithm found number 4096 after %f seconds and %d loops \n" % (wlooptime, wloopcount))