import random
import time
import math
import copy
import secrets
import pdb
import numpy as np
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
plt.style.use('seaborn-darkgrid')
#
# Generate Random Unsorted List
#
listRangeStart = 0
listRangeStop = 2127
listRangeStep = 23


#
# listShuffler()
#  - helps to avoid the problem that random.shuffle tends to shuffle in place
#  - copy the inputList around sometimes means references [i.e. the copies] are not copied


def listShuffler(initialList: list):
    workingList = copy.deepcopy(initialList)  # deepcopy that random sample
    randomNumber = secrets.randbits(8192)     # generate random number for random.seed()
    random.seed(randomNumber)     # improve the randomizer by calling random.seed()
    random.shuffle(workingList)  # shuffle the copy of the random sample again just to be sure :)
    # shuffledList = random.sample(workingList, len(workingList))  # take a random sample of list [which returns a shuffled version]

    # return the now shuffled list
    return workingList


# set Animation Save format
animationFormat = "gif"


# create list
initialList = [x for x in range(listRangeStart, listRangeStop, listRangeStep)]  # Generate Random Unsorted List
inputList = listShuffler(initialList)
inputListLength = len(inputList)
if inputListLength > 20:
    printedSliceLength = 15
else:
    printedSliceLength = inputListLength

# create distinct copies of the now reshuffled list [so as to ensure objectivity in the sorting]
hBSInputList = copy.deepcopy(inputList[:])
eBSInputList = copy.deepcopy(inputList[:])
sSInputList = copy.deepcopy(inputList[:])
mSInputList = copy.deepcopy(inputList[:])
iSInputList = copy.deepcopy(inputList[:])

#
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("")
print("Comparing performance of 5 algorithms [ mergeSort + hybridBubbleSort + elegantBubbleSort + selectionSort + insertionSort]:")
print("  - using randomly generated data")
print("  - of an array of integer values")
print("  - with {} elements".format(inputListLength))
print("")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")


# hybridBubbleSort() is a combination of the two
# - it is an hybrid in the sense that it dynamically adjusts
# - by reducing the inputListLength, after each inner loop iteration
# - while still using a swap flag AND break point
# - it 10x-100x faster than bubbleSortElegant.py
# - sometimes marginally faster (or marginally slower) than kindaBubbleSort()


def hybridBubbleSort(inputList: list):

    # animation data initialize dict, with `index 0` being an empty list
    hBSDictKey = 0  # key to store the arrayState for each loop cycle
    hBSPlotDataDict = {  # represents the plot data to be consumed to aggregated the sorting plot data for later animation
        hBSDictKey: hBSInputList[:],  # initialize placeholder for the stored arrayState: where initial inputList is initial state
    }

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
            
            # passing a slice of `inputList` (i.e. inputList[:]) helps to dereference/decouple before usage by getPlotData()
            #   - to avoids scenarios where all dict values are reference to same sorted list
            #   - we could also use `tempList = inputList[:]` and then pass `tempList` to getPlotData(tempList ... )
            #   - this was not done for `space complexity performance reasons`
            #   - this passing/receiving of slice is implemented inside augmentList()
            #   - getPlotData() implements augmentList() to validate the inputted list
            #       + augmentList() helps to validate if the size of inputList[:] is dynamically changing i.e. as it occurs within mergeSort()
            hBSDictKey += 1  # increase dictionary index before it is used in getPlotData i.e. initial inputList is initial state
            getPlotData(inputList[:], hBSDictKey, hBSPlotDataDict, inputListLength)

        # break from loop if already sorted input and sorting completion
        if not(swapflag):
            break
        oCount += 1
        inputListLength -= 1  # decrement list length before next iteration, since previous largest value does not need to be involved in next iterations 
    return inputList, hBSPlotDataDict

# elegantBubbleSort() is an elegant implementation


