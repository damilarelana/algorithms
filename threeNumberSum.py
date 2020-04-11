import time

# define threeNumSum function
# - takes in a user defined integer array
# - takes in a user defined integer value
# - checks if any 3 elements of array sums up to integer value
# - saves all 3-element `[a, b, c]` triplets that sum up to integer value, in a dict
# - returns
#       + an empty `[]`, when no 3-element triplets sums up to integer value
#       + a dict of all 3-element `[a, b]` triplets that sum up to integer value


def threeNumSum():  # inputList param is of type list

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

    # compute the 3-element triplets
    resultDict = computeThreeNumSum(testArray, testInteger)

    # return the results
    if checkEmptyList(str(resultDict[0])):  # checkEmptyList() checks if resultDict[0] is an empty list - str([]) is same as "[]"
        print("No 3-element [a, b, c] triplets of {0} sums up to the integer value {1}".format(testArray, testInteger))
    else:
        numOfTriplets = len(resultDict)
        firstTriplet = resultDict[0]
        print("There are {0} instances of 3-element [a, b, c] triplets that sum up to {1} ...".format(numOfTriplets, testInteger))
        print("{0} is one of those instances".format(firstTriplet))

# define computeTwoNumberSum()
# - takes in a user defined integer array tIA
# - takes in a user defined integer value tIV
# - computes difference between outer element and tIV
# - then compares to determine a match with the inner element
# - this does NOT restrict the computation to just unique elements of tIA
#    + if an element occurs multiple times, then the [a, b, c] triplet for it would be repeated
# - each matching triplet is sorted using bubbleSort(), before being added to the dictionary


def computeThreeNumSum(tIA: list, tIV: int):
    listIndex = 1  # index to obtain smaller/smallest lists intermediateList/innerList as we loop
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
        intermediateList = tIA[listIndex:]
        for i in intermediateList:
            testDiff = intermediatetIV - i
            innerList = intermediatetIV[listIndex:]
            for j in innerList:
                if j == testDiff:
                    resultTriplet = [t, i, j]  # current matching triplet is now identified 
                    resultTriplet = bubbleSort(resultTriplet)  # sort matching triplet
                    resultDict[keyDict] = resultTriplet  # append to dict
                    keyDict += 1  # increase dictionary index
        listIndex += 1
    return resultDict


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
    threeNumSum()
    print("Time: {} seconds".format((time.time() - start_time)))


if __name__ == "__main__":
    main()
