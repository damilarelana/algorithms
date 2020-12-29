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

def reverseString(inputList: list):
    inputListLength = len(inputList)
    
    if inputListLength < 2: # handles both single element string or empty string
        return inputList
    
    startIndex = 0
    lastIndex = inputListLength - 1

    if checkIfEven(inputListLength): # even clean split
        demarcationIndex = inputListLength // 2 # ensures you have an even split of swappable elements
        while (startIndex < demarcationIndex):
            inputList[startIndex], inputList[lastIndex] = inputList[lastIndex], inputList[startIndex] # switch elements at extreme ends of the list
            startIndex += 1 # decrement the element scope inwards by shifting startIndex upwards
            lastIndex -= 1 # decrement the element scope inwards by shifting the lastIndex downwards

    if checkIfOdd(inputListLength):
        demarcationIndex = 


    oCount = 0  # initialize the outer counter i.e. which controls repetition after bubbling previous largest values
    while oCount < len(inputList):  # this does not use rlistLength, to ensure we test all elements for largeness
        iCount = 0   # initialize the inner counter i.e. to move one selected element through the list
        while iCount < (inputListLength - 1):
            if inputList[iCount] > inputList[iCount+1]:
                inputList[iCount], inputList[iCount+1] = inputList[iCount+1], inputList[iCount]
            iCount += 1  # so as to move on the the next adjacent elements to test
        oCount += 1  # increment outer loop i.e. number of times we have so far bubbled up the largest value
        inputListLength -= 1  # decrement list length before next iteration, since previous largest value does not need to be involved in next iterations 

    return inputList  # returning a now sorted input List

def splitLength(_):
    demarcationIndex = int(math.ceil(temploopRange/2))          # words for even, odd and prime temploopRange values
    tempListOne = rlist[:demarcationIndex]                      # initialize tempListOne sub-list
    tempListTwo = rlist[demarcationIndex:]                      # initialize tempListTwo sub-list
    tempListOne = mergeSort(tempListOne)                      # recursive call to mergeSorter()
    tempListTwo = mergeSort(tempListTwo)                      # recursive call to mergeSorter()
    return sublistMerge(tempListOne, tempListTwo)


def insertionSort(ulist):
    loopRange = len(ulist)
    if loopRange == 1:
        return ulist    # no point wasting CPU cycle to sort one item
    else:
        # we assume that element at index `0` i.e. ocount = 0, is already sorted, hence why the unsorted starts at ocount = 1
        ocount = 1                       # initialising unsorted list index to the first one to be removed from unsorted [we ]
        while ocount < loopRange:        # handles if len(ulist)=1, unsorted loop index
            icount = ocount              # re-initialising sorted list's max index to allow countdown
            while icount > 0:            # handles inner loop i.e. the `sorted list loop`. greater than zero 
                                         # helps to ensure that when you `bring` a new element (from unsorted) to test/loop against `the sorted
                                         # it helps to ensure that the looping down does not go beyond `index 0` within the sorted
                if ulist[icount-1] > ulist[icount]:           # this already carters for assuming list[0] is sorted
                    ulist[icount - 1], ulist[icount] = ulist[icount], ulist[icount-1]
                icount -= 1 # this is different to bubbleSort i.e. where there is an increment. Here we are decreasing the unsorted set

            ocount += 1 # here we are increasing the sorted set boundaries [which weirdly also acts like the next `first element of the now shrinking unsorted set`]
        return ulist



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
# stirngShuffler()
def stringShuffler(initialString: str):
    randomNumber = secrets.randbits(8192)
    random.seed(randomNumber)
    random.shuffle(initialString) # shuffle the string in place just to be sure :)


# define main() function
def main():

    # test input data
    testString, selectionAnswerString = getInputData()
    stringShuffler(testString) # shuffle the string in place
    testArray = parseStringToList(testString)

    start_time = time.time()
    reverseString(testArray)
    print("Time: {} seconds".format((time.time() - start_time)))


if __name__ == "__main__":
    main()
