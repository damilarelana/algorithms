
# animate()
#  -
# def animate(i: int, xx, stateDataLists, ax):
def animate(i: int, arrayPlot, stateDataLists):
    arrayPlot.set_height(stateDataLists[i])
    # arrayPlot = ax.bar(xx[0], stateDataLists[i], color='green', alpha=0.8)  # `[0]` helps to ensure that we plot only the first array due to how ax.bar handles 
    return arrayPlot



def setupPlotParams(listMinValue: int, listMaxValue: int, stateDataLists: list):
    # setup plotting area attributes
    #   - set_ylim refers to the the actual values in the array hence why it should be on the y-axis - in relation to a bar chart
    #       + `5` is used to pad the listMinValue and listMaxValue to animating those values easier to see
    #   - set_xlim refers to the index numbers of the array, which can be computed simply from the array length 
    #   - xLinspace is obtained from the global variable scope
    #   - yLinspace is calculated here using attributes of the already sorted list e.g. listMaxValue

    yLinspace = np.linspace(listMinValue, listMaxValue, inputListLength) # creates even space in y-axis for array element values
    xx, yy = np.meshgrid(xLinspace, yLinspace)  # create the mesh grid 

    # figsize = (6, 3)  # set figure size tuple i.e. canvas size (i.e. paper size: A4, Letter, wide-screen aspect ratio etc.)
    fig, ax = plt.subplots(figsize=(6, 3))
    # ax.set(xlim=(0, inputListLength-1), ylim=(listMinValue-5, listMaxValue+5))
    ax.set_xlim(0, inputListLength-1)  # handles the scaling of the axis
    ax.set_ylim(0, listMinValue-5, listMaxValue+5)

    ax.set_xlabel("Index")  # handles the title label for of x-axis
    ax.set_ylabel("Value")  # handles the title label for of y-axis

    ax.set_title(algorithmName)  # handles printing of the name of the overall plot at the top
    
    color='green' # color of each bar chart shape

    pdb.set_trace()

    # plot the first array data
    #   - note that `stateDataLists[0, :]` is acting like `yy` i.e. the height data to the barplot handler
    #   - hence why we later `animate` i.e. iterate of `yy` (i.e. stateDataLists[i, :] different indices) in the `animate()` function
    arrayPlot = ax.bar(xx[0], stateDataLists[0], color, alpha=0.8)  # `[0]` helps to ensure that we plot only the first array due to how ax.bar handles 
    
    return fig, arrayPlot  # return generated plot setup parameters as a tuple




def createAnimation(stateDataLists: list, listMinValue: int, listMaxValue: int, algorithmName: str, animationFormat: str):
    # setup the matplotlib's plot parameters
    fig, arrayPlot = setupPlotParams(listMinValue, listMaxValue, stateDataLists)

    # create animation
    #   - 'interval' talks about ms interval between frames
    #   - 'frames' required to help save the animation later
    #   - 'blit' ensures that only areas of the plot which have changed are re-drawn i.e. improves performance and smoothness
    #   - uses `fig` after setupPlotParams() is called
    #   - calls `animate()` [while using the `stateDataList` and `arrayPlot`] defined within the scope of `createAnimation`
    animation = FuncAnimation(fig, animate(arrayPlot, stateDataLists), interval=200, frames=inputListLength-1, blit=True)

    # show
    plt.draw()
    plt.show()

    # save animation
    #   - checks the animation format
    #   - uses anonymous function to simulate a switch statement
    #   - to save as `mp4` change `filename` assignment i.e. "filename = algorithm + '.mp4' "
    filename = algorithmName + animationFormat
    if animationFormat == "gif":
        animation.save(filename, writer='imagemagick')
    else:
        animation.save(filename)



import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 6*np.pi, 100)
y = np.sin(x)

# You probably won't need this if you're embedding things in a tkinter plot...
plt.ion()

fig = plt.figure()
ax = fig.add_subplot(111)
line1, = ax.plot(x, y, 'r-') # Returns a tuple of line objects, thus the comma

for phase in np.linspace(0, 10*np.pi, 500):
    line1.set_ydata(np.sin(x + phase))
    fig.canvas.draw()
    fig.canvas.flush_events()


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
        return inputList, mSPlotDataDict

    tempMergedList = [0]*inputListLength       # initialise List to hold sorted values during merging of sub-Lists
    inputListLowerIndex = 0  # initialize index value of the list's first element
    inputListUpperIndex = inputListLength - 1  # initialize the index value of the list's last element

    print("\nInitial inputListLowerIndex: {}  |  inputListUpperIndex: {}\n".format(inputListLowerIndex, inputListUpperIndex))

    sublistRecurser(inputList, tempMergedList, inputListLowerIndex, inputListUpperIndex, mSDictKey, mSPlotDataDict, inputListLength)


# sublistRecurser()
def sublistRecurser(inputList: list, tempMergedList: list, inputListLowerIndex: int, inputListUpperIndex: int,  mSDictKey: int, mSPlotDataDict: dict, inputListLength: int):
    # indexSplitter() this helps to ensure that we get the floor that `a//b` gives
    leftSublistStopIndex = indexSplitter(inputListLowerIndex, inputListUpperIndex)

    leftSublistStartIndex = inputListLowerIndex
    rightSublistStartIndex = leftSublistStopIndex + 1
    rightSublistStopIndex = [inputListUpperIndex][:][0]

    if leftSublistStartIndex >= rightSublistStopIndex:
        print("Breaking recursive loop as LeftSublistStartIndex:{} >= RightSublistStopIndex:{}".format(leftSublistStartIndex, rightSublistStopIndex))
        return
    else:
        sublistRecurser(inputList, tempMergedList, leftSublistStartIndex, leftSublistStopIndex, mSDictKey, mSPlotDataDict, inputListLength)                      # recursive call to sublistRecurser() by leftSubList
        sublistRecurser(inputList, tempMergedList, rightSublistStartIndex, rightSublistStopIndex, mSDictKey, mSPlotDataDict, inputListLength)                      # recursive call to sublistRecurser() by rightSubList
        sublistMerger(inputList, tempMergedList, leftSublistStartIndex, leftSublistStopIndex, rightSublistStartIndex, rightSublistStopIndex, mSDictKey, mSPlotDataDict, inputListLength)


