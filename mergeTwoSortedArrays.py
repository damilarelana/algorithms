import time
import pdb

# subListMerge()
# - takes two sorted list as arguments
# - returns a sorted and merge list from that
def sublistMerge(tempSubListOne, tempSubListTwo):
    tempMergedList = []                                             # initialise empty List to merge sub-Lists into

    loopRangeSubListOne = len(tempSubListOne)
    loopRangeSubListTwo = len(tempSubListTwo)

    indexSubListOne = 0                                             # avoids using list.pop() to remove element
    indexSubListTwo = 0

    while loopRangeSubListOne > indexSubListOne and loopRangeSubListTwo > indexSubListTwo:      # a=[1]->len(a)=1
        if tempSubListOne[indexSubListOne] > tempSubListTwo[indexSubListTwo]:                   # test smaller element
            tempMergedList.append(tempSubListTwo[indexSubListTwo])                         # add to end of tempMergeList
            indexSubListTwo += 1
        else:
            tempMergedList.append(tempSubListOne[indexSubListOne])                         # add to end of tempMergeList
            indexSubListOne += 1

    while loopRangeSubListOne > indexSubListOne:                                  # no elements to merge in SubListTwo
        tempMergedList.append(tempSubListOne[indexSubListOne])                    # remaining elements are appended
        indexSubListOne += 1

    while loopRangeSubListTwo > indexSubListTwo:                                  # no elements to merge in SubListOne
        tempMergedList.append(tempSubListTwo[indexSubListTwo])                    # remaining elements are appended
        indexSubListTwo += 1

    return tempMergedList

# define selectInputMethod()
# - uses a try-except-finally to catch input edge-cases
# - gives user option to either randomly select test index value or have the use provide it as an input
# - via option to answer 'Yes' or 'No'
# - returns any of the `Yes` or `No` variations in ["y", "Y", "Yes", "YeS", "YEs", "YES", "yES", "yEs", "yeS", "yes", "n", "N", "no", "nO", "No", "NO"]

def selectInputMethod():
    try:
        selectionAnswer = input("To enter your own test integer arrays, enter 'Yes', OTHERWISE enter 'No' for default test integer arrays: ")
        selectionAnswerString = str(selectionAnswer)  # convert input to string
        sampleAnswerList = ["y", "Y", "Yes", "YeS", "YEs", "YES", "yES", "yEs", "yeS", "yes", "n", "N", "no", "nO", "No", "NO"]
        while (isinstance(selectionAnswerString, str) is False) or ((selectionAnswerString in sampleAnswerList) is False):
            print("Response should be a 'Yes' or 'No' answer")
            selectInputMethod() # recursively call selectGetIndexMethod() again
    except ValueError:
        raise Exception("Unable to parse the user defined string value")
    finally:
        print("Successfully parsed the *user defined string value*")
    return selectionAnswerString


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
        print("Invalid user define input as integer array") # handling the exception by calling getArray() again
        getArray() # recursive call
    finally:
        print("Successfully initialized the *user defined integer array*")
    return inputArray


# parseInputArrayString()
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


def getInputData():
    selectionAnswerString = selectInputMethod()
    if selectionAnswerString in ["y", "Y", "Yes", "YeS", "YEs", "YES", "yES", "yEs", "yeS", "yes"]:
        # obtain test array
        firstTestArray = getArray()
        firstTestArray.sort() # this pre-sorts it in place

        secondTestArray = getArray()
        secondTestArray.sort() # this pre-sorts it in place

        return firstTestArray, secondTestArray

    else: # not necessary to test for 'No', but here is the case for default
        defaultFirstArray = [1, 2, 4, 5, 6, 9]
        defaultFirstArray.sort() # sort in place

        defaultSecondArray = [7, 3, 8, 0, 31, 42]
        defaultSecondArray.sort() # sort in place

        return defaultFirstArray, defaultSecondArray


def main():

    start_time = time.time()
    firstSortedArray, secondSortedArray =  getInputData()
    mergedSortedArray = sublistMerge(firstSortedArray, secondSortedArray)
    print("Given {} and {}, the merged sorted array is {}".format(firstSortedArray, secondSortedArray, mergedSortedArray))
    print("\nTime: {} seconds".format((time.time() - start_time)))
    print("====================================\n")

if __name__ == "__main__":
    main()
