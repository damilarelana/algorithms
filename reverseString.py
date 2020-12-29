import random
import time
import secrets
import random

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
def getString():
    try:
        inputString = input("Enter input string: ")
        inputString = str(inputString)
        while (inputString is None):
            print("Input cannot be empty")
            getString() # recursive call
    except ValueError:
        raise Exception("Unable to initialize the user defined integers")

# 
def parseStringToList(inputString: str) -> list:  # inputString is of type string
    l = list()
    for s in inputString: # using a for loop as it is fastest and constant in terms of time complexity i.e. better than list comprehension `list = [s for s in inputString]`
        l.append(s) # construct it one by one
    return l # return the constructed list


# 
def parseListToString(inputList: list) -> str:  # inputString is of type string
    s = ""
    for l in inputList: 
        s += str(l)
    return s 


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
        testString = getString()
        return testString, selectionAnswerString

    else: # not necessary to test for 'No', but here is the case for default
        defaultString = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return defaultString, selectionAnswerString

#
# stringShuffler()
def stringShuffler(initialString: str):
    randomNumber = secrets.randbits(8192)
    random.seed(randomNumber)
    shuffledString = ''.join(random.sample(initialString, len(initialString))) # shuffle the string in place just to be sure :)
    return shuffledString


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
    testString, _ = getInputData()
    shuffledTestString = stringShuffler(testString) # shuffle the string in place
    testArray = parseStringToList(shuffledTestString)

    start_time = time.time()
    reversedList = reverseOrderOfListElements(testArray)
    reversedString = parseListToString(reversedList)
    print("========================\n")
    print("Given the original string {}, the reversed string is {}".format(shuffledTestString, reversedString))
    print("Time: {} seconds".format((time.time() - start_time)))


if __name__ == "__main__":
    main()