# sublistMerger()
# - is called by sublistRecurser()
# - to handle list merging operations

def sublistMerger(inputList: list, tempMergedList: list, leftSublistStartIndex: int, leftSublistStopIndex: int, rightSublistStartIndex: int, rightSublistStopIndex: int, mSDictKey: int, mSPlotDataDict: dict, inputListLength: int):
    # Logic for splitting
    #   - leftSubList = inputList[leftSubListStartIndex:leftSublistStopIndex+1]
    #   - rightSubList = inputList[rightSublistStartIndex:rightSublistStopIndex+1]
    initialLeftSublistCounter = leftSublistStartIndex
    tempMergedListIndex = leftSublistStartIndex
    initialRightSublistCounter = rightSublistStartIndex

    pdb.set_trace()

    while initialLeftSublistCounter <= leftSublistStopIndex and initialRightSublistCounter <= rightSublistStopIndex:
        if inputList[initialLeftSublistCounter] > inputList[initialRightSublistCounter]:                   # test smaller element
            tempMergedList[tempMergedListIndex] = inputList[initialRightSublistCounter]           # add to end of tempMergeList
            initialRightSublistCounter += 1
        else:
            tempMergedList[tempMergedListIndex] = inputList[initialLeftSublistCounter]            # add to end of tempMergeList
            initialLeftSublistCounter += 1

        # increment temporary merged list counter AND stop the current state of the merged list inside the mSPlotDataDict
        tempMergedListIndex += 1
        # mSDictKey += 1  # increase dictionary index before it is used
        # getPlotData(tempMergedList[:], mSDictKey, mSPlotDataDict, inputListLength) # get state data      

    # handles when the left sublist still elements in it (which are inherently sorted - since sublistMerger() is recursively building from the bottom)
    while initialLeftSublistCounter <= leftSublistStopIndex:                                  # no elements to merge in rightSublist
        tempMergedList[tempMergedListIndex] = inputList[initialLeftSublistCounter]                  
        initialLeftSublistCounter += 1

        # increment temporary merged list counter AND stop the current state of the merged list inside the mSPlotDataDict
        tempMergedListIndex += 1
        # mSDictKey += 1  # increase dictionary index before it is used
        # getPlotData(tempMergedList[:], mSDictKey, mSPlotDataDict, inputListLength) # get state data
    
    while initialRightSublistCounter <= rightSublistStopIndex:                                  # no elements to merge in leftSublist
        tempMergedList[tempMergedListIndex] = inputList[initialRightSublistCounter]                
        initialRightSublistCounter += 1

        # increment temporary merged list counter AND stop the current state of the merged list inside the mSPlotDataDict
        tempMergedListIndex += 1
        # mSDictKey += 1  # increase dictionary index before it is used
        # getPlotData(tempMergedList[:], mSDictKey, mSPlotDataDict, inputListLength) # get state data

    # update stateData by
    #   - this is only useful if you are trying to plot current state data of the input list
    #   - this basically writes back the `portion` (i.e. starting from the left sublist index 0) of the inputlist that has been sorted
    #       + leftSublistStartIndex is always going to start from 0
    #       + rightSublistStopIndex is however not going to always be `inputListLength - 1`
    #       + this is because at `line 240` the recursion would always go down the leftSublist side stack first i.e.         
    #               - sublistRecurser(inputList, tempMergedList, leftSublistStartIndex, leftSublistStopIndex, mSDictKey, mSPlotDataDict, inputListLength)  # recursive call to sublistRecurser() by leftSubList
    #   - hence indirectly making the other sides of the input list to be some sort of state data
    #   - tempMergedList is also a stateData, the difference however is that it ALWAYS builds up from index 0, as if you are appending sorted items to a list
    #       + tempMergedList does not show how the sorting is being done in comparison to the existing state of the data
    for index in range(leftSublistStartIndex, rightSublistStopIndex+1):
        inputList[index] = tempMergedList[index]
    
    mSDictKey += 1  # increase dictionary index before it is used AND then use a slice of the whole `updated input List` as the stateData to be added to mSPlotDataDict
    getPlotData(inputList[:], mSDictKey, mSPlotDataDict, inputListLength) # get state data

    return tempMergedList, mSPlotDataDict

#
# indexDemarcation()
#   - gives the floor of the division between inputListUpperIndex and inputListLowerIndex (i.e. a // b )
#   - alternative is to give the ceiling
#   - we are instead going with floor so as to more easily control the startIndex for rightSubList 
#           + i.e. if splitIndex = 2 and hence the last index for the leftSubList
#           + then startIndex for rightSubList is splitIndex += 1
#   - def indexDemarcation(inputListLowerIndex: int, inputListUpperIndex: int):
#           numerator = inputListLowerIndex + inputListUpperIndex
#           denumerator = 2
#           splitIndex, quotient = divmod(numerator, denumerator)
#           adjustedSplitIndex = value + bool(quotient)
#           return adjustedSplitIndex
def indexSplitter(inputListLowerIndex: int, inputListUpperIndex: int):
    nuMerator = inputListLowerIndex + inputListUpperIndex
    deNumerator = 2
    splitIndex = nuMerator // deNumerator
    return splitIndex