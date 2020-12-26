import time
import copy
import secrets
import random

# define twoNumberSum function
# - takes in a user defined integer array
# - takes in a user defined integer value
# - pre-sorts the list in place before usage
# - checks if any two elements of array sums up to integer value
# - does NOT bother about all 2-element `[a, b]` pairs that sum up to integer value, in a dict
# - focuses only on just 1 uniquer instance
# - returns
#       + an empty `()`, when no 2-element pairs sums up to integer value



def twoNumberSum(testArray: list, testSum: int, testIndex: int):  # inputList param is of type list
    # compute the 2-element pairs
    finalPair = computeTwoNumSum(testArray, testSum, testIndex)

    # return the results
    if not finalPair:  # checks if an empty tuple was returned i.e. no pairs found
        print("No 2-element (a, b) pairs of {0} sums up to the integer value {1}".format(testArray, testSum))
    

# define computeTwoNumberSum()
# - assumes the list has been pre-sorted in ascending manner i.e. default 
# - pre-sorting helps to divide and conquer
# - assumes the sum has to be constituted by two indices i.e. even if the same value exists in two indices
#    + i.e. we are not looking for when the sum is the multiple of just 1 index element
# - takes in a user defined integer array: tIA
# - takes in a user defined integer value: tIV
# - takes in a user defined (or randomly selected) tIndex to start search from
# - this restricts the computation to just one instance of a matching pair
#    + even if similar matching pairs exist at different indices


def computeTwoNumSum(tIA: list, tIV: int, tIndex: int):
    
    # loop array elements to check if they sum up to `tIV`
    # first we divide and conquer by searching in slice tIA[startIndex:lastIndex+1]
    #   - assuming that startIndex is NOT 0 i.e. startIndex > 0
    startIndex = copy.deepcopy(tIndex)  # deepcopy that random sampletIndex  # index to obtain smaller/smaller innerList as we loop
    lastIndex =  len(tIA) - 1
    if startIndex != 0: # this can sometimes help to speed up the search [but not always guaranteed to work]
        returnedPair = getTwoSumPairs(tIA, tIV, startIndex, lastIndex) # using another if startIndex < lastIndex before this, is redundant since getTwoSumPairs already does that
        if (not returnedPair) is False: # meaning a pair was found so 'not returnedPair' is 'not True' i.e. False
            return returnedPair
        # with returnedPair still being an empty tuple() means the range [startIndex:lastIndex+1] did not give a match in the initial slice tIA[startIndex:lastIndex+1]
        # we need to start another search from [0:startIndex+1]
        #   - we then test the remaining slice i.e. tIA[0:startIndex] (note we can also overlap the slices by using the slice tIA[0:startIndex + 1])
        #   - where newLastIndex = startIndex - 1 or newLastIndex = startIndex
        #   - newStartIndex = 0
        else:
            newLastIndex = copy.deepcopy(tIndex) + 1
            newStartIndex = 0
            newReturnedPair = getTwoSumPairs(tIA, tIV, newStartIndex, newLastIndex)
            if (not newReturnedPair) is False: # meaning a pair was found so 'not newReturnedPair' is 'not True' i.e. False
                return newReturnedPair
            else: # this means search withing both slices as failed and we now need to search across both slices
                firstFailSafeLastIndex = len(tIA) - 1
                firstFailSafeStartIndex = 0
                firstFailSafeReturnedPair = getTwoSumPairs(tIA, tIV, firstFailSafeStartIndex, firstFailSafeLastIndex)
                if (not firstFailSafeReturnedPair) is False: # meaning a pair was found so 'not failSafeReturnedPair' is 'not True' i.e. False
                    return firstFailSafeReturnedPair
                firstFailSafeReturnedPair = tuple() 
                return firstFailSafeReturnedPair # this is the catch-all for when that matching pairs are not found
    else: # the search jumps here immediately if startIndex is 0
        # this is a fail save loop that uses the whole list tIA[0:lastIndex+1]
        #   - in case the matching pairs on adjacent slices 
        lastFailSafeLastIndex = len(tIA) - 1
        lastFailSafeStartIndex = 0
        lastFailSafeReturnedPair = getTwoSumPairs(tIA, tIV, lastFailSafeStartIndex, lastFailSafeLastIndex)
        if (not lastFailSafeReturnedPair) is False: # meaning a pair was found so 'not failSafeReturnedPair' is 'not True' i.e. False
            return lastFailSafeReturnedPair
        lastFailSafeReturnedPair = tuple() 
        return lastFailSafeReturnedPair # this is the catch-all for when that matching pairs are not found


