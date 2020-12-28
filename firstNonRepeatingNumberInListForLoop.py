import time
import copy
import secrets
import random

# define twoNumberSum function
# - takes in a user defined integer inputArray
# - takes in a user defined integer value to start search from
# - returns a non-repeating number that
#       + is an element of the inputArray
#       + is not repeated in the same inputArray - even at least once
#       + there is thus no twoNumberSum that is === 2 * number
# - returns `None`, when no non-repeating `returnValue` is found in the inputArray



def twoNumberSum(testArray: list, testSums: list, testIndex: int):  # inputList param is of type list

    # iterate through the different Sums
    messagingFlag = False
    for tIV in testSums:

        # compute the 2-element pairs
        # - note that finalPair = (tIA[startIndex], tIA[lastIndex]) i.e. 
        #   + pair of matching elements of the testArray
        finalPair = computeTwoNumSum(testArray, tIV, testIndex)

        # checks if an empty tuple was returned i.e.
        if (not finalPair): # no pairs found means non-repeating number exists for that particular x for which 2*x = tIV
            nonRepeatedNumber = tIV // 2 # decompose the tIV to constituent value integer value [since tIV = 2*number originally]
            print("The first non-repeating number {} was found in the array {}".format(nonRepeatedNumber, testArray))
            messagingFlag = True
            break # loop

        # [where finalPair finds a match to tIV]
        # test for when a match is possible when it is only due to a nonRepeatingNumber
        # - if tIV = 20 (for when x > 0 or x < 0 e.g. 2 * 10 = 20), this can be due to:
        #       + 15 : 5 [do not want this also - even though it is not due to repeatedNumber as none of the number is a multiple of 10]
        #       + 20 : 0 [do not want this also - even though it is not due to repeatedNumber as none of the number is a multiple of 10]
        #       + 10 : 10 [do not want this - as it easily matches repeatedNumber even though the numbers are multiple of 10]
        #       + -30 : 50 [do not want this - as it easily matches repeatedNumber as none of the number is a multiple of 1]

        # - if tIV = 0 (for when x = 0 i.e. 2 * 0 = 0)
        #       + -10 : 10 [do not want this as neither of them are multiples of 0]
        #       +  0 : 0 [do not want this - as it easily matches repeatedNumber (0) even though the numbers are multiple of 0 ]

    if (messagingFlag is False): # if you did not find any nonReaptedNumber
        print("No non-repeating number found in the array {}".format(testArray))


    

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
        # print("1st slice search")
        if (not returnedPair) is False: # meaning a pair was found so 'not returnedPair' is 'not True' i.e. False
            return returnedPair
        # with returnedPair still being an empty tuple() means the range [startIndex:lastIndex+1] did not give a match in the initial slice tIA[startIndex:lastIndex+1]
        # we need to start another search from [0:startIndex+1]
        #   - we then test the remaining slice i.e. tIA[0:startIndex] (note we can also overlap the slices by using the slice tIA[0:startIndex + 1])
        #   - where newLastIndex = startIndex - 1 or newLastIndex = startIndex
        #   - newStartIndex = 0
        else:
            # print("2nd slice search")
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
        # print("whole array search")
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
        while checkEmptyInputList(inputArrayString):
            print("Array cannot be empty")
            getArray() # recursive call
        inputArray = parseInputArrayString(inputArrayString)
    except ValueError:
        print("Invalid user define input as integer array") # handling the exception by calling getArray() again
        getArray() # recursive call
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


# define selectInputMethod()
# - uses a try-except-finally to catch input edge-cases
# - gives user option to either randomly select test index value or have the use provide it as an input
# - via option to answer 'Yes' or 'No'
# - returns any of the `Yes` or `No` variations in ["y", "Y", "Yes", "YeS", "YEs", "YES", "yES", "yEs", "yeS", "yes", "n", "N", "no", "nO", "No", "NO"]