def elegantBubbleSort(inputList: list):

    # animation data initialize dict, with `index 0` being an empty list
    eBSDictKey = 0  # key to store the arrayState for each loop cycle
    eBSPlotDataDict = {  # represents the plot data to be consumed to aggregated the sorting plot data for later animation
        eBSDictKey: eBSInputList[:],  # initialize placeholder for the stored arrayState: where initial inputList is initial state
    }

    inputListLength = len(inputList)
    oCount = 0  # initialize the outer counter i.e. which controls repetition after bubbling previous largest values
    while oCount < len(inputList):  # this does not use inputListLength, to ensure we test all elements for largeness
        iCount = 0   # initialize the inner counter i.e. to move one selected element through the list
        while iCount < (inputListLength - 1):
            if inputList[iCount] > inputList[iCount+1]:
                inputList[iCount], inputList[iCount+1] = inputList[iCount+1], inputList[iCount]
            iCount += 1

            # passing a slice of `inputList` (i.e. inputList[:]) helps to dereference/decouple before usage by getPlotData()
            #   - to avoids scenarios where all dict values are reference to same sorted list
            #   - we could also use `tempList = inputList[:]` and then pass `tempList` to getPlotData(tempList ... )
            #   - this was not done for `space complexity performance reasons`
            #   - this passing/receiving of slice is implemented inside augmentList()
            #   - getPlotData() implements augmentList() to validate the inputted list
            #       + augmentList() helps to validate if the size of inputList[:] is dynamically changing i.e. as it occurs within mergeSort()            
            eBSDictKey += 1  # increase dictionary index before it is used in getPlotData i.e. inputList is the initial state
            getPlotData(inputList[:], eBSDictKey, eBSPlotDataDict, inputListLength)

        oCount += 1  # increment outer loop i.e. number of times we have so far bubbled up the largest value
        inputListLength -= 1  # decrement list length before next iteration, since previous largest value does not need to be involved in next iterations 

    return inputList, eBSPlotDataDict  # returning a now sorted input List

# selectionSort()
# - works by:
#   + assume l[0] is minimum
#   + saves the index of l[0] into a temporary placeholder
#   + scans all remaining items i.e. the innerCount being always one index ahead of the outerCount
# - sorts in an ascending order
# - all this is happening in place
#   + we are just using `outcounter` to implement a virtual segregation of what is sorted and unsorted


def selectionSort(inputList):

    # animation data initialize dict, with `index 0` being an empty list
    sSDictKey = 0  # key to store the arrayState for each loop cycle
    sSPlotDataDict = {  # represents the plot data to be consumed to aggregated the sorting plot data for later animation
        sSDictKey: sSInputList[:],  # initialize placeholder for the stored arrayState: with inputList as initial state
    }

    inputListLength = len(inputList) 
    if inputListLength == 1:
        return inputList
    else:
        outerCount = 0                      # initialise outerloop counter
        minElement = outerCount             # assume first index "0" is temporary minimum (changes with each pass)
        while outerCount < inputListLength:       # using "for ... in ... range()" would give same result
            innerCount = outerCount + 1     # make (or reset) innerCount to current "outerCount + 1"
            while innerCount < inputListLength:   # scanning by looping over all remaining items to test new minimum
                if inputList[innerCount] < inputList[minElement]:  # if any of the items if less than current minimum
                    minElement = innerCount  # swaps out the index of the old with the new i.e. create new temporary minimum for remaining unsorted set
                innerCount += 1             # increase inner counter i.e. reducing unsorted list of items
            inputList[outerCount], inputList[minElement] = inputList[minElement], inputList[outerCount]  # confirm new minimum by swapping [temporary outerCount index with new minimum's index]

            # passing a slice of `inputList` (i.e. inputList[:]) helps to dereference/decouple before usage by getPlotData()
            #   - to avoids scenarios where all dict values are reference to same sorted list
            #   - we could also use `tempList = inputList[:]` and then pass `tempList` to getPlotData(tempList ... )
            #   - this was not done for `space complexity performance reasons`
            #   - this passing/receiving of slice is implemented inside augmentList()
            #   - getPlotData() implements augmentList() to validate the inputted list
            #       + augmentList() helps to validate if the size of inputList[:] is dynamically changing i.e. as it occurs within mergeSort()
            sSDictKey += 1  # increase dictionary index before it is used in getPlotData [since inputList is already at index 0]
            getPlotData(inputList[:], sSDictKey, sSPlotDataDict, inputListLength)

            outerCount += 1                 # increase outer counter i.e. expanding the sorted set
            minElement = outerCount         # reset new temporary minimum index e.g. if initial was index `0`, it would now be `1` 
            if outerCount == inputListLength - 1:  # i.e. only one unsorted element remains, break outer loop
                break
            # note that we CANNOT use the optimization (inputListLength -= 1) since we are shifting values/index around 
            # as such the last value after every iteration can still need to be touched
            # this is one difference with BubbleSort() where the last index can be removed from dataset after every loop
        return inputList, sSPlotDataDict


