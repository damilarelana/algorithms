import time
import algorithms.createLinkedList as c


def addIntegerLinkedList(firstInteger: c.LinkedList, secondInteger: c.LinkedList):

    newLinkedList = c.LinkedList() # default head value is None
    lastNode = c.Node() # default data argument is None
    carryValue = 0 # value carried over when adding two other numbers e.g. 9 + 8 = 17 - which in reality was 7 and 1 carried to the left

    # check if list is empty and exit accordingly
    # return the empty list
    if ((not testList) is True) or (len(testList) == 0) or (testList == None):
        return testList

    newList = list() # initialize a new array
    newList.append( Interval( # start pre-populating new array with a new first pair as if it is first correct state 
        getattr(testList[0], 'start'), # extract start value of first interval and pass it here to create a new interval for newArray
        getattr(testList[0], 'end') # extract end value of first interval and pass it here to create a new interval for newArray
    ))

    # start iterating over the remaining intervals object in testList
    for i in range(1, len(testList)):
        # test the intervals within newList compared to the 
        lastIndexNewList = len(newList) - 1 # the lastIndex of the newList is constantly changing
        if getattr(newList[lastIndexNewList],'end') >= getattr(testList[i],'start'): # if endtimestamp of current last interval (of newList) is greater than starttimestamp current test interval of test List, then there is an overlap
            setattr(newList[lastIndexNewList], 'end', max(testList[i].end, newList[lastIndexNewList].end)), # since there is an overlap, then choose largest endtimestamp (between current last interval [of newList] and current test interval of testList)
        else: # if there is no overlap, then just append the current test interval object to the newlist
            newList.append( Interval( 
                getattr(testList[i], 'start'),
                getattr(testList[i], 'end')
            ))
    return newList # return the now populated newList
#
# printListOfObjects()
def printListOfObjects(listOfIntervalObjects: list):
    for intervalObject in listOfIntervalObjects:
        print("[" + str(intervalObject.start) + ", " + str(intervalObject.end) + "]", end=" ") # 'end=" " is used to replace the default \n that comes with print()'
    return
# main()

def main():

    # initialize test intervals tInterval
    tIntervals = [Interval(1, 5), Interval(3, 1), Interval(4,6), Interval(6,8), Interval(10,12), Interval(11,15)] # defines a list of tInterval objects

    start_time = time.time()
    newMergedList = mergeIntervals(tIntervals)
    printListOfObjects(newMergedList)
    print("\nTime: {} seconds".format((time.time() - start_time)))


if __name__ == "__main__":
    main()
