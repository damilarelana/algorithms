import random
import time
import secrets
import random
import pdb

# checkIfEven()
# - checks if a number is even 
# - returns True is valid (or False if otherwise)
def checkIfEven(number: int) -> bool:
    Flag = False
    if (number % 2) == 0:
        Flag = True
    return Flag


# checkIfOdd()
# - checks if a number is Odd
# - returns True is valid (or False if otherwise)
def checkIfOdd(number: int) -> bool:
    Flag = False
    if (number % 2) == 1:
        Flag = True
    return Flag

# getInteger()
# - used to obtain the required test data
def getSentence():
    try:
        inputSentence = input("Enter input sentence: ")
        inputSentence = str(inputSentence)
        while (inputSentence is None):
            print("Input cannot be empty")
            getSentence() # recursive call
    except ValueError:
        raise Exception("Unable to initialize the user defined sentence")
    return inputSentence

def parseListToSentence(inputList: list) -> str:  # 
    counter = 0
    newSentence = ""
    listLength = len(inputList)
    for e in inputList:
        if counter == (listLength - 1): # i.e. no need to add extra space at the end o fthe 
            newSentence += str(e)
        else:
            newSentence += str(e) + " " # add space between each string concatenation
        counter += 1  
    return newSentence

def parseSentenceToList(inputSentence: str) -> list:  # 
    listOfSentences = inputSentence.split(" ")  # extract each string elements into a list
    counter = 0 # counter is being used because the following were not working s.strip(), s = s.replace()
    for s in listOfSentences: # using a for loop as it is fastest and constant in terms of time complexity i.e. better than list comprehension `list = [s for s in inputString]`
        listOfSentences[counter].strip() # remove whitespaces around each element 
        listOfSentences[counter] = listOfSentences[counter].replace(',', '') # remove "," around each element
        listOfSentences[counter] = listOfSentences[counter].replace('.', '') # remove "." around each element
        counter += 1
    return listOfSentences


# define selectInputMethod()
# - uses a try-except-finally to catch input edge-cases
# - gives user option to either randomly select test index value or have the use provide it as an input
# - via option to answer 'Yes' or 'No'
# - returns any of the `Yes` or `No` variations in ["y", "Y", "Yes", "YeS", "YEs", "YES", "yES", "yEs", "yeS", "yes", "n", "N", "no", "nO", "No", "NO"]

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
        testSentence = getSentence()
        return testSentence, selectionAnswerString

    else: # not necessary to test for 'No', but here is the case for default
        defaultSentence = "Banner transformed into Worldbreaker Hulk, at ComicCon 2011."
        return defaultSentence, selectionAnswerString


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

# define main() function
def main():

    # test input data
    testSentence, _ = getInputData()

    start_time = time.time()
    sentenceAsList = parseSentenceToList(testSentence)
    reversedList = reverseOrderOfListElements(sentenceAsList)
    reversedSentence = parseListToSentence(reversedList)
    print("========================\n")
    print("Given the original sentence '{}', the reversed sentence is '{}'".format(testSentence, reversedSentence))
    print("Time: {} seconds".format((time.time() - start_time)))


if __name__ == "__main__":
    main()