# mergeSort()
# - works by:
#   + splitting the iteratively splitting the original lists into sublists using sublistRecurser
#   + until you have sublists that are not more than 1 element long i.e. inherently sorted
#   + iteratively compares and determines whether to `append sublist1` to `sublist2` OR `append sublist2 to sublist1`
# - this is NOT happening in place
#   + hence there is a space penalty for the algorithm
# - returns the final sorted list via sublistMerge()

def mergeSort(inputList):
    # animation data initialize dict, with `index 0` being an empty list
    # - this is initialized at the global level since mergeSort is recursive
    #   + recursion means that stateData would be brought back to zero state after each recursive call
    mSDictKey = 0  # key to store the arrayState for each loop cycle
    mSPlotDataDict = {  # represents the plot data to be consumed to aggregated the sorting plot data for later animation
        mSDictKey: inputList[:],  # initialize placeholder for the stored arrayState: where initial inputList is initial state (i.e. at index 0)
    }
    inputListLength = len(inputList)
    if inputListLength < 2:                                           # using "<2" instead of "==", handles when inputList=[] or [1] i.e. either a null or single element list
        # return the original list without changing stateData since it is not necessary [as there is nothing to sort and hence no data to animate]
        return inputList

    tempMergedList = [0]*inputListLength       # initialise List to hold sorted values during merging of sub-Lists
    inputListLowerIndex = 0  # initialize index value of the list's first element
    inputListUpperIndex = inputListLength - 1  # initialize the index value of the list's last element

    return sublistRecurser(inputList, tempMergedList, inputListLowerIndex, inputListUpperIndex, mSDictKey, mSPlotDataDict, inputListLength)


# sublistRecurser()
def sublistRecurser(inputList: list, tempMergedList: list, inputListLowerIndex: int, inputListUpperIndex: int,  mSDictKey: int, mSPlotDataDict: dict, inputListLength: int):
    # Logic for splitting
    #   - leftSubList = inputList[inputListLowerIndex:splitIndex+1]
    #   - rightSubList = inputList[splitIndex:inputListUpperIndex+1]

    # 'inputListLowerIndex != 0' since it can actually be `inputListIndex = splitIndex` when the rightSubList is being handled
    splitIndex = (inputListLowerIndex + (inputListUpperIndex + 1))//2  # "//" helps ensure that only the floor (i.e. integer value) is returned

    # using "<" instead of "==" to avoid infinite recursion
    #   - 'when splitIndex == 2' THEN we had 1 split left i.e. if [0:1] and[1:2]
    #   - once that split is done then there is nothing to split any more
    #   - since next splitIndex is now `(0 + 1)//2` i.e. `0` 
    #       + which means that 'new inputListUpperIndex' == 'inputListLowerIndex' i.e. 0 == 0, is when we should breakout of recursion
    #       + using 'inputListLowerIndex >= inputListUpperIndex' helps us to adjust for when `inputListIndex = splitIndex` i.e. rightSubList is being handled
    if inputListLowerIndex >= inputListUpperIndex:
        return sublistMerger(inputList, tempMergedList, inputListLowerIndex, inputListUpperIndex, splitIndex, mSDictKey, mSPlotDataDict, inputListLength)
    else:  # continue the recursion
        sublistRecurser(inputList, tempMergedList, inputListLowerIndex, splitIndex, mSDictKey, mSPlotDataDict, inputListLength)                      # recursive call to sublistRecurser() by tempListOne
        sublistRecurser(inputList, tempMergedList, splitIndex, inputListUpperIndex, mSDictKey, mSPlotDataDict, inputListLength)                      # recursive call to sublistRecurser() by tempListTwo
        return sublistMerger(inputList, tempMergedList, inputListLowerIndex, inputListUpperIndex, splitIndex, mSDictKey, mSPlotDataDict, inputListLength)


