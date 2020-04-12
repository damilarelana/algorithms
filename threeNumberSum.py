import time

# define threeNumSum function
# - takes in a user defined integer array
# - takes in a user defined integer value
# - checks if any 3 elements of array sums up to integer value
# - saves all 3-element `[a, b, c]` triplets that sum up to integer value, in a dict
# - returns
#       + an empty `[]`, when no 3-element triplets sums up to integer value
#       + a dict of all 3-element `[a, b]` triplets that sum up to integer value

# To Test, let: 
#  - tIV = 30
#  - tIA = "[102, 134, 32, 100, 34, 70, 64, -9, 7, 14, 50, 1, 2, 3, 12, 5, 13]"


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
        print("{0} is one of those instances, in sorted form".format(firstTriplet))

    # constructor a 2-dimensional array using the dictionary values
    two2DArray = build2DArray(resultDict)

    # return the 2-d array
    return two2DArray

# define build2DArray()
# - takes in a dictionary as argument
# - assumes each dict values is an already sorted integer array `list`
# - assumes the maximum value for each `list` would be element at `list[index len(list)-1]`
# - creates a new list i.e. 2DArray with elements consisting of the previous sorted lists
# - uses these maximum values to sort the new list
# - used the .sort(key=lambda ...) to do the actual sorting 
# - return the now sorted 2DArray


def build2DArray(resultDict: dict):

    # extract the `list` of `already sorted lists`
    two2DArray = list()
    for v in resultDict.values():
        if bool(v) is True:
            two2DArray.append(v)

    # sort the `list` of `already sorted lists`
    # two2DArray.sort(key=lambda x: x[len(x) - 1])  # sort by last element in each list
    two2DArray.sort(key=lambda x: (x[0], x[1], x[2]))  # sort by 1st then 2nd then 3rd index of each element

    return two2DArray

# define computeTwoNumberSum()
# - takes in a user defined integer array tIA
# - takes in a user defined integer value tIV
# - computes difference between outer element and tIV
# - then compares to determine a match with the inner element
# - this does NOT restrict the computation to just unique elements of tIA
#    + if an element occurs multiple times, then the [a, b, c] triplet for it would be repeated
# - each matching triplet is sorted using bubbleSort(), before being added to the dictionary


def computeThreeNumSum(tIA: list, tIV: int):
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
    return resultDict


# define bubbleSort()
# - takes in a input list
# - sorts it in ascending order
# - returns a now sorted input list


def bubbleSort(inputList: list):
    inputListLength = len(inputList)
    oCount = 0  # initialize the outer counter i.e. which controls repetition after bubbling previous largest values
    while oCount < len(inputList):  # this does not use rlistLength, to ensure we test all elements for largeness
        iCount = 0   # initialize the inner counter i.e. to move one selected element through the list
        while iCount < (inputListLength - 1):
            if inputList[iCount] > inputList[iCount+1]:
                inputList[iCount], inputList[iCount+1] = inputList[iCount+1], inputList[iCount]
            iCount += 1
        oCount += 1  # increment outer loop i.e. number of times we have so far bubbled up the largest value
        inputListLength -= 1  # decrement list length before next iteration, since previous largest value does not need to be involved in next iterations 

    return inputList  # returning a now sorted input List

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
    two2DArray = threeNumSum()
    print("The 2-dimensional array of matching triplets are: {0}".format(two2DArray))
    print("Time: {} seconds".format((time.time() - start_time)))


if __name__ == "__main__":
    main()