def getTwoSumPairs(tIA: list, tIV: int, startIndex: int, lastIndex: int):
    resultPair = tuple()
    while startIndex < lastIndex:
        tempSum = tIA[startIndex] + tIA[lastIndex]
        if tempSum == tIV:
            resultPair = (tIA[startIndex], tIA[lastIndex])
            print("Successfully found a pair ({}, {}) at tIA[{}] and tIA[{}]".format(tIA[startIndex], tIA[lastIndex], startIndex, lastIndex))
            return resultPair
        
        # if the tempSum is larger than tIV then it means
        #   - indices that provide a match (the startIndex to give tIV) would have to be lower than lastIndex
        #   - thus we should `let startIndex remain unchanged`, but `start decreasing lastIndex` decrementally 1 step at a time`
        #   - i.e. let `lastIndex -= 1`
        # otherwise if tempSum is smaller than tIV
        #   - indices that provide a match (the startIndex to give tIV) would have to be higher than startIndex [since lastIndex is already the biggest value in list]
        #   - thus we should `let lastIndex remain unchanged`, but `start increasing lastIndex`incrementally 1 step at a time`
        #   - i.e. let `startIndexIndex -= 1`
        if tempSum > tIV: # notice that "==" is already handled by the previous loop the returns a result
            lastIndex -= 1
        else:
            startIndex += 1
    return resultPair


# define getArray()
# - uses a try-except-finally to catch input edge-cases
# - specifies format of user defined array
# - calls the input() to get user defined array
# - calls parseInputArrayString() to convert users `string` to `integer array`
# - returns the user defined integer array value [when all goes to plan]


def getArray():
    try:
        print("\nUsing the format [1, 2, 3, 4] or [1,2,3,4] or [1, 2,3, 4] ...")
        inputArrayString = input("Enter an integer array: ")
        while checkEmptyList(inputArrayString):
            print("Array cannot be empty")
            getArray() # recursive call
        inputArray = parseInputArrayString(inputArrayString)
    except ValueError:
        raise Exception("Unable to initialize the user defined array")
    finally:
        print("Successfully initialized the *user defined integer array*")
    return inputArray

# define getInteger()
# - uses a try-except-finally to catch input edge-cases
# - calls input() to get user defined integer value
# - returns the user defined integer value [when all goes accordingly to plan]

def getInteger():
    try:
        inputIntegerString = input("Enter a test value for 'Sum of Integers': ")
        inputInteger = int(inputIntegerString)  # convert string to integer
        while isinstance(inputInteger, int) is False:
            print("Input must be an integer")
            getInteger() # recursive call
    except ValueError:
        raise Exception("Unable to initialize the user defined test value for 'Sum of Integers'")
    finally:
        print("Successfully initialized the *user defined test value for 'Sum of Integers'*")
    return inputInteger


# define getIndex()
# - uses a try-except-finally to catch input edge-cases
# - calls input() to get user defined integer value
# - with input being a valid integer, it checks to ensure it is in the required range(listLength)
# - returns the user defined integer value [when all goes accordingly to plan]

def getIndex(lLength: int):
    try:
        inputIndexString = input("Enter an integer test initiation index: ")
        inputIndex = int(inputIndexString)  # convert string to integer
        while isinstance(inputIndex, int) is False:
            print("Index must be an integer")
            getIndex(lLength) # recursive call
        if (inputIndex in range(lLength)) is False:
            print("Index must be within the range of the list")
            getIndex(lLength)
    except ValueError:
        raise Exception("Unable to initialize the user defined integer test initiation index")
    finally:
        print("Successfully initialized the *user defined integer test initiation index*")
    return inputIndex

#
# getRandomIndex()
#  - helps to pick a random integer within a range of numbers that represent the indices of an array
#  - lowest possible integer is '0' even if the original number was 0.1
#  - it does not use ceil() because this can lead to the index being out of range when the random number choice is len(Array)-1

def getRandomIndex(lLength: int):
    randomSeedBits = secrets.randbits(8192)     # generate random integer number [for random.seed()] that contains 8192 bits in it
    random.seed(randomSeedBits)     # improve the randomizer by calling random.seed() i.e. make the randomizer stronger
    return random.randint(0, lLength - 1) # use the randomizer to generate and return a random integer in the range '0' to 'len(testArray) - 1'