# sublistMerger()
# - is called by sublistRecurser()
# - to handle list merging operations

def sublistMerger(inputList: list, tempMergedList: list, inputListLowerIndex: int, inputListUpperIndex: int, splitIndex: int, mSDictKey: int, mSPlotDataDict: dict, inputListLength: int):
    # Logic for splitting
    #   - leftSubList = inputList[inputListLowerIndex:splitIndex+1]
    #   - rightSubList = inputList[splitIndex:inputListUpperIndex+1]

    leftSublistIndex = inputListLowerIndex
    rightSublistIndex = splitIndex
    tempMergedListIndex = [inputListLowerIndex][:][0]  # used here to create an independent copy (that can increment without changing inputListLowerIndex) without using copy.deepcopy()

    while leftSublistIndex <= splitIndex and rightSublistIndex <= inputListUpperIndex:      
        if inputList[leftSublistIndex] > inputList[rightSublistIndex]:                   # test smaller element
            tempMergedList[tempMergedListIndex] = inputList[rightSublistIndex]                     # add to end of tempMergeList
            rightSublistIndex += 1
            tempMergedListIndex += 1
        else:
            tempMergedList[tempMergedListIndex] = inputList[leftSublistIndex]                           # add to end of tempMergeList
            leftSublistIndex += 1
            tempMergedListIndex += 1
    while leftSublistIndex <= splitIndex:                                  # no elements to merge in rightSublist
        tempMergedList[tempMergedListIndex] = inputList[leftSublistIndex]                    
        leftSublistIndex += 1
        tempMergedListIndex += 1
    while rightSublistIndex <= inputListUpperIndex:                                  # no elements to merge in leftSublist
        tempMergedList[tempMergedListIndex] = inputList[rightSublistIndex]                
        rightSublistIndex += 1
        tempMergedListIndex += 1

    # update stateData by
    #   - note that `inputListLowerIndex` is not always `0` 
    #   - using the recently updated tempMergeList values between indices: `inputLowerIndex <> inputListUpperIndex`
    #   - to change the all the values at the index of inputList to their correct values
    #   - since we are building upwards from `pre-sorted` single element lists THEN would be able to over-writing any unsorted elements
    #       + i.e. the data (where a > c > b) we are dealing with means:
    #           - if the leftSubList = [a, b] where `inputList[0] = a` and `inputList[1]`
    #           - if the rightSubList = [c] where `inputList[2] = c`
    #       + thus tempMergedList would have them in the correct order [b, c, a]
    #       + then the ONLY indices we are dealing with are those of [a, b] and [c]
    #       + so the location of the values changes but the values themselves are NOT over-written
    for index in range(inputListLowerIndex, inputListUpperIndex+1):
        inputList[index] = tempMergedList[index]
    
    mSDictKey += 1  # increase dictionary index before it is used
    getPlotData(inputList[:], mSDictKey, mSPlotDataDict, inputListLength) # get state data      

    return tempMergedList


# insertionSort()
#


