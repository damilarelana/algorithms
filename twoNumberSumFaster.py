import time


# define twoNumberSum function
# - takes in a user defined integer array
# - takes in a user defined integer value
# - checks if any two elements of array sums up to integer value
# - saves all 2-element `[a, b]` pairs that sum up to integer value, in a dict
# - returns
#       + an empty `[]`, when no 2-element pairs sums up to integer value
#       + a dict of all 2-element `[a, b]` pairs that sum up to integer value


def twoNumberSum():  # inputList param is of type list

    # obtain test array
    testArray = getArray()
    print("\nTest Array: ", testArray)
    print("Test Array is of type: ", type(testArray))
    print("    ============    \n")

    # obtain test integer
    testInteger = getInteger()
    print("\nTest Sum: ", testInteger)
    print("Sum is of type: ", type(testInteger))
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


    # compute the 2-element pairs
    resultDict = computeTwoNumSum(testArray, testInteger)

    # return the results
    if checkEmptyList(str(resultDict[0])):  # checkEmptyList() checks if resultDict[0] is an empty list - str([]) is same as "[]"
        print("No 2-element [a, b] pairs of {0} sums up to the integer value {1}".format(testArray, testInteger))
    else:
        numOfPairs = len(resultDict)
        firstPair = resultDict[0]
        print("There are {0} instances of 2-element [a, b] pairs that sum up to {1} ...".format(numOfPairs, testInteger))
        print("{0} is one of those instances".format(firstPair))


# define computeTwoNumberSum()
# - takes in a user defined integer array tIA
# - takes in a user defined integer value tIV
# - uses the user-define random index selection
# - selects a random start index within tIA
# - then compares to determine a match with the inner element
# - this does NOT restrict the computation to just unique elements of tIA
#    + if an element occurs multiple times, then the [a, b] pair for it would be repeated


def computeTwoNumSum(tIA: list, tIV: int):
    listIndex = 1  # index to obtain smaller/smaller innerList as we loop
    keyDict = 0  # key to store the matching pairs in a dictionary

    resultPair = list()  # initialize placeholder for matched pairs

    # initialize dict, with `index 0` being an empty list
    # - if subsequent pairs are found, `index 0` would be overwritten
    # - if not pairs are found, then we still have our `empty List []` as first value
    resultDict = {
        keyDict: resultPair,
    }

    # loop array elements to check if they sum up to `tIV`
    for t in tIA:
        testDiff = tIV - t
        innerList = tIA[listIndex:]
        for i in innerList:
            if i == testDiff:
                resultPair = [t, testDiff]
                resultDict[keyDict] = resultPair  # append to the dictionary
                keyDict += 1  # increase dictionary index
        listIndex += 1
    return resultDict

# define computeTwoNumberSumOptionTwo()
# - takes in a user defined integer array tIA
# - takes in a user defined integer value tIV
# - computes sum between outer element and inner element
# - then compares to determine a match with tIV
# - this does NOT restrict the computation to just unique elements of tIA
#    + if an element occurs multiple times, then the [a, b] pair for it would be repeated


def computeTwoNumSumOptionTwo(tIA: list, tIV: int):
    listIndex = 1  # index to obtain smaller/smaller innerList as we loop
    keyDict = 0  # key to store the matching pairs in a dictionary

    resultPair = list()  # initialize placeholder for matched pairs

    # initialize dict, with `index 0` being an empty list
    # - if subsequent pairs are found, `index 0` would be overwritten
    # - if not pairs are found, then we still have our `empty List []` as first value
    resultDict = {
        keyDict: resultPair,
    }

    # loop array elements to check if they sum up to `tIV`
    for t in tIA:
        innerList = tIA[listIndex:]
        for i in innerList:
            testSum = t + i
            if testSum == tIV:
                resultPair = [t, i]
                resultDict[keyDict] = resultPair  # append to the dictionary
                keyDict += 1  # increase dictionary index
        listIndex += 1
    return resultDict[0]


# define getArray()
# - uses a try-except-finally to catch input edge-cases
# - specifies format of user defined array
# - calls the input() to get user defined array
# - calls parseInputArrayString() to convert users `string` to `integer array`
# - returns the user defined integer array value [when all goes to plan]


def getArray():
    try:
        print("\nUsing the format [1, 2, 3, 4] or [1,2,3,4] or [1, 2,3, 4] ...")
        inputArrayString = input("please enter an integer array: ")
        while checkEmptyList(inputArrayString):
            print("Array cannot be empty")
            inputArrayString = input("Enter an integer array: ")
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
        inputIntegerString = input("please enter an integer value: ")
        inputInteger = int(inputIntegerString)  # convert string to integer
        while isinstance(inputInteger, int) is False:
            print("Input must be an integer")
            inputIntegerString = input("please enter an integer value: ")
            inputInteger = int(inputIntegerString)
    except ValueError:
        raise Exception("Unable to initialize the user defined integer value")
    finally:
        print("Successfully initialized the *user defined integer value*")
    return inputInteger


# define getIndex()
# - uses a try-except-finally to catch input edge-cases
# - calls input() to get user defined integer value
# - with input being a valid integer, it checks to ensure it is in the required range(listLength)
# - returns the user defined integer value [when all goes accordingly to plan]

def getIndex(lLength: int):
    try:
        inputIndexString = input("please enter an integer index value: ")
        inputIndex = int(inputIndexString)  # convert string to integer
        while isinstance(inputIndex, int) is False:
            print("Index must be an integer")
            getIndex(lLength: int) # recursively call getIndex again
        if (inputIndex in range(lLength)) is False:
            print("Index must be within the range of the list")
            getIndex(lLength: int) # recursively call getIndex again
    except ValueError:
        raise Exception("Unable to initialize the user defined integer index value")
    finally:
        print("Successfully initialized the *user defined integer index value*")
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
        while (isinstance(selectionAnswerString, str) is False) or ((selectionAnswerString in ["y", "Y", "Yes", "YeS", "YEs", "YES", "yES", "yEs", "yeS", "yes", "n", "N", "no", "nO", "No", "NO"]) is False):
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
    start_time = time.time()
    twoNumberSum()
    print("Time: {} seconds".format((time.time() - start_time)))


if __name__ == "__main__":
    main()