# define selectGetIndexMethod()
# - uses a try-except-finally to catch input edge-cases
# - gives user option to either randomly select test index value or have the use provide it as an input
# - via option to answer 'Yes' or 'No'
# - returns any of the `Yes` or `No` variations in ["y", "Y", "Yes", "YeS", "YEs", "YES", "yES", "yEs", "yeS", "yes", "n", "N", "no", "nO", "No", "NO"]

def selectGetIndexMethod():
    try:
        selectionAnswer = input("To select integer testIndex yourself enter 'Yes', otherwise enter 'No' for randomly generated value: ")
        selectionAnswerString = str(selectionAnswer)  # convert input to string
        sampleAnswerList = ["y", "Y", "Yes", "YeS", "YEs", "YES", "yES", "yEs", "yeS", "yes", "n", "N", "no", "nO", "No", "NO"]
        while (isinstance(selectionAnswerString, str) is False) or ((selectionAnswerString in sampleAnswerList) is False):
            print("Response should be a 'Yes' or 'No' answer")
            selectGetIndexMethod() # recursively call selectGetIndexMethod() again
    except ValueError:
        raise Exception("Unable to parse the user defined string value")
    finally:
        print("Successfully parsed the *user defined string value*")
    return selectionAnswerString

# define parseInputArrayString() function
# - assumes user leveraged string format: [1, 2, 3, 4] or [1,2,3,4] or [1, 2,3, 4] ...
# - strips away the left and right brackets
# - strips away the extra whitespaces around each element  input()
# - converts each element from a string to an int
# - returns an integer array


def parseInputArrayString(inputString: str):  # inputString is of type string
    parsedString = stringStripper(inputString)
    listOfString = parsedString.split(",")  # get elements using delimiter ","
    listOfString = [s.strip() for s in listOfString]  # remove whitespaces around each element
    listOfInt = [int(s) for s in listOfString]  # using list comprehension
    return listOfInt  # return the integer array


# define stringStripper() function
#  - takes in an input string in an array format [1, 2, 3, 4]
#  - strips away the brackets
#  - returns a bare parsed string


def stringStripper(inputArrayString: str):
    inputArrayString = inputArrayString[1:]  # strip left bracket : 'index 0'
    lastIndex = len(inputArrayString) - 1
    parsedArrayString = inputArrayString[: lastIndex]  # strip right bracket : last Index
    return parsedArrayString

# define checkEmptyList() function
# - takes in an input string in an array format [1, 2, 3, 4]
# - uses python dictionary to simulate a switch
# - uses .strip() to remove whitespaces (and multiple edges-cases of it)
# - checks if it is empty string ""
# - checks if it is empty string "[]" or "[,]"
# - checks if it is whitespace edge-cases: [, ]"" or "[ ,]"" or "[ , ]" etc.
# - returns a True (i.e. an empty list) or otherwise it returns a False


def checkEmptyList(inputArrayString: str):
    parsedString = stringStripper(inputArrayString)  # remove the brackets
    parsedStringWithNoWhitespaces = parsedString.strip()
    return {
        "": True,  # handles empty string array of type "[]" or ""
        ",": True,  # handles empty string array of types "[, ]" etc.
    }.get(parsedStringWithNoWhitespaces, False)

# define main() function
# - to allow code to be run as either standalone or re-usable code

def main():

    # obtain test array
    testArray = getArray()
    testArray.sort() # this pre-sorts it in place
    print("\nTest Array: ", testArray)
    print("Test Array is of type: ", type(testArray))
    print("    ============    \n")

    # obtain test integer
    testSum = getInteger()
    print("\nTest Sum: ", testSum)
    print("Sum is of type: ", type(testSum))
    print("    ============    \n")

    # obtain test index - after passing in the length of the array
    selectionAnswerString = selectGetIndexMethod()
    if selectionAnswerString in ["y", "Y", "Yes", "YeS", "YEs", "YES", "yES", "yEs", "yeS", "yes"]:
        testIndex = getIndex(len(testArray))
        print("\nTest Index: ", testIndex)
        print("Index is of type: ", type(testIndex))
        print("    ============    \n")
    else: # not necessary to test for `No` here because selectGetIndexMethod() already handles invalid inputs [so the remain values would be `No`]
        testIndex = getRandomIndex(len(testArray))
        print("\nTest Index: ", testIndex)
        print("Index is of type: ", type(testIndex))
        print("    ============    \n")

    start_time = time.time()
    twoNumberSum(testArray, testSum, testIndex)
    print("Time: {} seconds".format((time.time() - start_time)))


if __name__ == "__main__":
    main()
