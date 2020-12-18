def computeTwoNumSum(tIA: list, tIV: int, tIndex: int):
    startIndex = copy.deepcopy(tIndex)  # deepcopy that random sampletIndex  # index to obtain smaller/smaller innerList as we loop
    lastIndex =  len(tIA) - 1
    resultPair = tuple()  # initialize tuple placeholder for matched pairs
    returnedPair = tuple()
    newReturnedPair = tuple()
    failSafeReturnedPair = tuple() 

    # loop array elements to check if they sum up to `tIV`
    # first we divide and conquer by searching in slice tIA[startIndex:lastIndex+1]
    #   - assuming that startIndex is NOT 0 i.e. startIndex > 0
    newLastIndex = copy.deepcopy(tIndex)
    if startIndex < lastIndex and startIndex != 0:
        returnedPair = getTwoSumPairs(tIA, tIV, startIndex, lastIndex, resultPair)
        pdb.set_trace()
        if not returnedPair is False: # meaning a pair was found so 'not returnedPair' is 'not True' i.e. False
            return returnedPair
    
    if not returnedPair: # only runs if search with previous slice is still empty
        # this loop solves for when the search does not find the pairs in the initial slice tIA[startIndex:lastIndex+1]
        #   - we then test the remaining slice i.e. tIA[0:startIndex] (note we can also overlap the slices by using the slice tIA[0:startIndex + 1])
        #   - where newLastIndex = startIndex - 1 or newLastIndex = startIndex
        #   - newStartIndex = 0
        newResultPair = tuple()
        newLastIndex = copy.deepcopy(tIndex)
        newStartIndex = 0
        if newStartIndex < newLastIndex:
            newReturnedPair = getTwoSumPairs(tIA, tIV, newStartIndex, newLastIndex, newResultPair)
            if not newReturnedPair is False: # meaning a pair was found so 'not newReturnedPair' is 'not True' i.e. False
                return newReturnedPair

    
    if not newReturnedPair: # only runs if both search with both slices return empty
        # this is a fail save loop that uses the whole list tIA[0:lastIndex+1]
        #   - in case the matching pairs on adjacent slices 
        failSafeResultPair = tuple()
        failSafeLastIndex = len(tIA) - 1
        failSafeStartIndex = 0
        if failSafeStartIndex < failSafeLastIndex:
            failSafeReturnedPair = getTwoSumPairs(tIA, tIV, failSafeStartIndex, failSafeLastIndex, failSafeResultPair)
            if not failSafeReturnedPair is False: # meaning a pair was found so 'not failSafeReturnedPair' is 'not True' i.e. False
                return failSafeReturnedPair

    return resultPair # return the empty tuple which has not been changed since the pairs were not found