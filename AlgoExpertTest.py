import time


def threeNumberSum(tIA: list, tIV: int):
    intermediateListIndex = 1  # index to obtain smaller/smallest intermediate list
    keyDict = 0  # key to store the matching triplet in a dictionary

    resultTriplet = list()  # initialize placeholder for matched triplets

    # initialize dict, with `index 0` being an empty list
    # - if subsequent pairs are found, `index 0` would be overwritten
    # - if not pairs are found, then we still have our `empty List []` as first value
    resultDict = {
        keyDict: resultTriplet,
    }

    # loop array elements to check if they sum up to `tIV`
    # - a single listIndex can be used if you think of `tIV`, `intermediateList` and `innerList` as subsets of each other
    #   + where the length is decreasing 1 each time you go down a loop
    #   + since you have excluded the test element `from previous loop`

    for t in tIA:
        intermediatetIV = tIV - t
        intermediateList = tIA[intermediateListIndex:]
        # print("Intermediate List : {}".format(intermediateList))
        innerListIndex = 1  # reset here since the new intermediateList also resets to `index 0`, hence needs a new innerList
        for i in intermediateList:
            testDiff = intermediatetIV - i
            innerList = intermediateList[innerListIndex:]
            # print("Inner List : {}".format(innerList))
            for j in innerList:
                if j == testDiff:
                    print("... matching triplets [{0}, {1}, {2}] found!".format(t, i, j))
                    resultTriplet = [t, i, j]  # current matching triplet is now identified 
                    resultTriplet = bubbleSort(resultTriplet)  # sort matching triplet
                    resultDict[keyDict] = resultTriplet  # append to dict
                    keyDict += 1  # increase dictionary index
            innerListIndex += 1  # incremented here to shrink innerList at next iteration with same intermediateList
        intermediateListIndex += 1  # increment this so as to shrink the intermediate list at next iteration [with same ]

    # constructor a 2-dimensional array using the dictionary values
    two2DArray = build2DArray(resultDict)

    # return the 2-d array
    return two2DArray

		
# define bubbleSort()
# - takes in a input list
# - sorts it in ascending order
# - returns a now sorted input list


def bubbleSort(inputList: list):
    oCount = 0  # outer counter initialization
    while oCount < len(inputList):
        # handles already sorted input and sorting completion
        swapflag = False
        iCount = 0  # inner counter initialization
        while iCount < (len(inputList)-1):
            if inputList[iCount] > inputList[iCount+1]:  # this sorts in ascending order
                inputList[iCount], inputList[iCount+1] = inputList[iCount+1], inputList[iCount]
                swapflag = True
            iCount += 1
        # break from loop if already sorted input and sorting completion
        if not(swapflag):
            break
        oCount += 1
    return inputList


# define build2DArray()
# - takes in a dictionary as argument
# - assumes each dict values is an already sorted integer array `list`
# - assumes the maximum value for each `list` would be element at `list[index len(list)-1]`
# - creates a new list i.e. 2DArray with elements consisting of the previous sorted lists
# - uses these maximum values to sort the new list
# - used the .sort(key=lambda ...) to do the actual sorting 
# - return the now sorted 2DArray


def build2DArray(resultDict: dict):

    # extract the `list` or `already sorted lists`
    two2DArray = list()
    for v in resultDict.values():
        if bool(v) is True:
            two2DArray.append(v)

    # sort the `list` of `already sorted lists`
    two2DArray.sort(key=lambda x: x[0])  # sort by last element in each list

    return two2DArray


def main():
    start_time = time.time()
    tIV = 7
    tIA = [1, 2, 3]
    twoDArray = threeNumberSum(tIA, tIV)
    print("The 2-dimensional array of matching triplets are: {0}".format(twoDArray))
    print("Time: {} seconds".format((time.time() - start_time)))


if __name__ == "__main__":
    main()