def insertionSort(inputList):
    # animation data initialize dict, with `index 0` being an empty list
    iSDictKey = 0  # key to store the arrayState for each loop cycle
    iSPlotDataDict = {  # represents the plot data to be consumed to aggregated the sorting plot data for later animation
        iSDictKey: iSInputList[:],  # initialize placeholder for the stored arrayState: where initial input list initial state (at index 0)
    }

    # array sorting logic 
    inputListLength = len(inputList)
    if inputListLength == 1:
        return inputList    # no point wasting CPU cycle to sort one item
    else:
        # we assume that element at index `0` i.e. ocount = 0, is already sorted, hence why the unsorted starts at ocount = 1
        ocount = 1                       # initialising unsorted list index to the first one to be removed from unsorted [we ]
        while ocount < inputListLength:        # handles if len(inputList)=1, unsorted loop index
            icount = ocount              # re-initialising sorted list's max index to allow countdown
            while icount > 0:            # handles inner loop i.e. the `sorted list loop`. greater than zero 
                                         # helps to ensure that when you `bring` a new element (from unsorted) to test/loop against `the sorted
                                         # it helps to ensure that the looping down does not go beyond `index 0` within the sorted
                if inputList[icount-1] > inputList[icount]:           # this already carters for assuming list[0] is sorted
                    inputList[icount - 1], inputList[icount] = inputList[icount], inputList[icount-1]
                icount -= 1 # this is different to bubbleSort i.e. where there is an increment. Here we are decreasing the unsorted set

                # passing a slice of `inputList` (i.e. inputList[:]) helps to dereference/decouple before usage by getPlotData()
                #   - to avoids scenarios where all dict values are reference to same sorted list
                #   - we could also use `tempList = inputList[:]` and then pass `tempList` to getPlotData(tempList ... )
                #   - this was not done for `space complexity performance reasons`
                #   - this passing/receiving of slice is implemented inside augmentList()
                #   - getPlotData() implements augmentList() to validate the inputted list
                #       + augmentList() helps to validate if the size of inputList[:] is dynamically changing i.e. as it occurs within mergeSort()
                iSDictKey += 1  # increase dictionary index before it is used getPlotData e.g. since inputList is already at index 0
                getPlotData(inputList[:], iSDictKey, iSPlotDataDict, inputListLength)  # note that isPlotDataDict is being updated in place within scope of `insertionSort()`
            ocount += 1  # here we are increasing the sorted set boundaries [which weirdly also acts like the next `first element of the now shrinking unsorted set`]
        return inputList, iSPlotDataDict

#
# augmentList()
#   - is mostly applicable to algorithms that breakdown the list before sorting e.g. MergeSort()
#   - it takes a full slice `inputList[:]` of current list as argument (i.e. currentList = inputList[:]) so as to capture current state
#   - it gets length of current list currentListLength = len(currentList)
#   - it takes in length of input list i.e. inputListLength
#   - checks if there has been a decomposition i.e. if inputListLength != currentListLength
#       + if false, it simply returns `currentList` to the callback function
#       + if true, it pads the currentList with `0` at the end so as to make the `lists` inside `stateDataList` to be of same length i.e.
#               - calculates `padLength = looRange - currentListLength`
#               - creates `padList = [0]*padLength`
#               - pads `currentList` by the pythonic approach of `currentList += padList`
#               - returns the padded list
#


def augmentList(currentList: list, inputListLength: list):
    currentListLength = len(currentList)
    if currentListLength != inputListLength:
        padLength = inputListLength - currentListLength
        padList = [0]*padLength
        currentList += padList
    return currentList


# getPlotData()
#  - takes in an array state while sorting
#  - takes in plot data dictionary (to be populated)
#  - takes in the initialized dictionary key dictKey
#  - takes in the initialized stateData list
#  - takes in the initialized plotDataDict dict
#  - takes in the original input list length i.e. inputListLength
#  - saves the stateData (initial, current and future) into the dictionary, with specific key value
#  - increment the dictionary key value
#  - repeat the saving process
#  - does not return anything as it is working on the array and dictionary in-place
#  - dictionary is being used so as to obtain:
#   + a 2-D array once we extract the `list of lists` from the dictionary 
#   + as required by the animation approach [https://brushingupscience.com/2016/06/21/matplotlib-animations-the-easy-way/]
#   + `list of lists` approach is also being used to improved performance:
#        - by avoiding the use of zip() to extract and unzip


def getPlotData(arrayWhileSorting, dictKey: int, plotDataDict: dict, inputListLength: int):
    augmentedList = augmentList(arrayWhileSorting, inputListLength)
    plotDataDict.update({dictKey: augmentedList})  # append arrayWhileSorting to dict, at the end of the dict
    # plotDataDict[dictKey] = arrayWhileSorting  # append arrayWhileSorting to dict, at the end of the dict

#
# parsePlotData()
# - takes in the returned plotDataDict (via getPlotData via sort functions [e.g. insertionSort()])
# - parses it through a `list comprehension` that references plotDataDict.values()
#   + to extract the [indexTuple, valueTuple] at each dictionary key


