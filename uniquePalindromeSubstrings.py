import random
import time
import secrets
import random
import pdb
import hashlib

def getString():
    try:
        inputString = input("Enter input string: ")
        inputString = str(inputString)
        while (inputString is None):
            print("Input cannot be empty")
            getString() # recursive call
    except ValueError:
        raise Exception("Unable to initialize the user defined string")
    return inputString


def getMinSubStringLength(inputString: str):
    inputStringLength = len(inputString)
    try:
        inputIntegerString = input("Enter a minimum subString length as an integer ( >= 0): ")
        inputInteger = int(inputIntegerString)  # convert string to integer
        while isinstance(inputInteger, int) is False:
            print("Input must be a integer")
            getMinSubStringLength() # recursive call

        while not ((inputInteger >= 0) and (inputInteger <= inputStringLength)): # ensure the value is within required range
            print("Input integer should be >= 0 and <= len(inputString)")
            getMinSubStringLength() # recursive call

    except ValueError:
        raise Exception("Unable to initialize the user defined value for minimum subString length")
    return inputInteger


def getMaxSubStringLength(inputString: str, minSubStringLength: int):
    inputStringLength = len(inputString)
    try:
        inputIntegerString = input("Enter a maximum subString length as an integer ( >= 0): ")
        inputInteger = int(inputIntegerString)  # convert string to integer
        while isinstance(inputInteger, int) is False:
            print("Input must be a integer")
            getMaxSubStringLength() # recursive call

        while not ((inputInteger >= 0) and (inputInteger <= inputStringLength) and (inputInteger >= minSubStringLength)): # ensure the value is within required range
            print("Input integer should be >= 0 and <= len(inputString) and >= minimum subString length")
            getMinSubStringLength() # recursive call

    except ValueError:
        raise Exception("Unable to initialize the user defined value for maximum subString length")
    return inputInteger


def selectInputMethod():
    sampleAnswerList = ["y", "Y", "Yes", "YeS", "YEs", "YES", "yES", "yEs", "yeS", "yes", "n", "N", "no", "nO", "No", "NO"]
    while True:
        selectionAnswer = input("To enter your own test string, enter 'Yes', OTHERWISE enter 'No' for default string: ")
        selectionAnswerString = str(selectionAnswer)  # convert input to string
        if (isinstance(selectionAnswerString, str) is True) and ((selectionAnswerString in sampleAnswerList) is True):
            return selectionAnswerString


def getInputData():
    selectionAnswerString = selectInputMethod()
    if selectionAnswerString in ["y", "Y", "Yes", "YeS", "YEs", "YES", "yES", "yEs", "yeS", "yes"]:
        # obtain test array
        testString = getString()
        minStringLength = getMinSubStringLength(testString)
        maxStringLength = getMaxSubStringLength(testString, minStringLength)
        return testString, selectionAnswerString, minStringLength, maxStringLength

    else: # not necessary to test for 'No', but here is the case for default
        # defaultSentence = "wow anna is at already at madam level"
        defaultSentence = "aabbbaa"
        minStringLength = 2
        maxStringLength = len(defaultSentence)
        return defaultSentence, selectionAnswerString, minStringLength, maxStringLength


# reverseOrderOfListElements()
def reverseOrderOfListElements(inputList: list):
    inputListLength = len(inputList)
    
    if inputListLength < 2: # handles both single element string or empty string
        return inputList
    else: 
        startIndex = 0
        lastIndex = inputListLength - 1

        demarcationIndex = inputListLength // 2 # ensures you have an even split of swappable elements (still works if inputListLength is odd) as it means the central element is not swapped
        while (startIndex < demarcationIndex):
            inputList[startIndex], inputList[lastIndex] = inputList[lastIndex], inputList[startIndex] # switch elements at extreme ends of the list
            startIndex += 1 # decrement the element scope inwards by shifting startIndex upwards
            lastIndex -= 1 # decrement the element scope inwards by shifting the lastIndex downwards
        return inputList # return a list with all the elements swapped

# to get all subStrings include the original string
#   - this means that:
#       + minStringLength = 0
#       + maxStringLength = len(inputString)
def getUniqueSubstrings(inputString: str, minStringLength: int, maxStringLength: int):
    inputStringLength = len(inputString)
    subStringList = list() # used to store all the generated substrings
    for i in range((inputStringLength+1) - minStringLength):
        for j in range(minStringLength, maxStringLength + 1):
            sliceLowerIndex = i 
            sliceUpperIndex = i + j
            if sliceUpperIndex <= maxStringLength: # exclude illogical slices like list[5:10] when the actual length of the array is 7 i.e. limit things to list[5:7]
                print("sliceLowerIndex: {} - sliceUpperIndex: {} gives {}".format(sliceLowerIndex, sliceUpperIndex, inputString[sliceLowerIndex: sliceUpperIndex]))
                stringSlice = inputString[sliceLowerIndex: sliceUpperIndex]
                subStringList.append(stringSlice)

    uniqueSubStringList = list()
    uniqueSubstringSet = set()

    for subString in subStringList: # iterate over all the substrings generated
        if subString in uniqueSubstringSet: # check if the set already has the subString stored
            pass # do nothing since a set only contains unique stuff
        else: # if the subString does not exist in the set THEN add to both the set and uniqueList
            uniqueSubStringList.append(subString) 
            uniqueSubstringSet.add(subString)

    return uniqueSubStringList, uniqueSubstringSet, subStringList

def parseStringToList(inputString: str) -> list:  # 
    l = list()
    for s in inputString: # using a for loop as it is fastest and constant in terms of time complexity i.e. better than list comprehension `list = [s for s in inputString]`
        l.append(s) # construct it one by one
    return l # return the constructed list

def parseListToString(inputList: list) -> str:  # 
    counter = 0
    newString = ""
    listLength = len(inputList)
    for e in inputList:
        newString += str(e) # i.e. no need to add extra space at the end of the [since this is used for a string including spaces and not a sentence]
        counter += 1  
    return newString

def reverseString(inputString: str) -> str:
    generatedStringList = parseStringToList(inputString) # convert original string to a list
    reversedStringList = reverseOrderOfListElements(generatedStringList) # reverse order of the list elements
    reversedString = parseListToString(reversedStringList)# convert the reversed list back to a String
    return reversedString

def palindrome():
    testString, _, minStringLength, maxStringLength = getInputData() # get the original test data
    uniqueSubStringsList, _, _ = getUniqueSubstrings(testString, minStringLength, maxStringLength) # get the subStrings
    palindromeStrings = list() # initialize the palindrome container

    # iterate through all the subStrings to test palindrome
    for subString in uniqueSubStringsList:
        reversedSubString = reverseString(subString) # reverse string
        if (reversedSubString  == subString):# check if reversedSubString is equivalent to the original subString
            palindromeStrings.append(subString) # store the subString as a palindrome
    
    return palindromeStrings, testString, minStringLength


# define main() function
def main():

    start_time = time.time()

    palindromeStrings, testString, minStringLength = palindrome()
    palindromeStringsLength = len(palindromeStrings)

    print("========================\n")
    print("The test String is '{}'.".format(testString))
    if (not palindromeStrings):
        print("{} instances of at least {} subStrings was a palindrome string'.".format(palindromeStringsLength, minStringLength))
    else:
        print("{} instances of at least {} subStrings were found to be a palindrome string.".format(palindromeStringsLength, minStringLength), end=" ")
        print("These are: {}'.".format(palindromeStrings))
    print("Time: {} seconds".format((time.time() - start_time)))


if __name__ == "__main__":
    main()