# def selectInputMethod():
#     try:
#         sampleAnswerList = ["y", "Y", "Yes", "YeS", "YEs", "YES", "yES", "yEs", "yeS", "yes", "n", "N", "no", "nO", "No", "NO"]
#         selectionAnswer = input("To enter your own test integer arrays, enter 'Yes', OTHERWISE enter 'No' for default test integer arrays: ")
#         selectionAnswerString = str(selectionAnswer)  # convert input to string
#         while not ((isinstance(selectionAnswerString, str) is True) and ((selectionAnswerString in sampleAnswerList) is True)):
#             print("Response should be a 'Yes' or 'No' answer")
#             selectInputMethod() # recursively call again
#     except ValueError:
#         raise Exception("Unable to parse the user defined string value")
#     return selectionAnswerString
def selectInputMethod():
    sampleAnswerList = ["y", "Y", "Yes", "YeS", "YEs", "YES", "yES", "yEs", "yeS", "yes", "n", "N", "no", "nO", "No", "NO"]
    while True:
        selectionAnswer = input("To enter your own test integer arrays, enter 'Yes', OTHERWISE enter 'No' for default test integer arrays: ")
        selectionAnswerString = str(selectionAnswer)  # convert input to string
        if (isinstance(selectionAnswerString, str) is True) and ((selectionAnswerString in sampleAnswerList) is True):
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
    if inputArrayString[0] == "[": # only strip the left bracket if it even exists
        inputArrayString = inputArrayString[1:]  # strip left bracket : 'index 0'
    lastIndex = len(inputArrayString) - 1
    if inputArrayString[lastIndex] == "]": # only strip the right bracket if it even exists
        inputArrayString = inputArrayString[:lastIndex]  # strip right bracket : last Index
    return inputArrayString


# define checkEmptyInputList() function
# - takes in an input string in an array format [1, 2, 3, 4]
# - uses python dictionary to simulate a switch
# - uses .strip() to remove whitespaces (and multiple edges-cases of it)
# - checks if it is empty string ""
# - checks if it is empty string "[]" or "[,]"
# - checks if it is whitespace edge-cases: [, ]"" or "[ ,]"" or "[ , ]" etc.
# - returns a True (i.e. an empty list) or otherwise it returns a False
def checkEmptyInputList(inputArrayString: str):
    parsedString = stringStripper(inputArrayString)  # remove the brackets
    parsedStringWithNoWhitespaces = parsedString.strip()
    return {
        "": True,  # handles empty string array of type "[]" or ""
        ",": True,  # handles empty string array of types "[, ]" etc.
    }.get(parsedStringWithNoWhitespaces, False)


def getInputData():
    selectionAnswerString = selectInputMethod()
    if selectionAnswerString in ["y", "Y", "Yes", "YeS", "YEs", "YES", "yES", "yEs", "yeS", "yes"]:
        # obtain test array
        testArray = getArray()

        return testArray, selectionAnswerString

    else: # not necessary to test for 'No', but here is the case for default
        defaultArray = [1, 417, 19, 23, 17, 4, 3, 7, 3, 8, 1, 31, 42, 2, 4, 5, 6, 9, 2]
        return defaultArray, selectionAnswerString
    

# obtain test index - after passing in the length of the array
def getTestIndex(testArray: list, selectionAnswerString: str):
    if (selectionAnswerString is None):
        selectionAnswerString = selectInputMethod()

    if selectionAnswerString in ["y", "Y", "Yes", "YeS", "YEs", "YES", "yES", "yEs", "yeS", "yes"]:
        testIndex = getIndex(len(testArray))
        print("\nTest Index: ", testIndex)
        print("========================\n")
    else: # not necessary to test for `No` here because selectInputMethod() already handles invalid inputs [so the remain values would be `No`]
        testIndex = getRandomIndex(len(testArray))
        print("\nRandom Test Index: ", testIndex)
        print("========================\n")
    return testIndex

#
# listShuffler()
#  - helps to avoid the problem that random.shuffle tends to shuffle in place
#  - takes in a pointer to the list to be shuffled
#  - shuffles the list in place

def listShuffler(initialList: list):
    randomNumber = secrets.randbits(8192) # generate random number for random.seed()
    random.seed(randomNumber) # improve the randomizer by calling random.seed()
    random.shuffle(initialList) # shuffle the list in place just to be sure :)
    # shuffledList = random.sample(workingList, len(workingList))  # take a random sample of list [which returns a shuffled version]

# define main() function
def main():

    # test input data
    testArray, selectionAnswerString = getInputData()
    listShuffler(testArray) # shuffle the array in place
    testArray.sort() # pre-sort
    testIndex = getTestIndex(testArray, selectionAnswerString)

    # test validation data
    # - a number in testArray is non-repeating if
    #       + for a number 'x' in the 'testArray'
    #       + you CANNOT find any other number 'y' in the array 
    #       + for which `y + x = 2x` i.e. there should be no other number y = x
    #  - this means we can validate a non-repeating number if we
    #       + create a testSum made of 2 times each element
    #       + iterate with different tIV which are simply elements of the array testSums
    testSums = [2*x for x in testArray] # 

    start_time = time.time()
    twoNumberSum(testArray, testSums, testIndex)
    print("Time: {} seconds".format((time.time() - start_time)))


if __name__ == "__main__":
    main()