def parsePlotData(plotDataDict: dict):
    stateDataLists = [values for values in plotDataDict.values()]
    return stateDataLists  # returns the list of lists required by animation
#
# createAnimation()
#   - takes in the stateDataLists
#   - takes in listMinValue
#   - takes in listMaxValue
#   - takes in the algorithm's name e.g. "insertion Sort" etc.
#   - takes in the animation file format e.g. "mp4" or "gif"
#   - uses the parameters to create an animation of the sorting


def createAnimation(stateDataLists: list, listMinValue: int, listMaxValue: int, algorithmName: str, animationFormat: str, speedFlag):

    # determine length of each stateData list (in the list of list) meant to be animated
    try:
        inputListLength = len(stateDataLists[0])
    except ValueError:
        raise Exception("Unable to determine length of stateData list (in the `list of lists`)")


    # setup the mesh grid
    #   - xLinspace and yLinspace input to np.meshgrid()
    #   - xx and yy output indicating the width and height of the mesh grid in terms of array
    #   - initializing the meshGrid at the beginning would not be a problem even if stateData length changes during sorting
    #       + this is because the stateData length can only reduce and not increase
    #       + thus the meshGrid would still be big enough to handle rendering on it by smaller data set
    xLinspace = np.linspace(0, inputListLength-1, inputListLength)  # creates i.e. evenly spaced stuff in x-axis that matches the array index spacing
    yLinspace = np.linspace(listMinValue, listMaxValue, inputListLength) # creates even space in y-axis for array element values
    xx, yy = np.meshgrid(xLinspace, yLinspace)  # create the mesh grid 

    # setup the matplotlib's plot parameters
    fig, ax = setupPlotParams(listMinValue, listMaxValue, inputListLength)
    fig.show()
    # fig.canvas.draw()

    # create animation
    #   - 'interval' talks about ms interval between frames
    #   - 'frames' required to help save the animation later
    #   - 'blit' ensures that only areas of the plot which have changed are re-drawn i.e. improves performance and smoothness
    #   - uses `fig` after setupPlotParams() is called
    #   - calls `animate()` [while using the `stateDataList` and `arrayPlot`] defined within the scope of `createAnimation`

    # numEvents
    #   - refers to the number of stateData that exists in the stateDataLists
    #   - i.e. how many lists do you have within the `list of lists`
    #   - where each `list` represents an event
    numEvents = len(stateDataLists)

    # plot the first array data
    #   - note that `stateDataLists[0, :]` is acting like `yy` i.e. the height data to the barplot handler
    #   - hence why we later `animate` i.e. iterate of `yy` (i.e. stateDataLists[i, :] different indices) in the `animate()` function
    #   - assumption is that:
    #       + length of xx[i] does not change AND length of stateDataList[i] also does not change
    #       + hence this breaks with mergeSort() since stateDataList[i] changes during mergeSort()
    #       + two solutions:
    #           - Option I: dynamically alter length of `xx[0]` i.e. recomputing np.meshgrid everytime [with new Linspace], while stateData[i] changes
    #           - Option II: `xx[0]` remains the same but stateData[i] is dynamically padded (at the) with `zeros` to simulate absence of plot data [as mergeSort splits the data down to only one index]
    #       + Option is more DRY and SOLID i.e. it avoids to many changes to the animation convas
    #           - only the plotting data is dynamically changing
    arrayPlot = plt.bar(xx[0], stateDataLists[0], 0.8, None, color='green', edgecolor='snow', alpha=0.7)  # helps to ensure that we plot only the first array due to how ax.bar handles 
    
    backgroundRender = fig.canvas.copy_from_bbox(ax.bbox)  #save background be fore animating ... to improve performance
    animStartTime = time.time()
    animate(xx[0], ax, arrayPlot, stateDataLists, fig, numEvents, backgroundRender, speedFlag)
    print('animation rendered in {:.2f}s'.format(time.time()-animStartTime))  # print the fps to have 2 decimal places

    # save animation
    #   - checks the animation format
    #   - uses anonymous function to simulate a switch statement
    #   - to save as `mp4` change `filename` assignment i.e. "filename = algorithm + '.mp4' "
    filename = algorithmName + animationFormat
    # if animationFormat == "gif":
    #     animation.save(filename, writer='imagemagick')
    # else:
    #     animation.save(filename)


# animate()
def animate(x, ax, arrayPlot, stateDataLists, fig, numEvents, backgroundRender, speedFlag):
    for i in range(numEvents):
        fig.canvas.restore_region(backgroundRender) # restore the cached/rendered background (i.e. apart from the bars themselves)
        arrayPlot.remove() # remove the previous bar chart rendering, so as to avoid ghosting

        if hasattr(arrayPlot, 'set_height'):
            arrayPlot.set_height(stateDataLists[i])  # faster option but does not always work due to matplotlib issues
        else:
            arrayPlot = plt.bar(x, stateDataLists[i], 0.8, None, color='green', edgecolor='snow', alpha=0.7)  # brute force creation of new bar container
        if speedFlag is True:
            time.sleep(0.5)  # meant to slow down the animation plot of mergesort() data
            fig.canvas.draw()
            fig.canvas.blit(ax.bbox)
            fig.canvas.flush_events()
        else:
            fig.canvas.draw()
            fig.canvas.blit(ax.bbox)
            fig.canvas.flush_events()

# setupPlotParameters()
# - sets up the required Matplotlib parameters
def setupPlotParams(listMinValue: int, listMaxValue: int, inputListLength: int):

    # plt.ion()
    # setup plotting area attributes
    #   - set_ylim refers to the the actual values in the array hence why it should be on the y-axis - in relation to a bar chart
    #       + `5` is used to pad the listMinValue and listMaxValue to animating those values easier to see
    #   - set_xlim refers to the index numbers of the array, which can be computed simply from the array length 
    #   - xLinspace is obtained from the global variable scope
    #   - yLinspace is calculated here using attributes of the already sorted list e.g. listMaxValue
    # figsize = (6, 3)  # set figure size tuple i.e. canvas size (i.e. paper size: A4, Letter, wide-screen aspect ratio etc.)
    # ax.set(xlim=(0, inputListLength), ylim=(listMinValue-5, listMaxValue+5))
    #   - note that xlim(0, inputListLength) was choosen as such to ensure that last element is visible during the plot
    #   - it would have been invisible, if xlim(0, inputListLength) was used instead

    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(1,1,1, xlim = (-1, inputListLength), ylim = (listMinValue-20, listMaxValue+20), xlabel = "Index", ylabel = "Value", title = algorithmName, alpha=0.6)
    
    return fig, ax



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
# selectionSort()
#
# timed runtime
unsortedSSInputList = mSInputList
sSStartTime = time.time()
selectionSorted, sSPlotData = selectionSort(sSInputList)
sSStopTime = time.time()
print("Selection Sort gives first {} values as: {}".format(printedSliceLength, selectionSorted[:printedSliceLength+1]))
print("runtime: %f seconds" % (sSStopTime - sSStartTime))
print("input's first {} values: {}".format(printedSliceLength, unsortedSSInputList[:printedSliceLength+1]))
# animation creation
algorithmName = selectionSort.__name__  # get the function name as a string
sSListMinValue = selectionSorted[0]
sSListMaxValue = selectionSorted[inputListLength - 1]
sSParsedPlotData = parsePlotData(sSPlotData)  # converts the plotdata from a dict into a list
createAnimation(sSParsedPlotData, sSListMinValue, sSListMaxValue, algorithmName, animationFormat, False)
print("================================")

#
# mergeSort()
#
# timed runtime
unsortedMSInputList = mSInputList
mSStartTime = time.time()
mergesorted = mergeSort(mSInputList)
mSStopTime = time.time()
print("\nMerge Sort gives first {} elements as: {}".format(printedSliceLength, mergesorted[:printedSliceLength+1]))
print("runtime: %f seconds" % (mSStopTime - mSStartTime))
print("input's first {} values: {}".format(printedSliceLength, unsortedMSInputList[:printedSliceLength+1]))
# animation creation
algorithmName = mergeSort.__name__  # get the function name as a string
mSListMinValue = mergesorted[0]
mSListMaxValue = mergesorted[inputListLength - 1]
mSParsedPlotData = parsePlotData(mSPlotDataDict)  # converts the plotdata from a dict into a list [notice that `mSPlotDataDict` is a global variable in this case since mergeSort is recursive]
createAnimation(mSParsedPlotData, mSListMinValue, mSListMaxValue, algorithmName, animationFormat, True)
print("================================")

#
# hybridBubbleSort()
#
# timed runtime
unsortedHBSInputList = mSInputList
hBSStartTime = time.time()
hybridBubblesorted, hBSPlotData  = hybridBubbleSort(hBSInputList)
hBSStopTime = time.time()
print("\nHybrid Bubble Sort gives first {} elements as: {}".format(printedSliceLength, hybridBubblesorted[:printedSliceLength+1]))
print("runtime: %f seconds" % (hBSStopTime - hBSStartTime))
print("input's first {} values: {}".format(printedSliceLength, unsortedHBSInputList[:printedSliceLength+1]))
# animation creation
algorithmName = hybridBubbleSort.__name__  # get the function name as a string
hBSListMinValue = hybridBubblesorted[0]
hBSListMaxValue = hybridBubblesorted[inputListLength - 1]
hBParsedPlotData = parsePlotData(hBSPlotData)  # converts the plotdata from a dict into a list
createAnimation(hBParsedPlotData, hBSListMinValue, hBSListMaxValue, algorithmName, animationFormat, False)
print("================================")

#
# elegantBubbleSort()
#
# timed runtime
unsortedEBSInputList = mSInputList
eBSStartTime = time.time()
elegantBubblesorted, eBSPlotData = elegantBubbleSort(eBSInputList)
eBSStopTime = time.time()
print("\nElegant Bubble Sort gives first {} elements as: {}".format(printedSliceLength, elegantBubblesorted[:printedSliceLength+1]))
print("runtime: %f seconds" % (eBSStopTime - eBSStartTime))
print("input's first {} values: {}".format(printedSliceLength, unsortedEBSInputList[:printedSliceLength+1]))
# animation creation
algorithmName = elegantBubbleSort.__name__  # get the function name as a string
eBSListMinValue = elegantBubblesorted[0]
eBSListMaxValue = elegantBubblesorted[inputListLength - 1]
eBParsedPlotData = parsePlotData(eBSPlotData)  # converts the plotdata from a dict into a list
createAnimation(eBParsedPlotData, eBSListMinValue, eBSListMaxValue, algorithmName, animationFormat, False)
print("================================")

#
# insertionSort()
#
# timed runtime
unsortedISInputList = mSInputList
iSStartTime = time.time()
insertionsorted, iSPlotData = insertionSort(iSInputList)
iSStopTime = time.time()
print("\nInsertion Sort gives first {} elements as: {}".format(printedSliceLength, insertionsorted[:printedSliceLength+1]))
print("runtime: %f seconds" % (iSStopTime - iSStartTime))
print("input's first {} values: {}".format(printedSliceLength, unsortedISInputList[:printedSliceLength+1]))
# animation creation
algorithmName = insertionSort.__name__  # get the function name as a string
iSListMinValue = insertionsorted[0]
iSListMaxValue = insertionsorted[inputListLength - 1]
iSParsedPlotData = parsePlotData(iSPlotData)  # converts the plotdata from a dict into a list
createAnimation(iSParsedPlotData, iSListMinValue, iSListMaxValue, algorithmName, animationFormat, False)
print("================================")

#
# # Check if both sorted list are equivalent
# #
sShBS = checkOrderedListEquivalence(hybridBubblesorted, selectionSorted)
hBSmS = checkOrderedListEquivalence(hybridBubblesorted, mergesorted)
hBSiS = checkOrderedListEquivalence(hybridBubblesorted, insertionsorted)
hBSeBS = checkOrderedListEquivalence(hybridBubblesorted, elegantBubblesorted)
if sShBS and hBSmS and hBSiS and hBSeBS:
    print("\nAll algorithms give the same sorted list")
else:
    print("\nAll algorithms did NOT give the same sorted list")
