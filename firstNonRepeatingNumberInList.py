import time
import secrets
import random
import hashlib

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
        print("Successfully parsed the user defined string value")
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
        while checkEmptyInputList(inputArrayString):
            print("Array cannot be empty")
            getArray() # recursive call
        inputArray = parseInputArrayString(inputArrayString)
    except ValueError:
        print("Invalid user define input as integer array") # handling the exception by calling getArray() again
        getArray() # recursive call
    finally:
        print("Successfully initialized the user defined integer array")
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

        return testArray

    else: # not necessary to test for 'No', but here is the case for default
        defaultArray = [1, 417, 19, 23, 17, 4, 3, 7, 3, 8, 1, 31, 42, 2, 4, 5, 6, 9, 2]
        return defaultArray

# def createHasher()
# - takes in a string of the desired hashing algorithm e.g. sha256, sha224 etc.
# - returns the hashing object
def createHasher(hashingAlgorithm: str):
  hasher = hashlib.new(hashingAlgorithm)
  return hasher

# getHash()
# - takes in an Hashlib object i.e. hasher
# - takes in an array element and returns the appropriate hash digest value
def getHash(intValue: int, hasher):
  byteValue = bytes(intValue) # parser the data into bytes
  hasher.update(byteValue) # load the data into the hasher
  hashedString = hasher.hexdigest() # extract hashed value
  return hashedString

# def findRepeatNumber()
# - uses a dictionary i.e. Hastable
# - with hashvalue of each integer as the dictionary key [to ensure uniqueness]
# - using a DAT (direct access table) approach as the hash-table key [i.e. simple integer increments]
# - returns a list of hash
def findNonRepeatingNumber(inputArray: list):
    hashTableAllValues = dict()
    hashTableRepeatingValues = dict()
    nonRepeatingNumber = None # initialize the returned number
    nonRepeatingHashValue = None # initialize the return hashedValue
    for v in inputArray: # iterate through the array
        # create new instances of hasher to avoid hasher.update() problem where repeat calls (a, a, b, c etc.) leads to update being like update(a), update(a+a), update(a+b), update(a+b+c)
        hasher = createHasher('sha256')
        hashedString = getHash(v, hasher) # determine the hashedValue
        # print("{} : {}".format(hashedString, v))
        if (hashTableAllValues.get(hashedString) is None): # when the hashedValue does not exist yet in the hashTable  
            hashTableAllValues.update({hashedString: v}) # update the hashtable with the key value pair '{hashedString, v}'
        else: # means that hashtable already contains an instance of the number being hashed
            hashTableRepeatingValues.update({hashedString: v}) # contains only 1 instance of repeated values e.g. if '2' occurs three times, it would only exist once here
    nonRepeatingKeysSet = getNonRepeatingKeys(hashTableAllValues, hashTableRepeatingValues)
    nonRepeatingKeysList = getListFromSet(nonRepeatingKeysSet)

    if not(checkEmptyHashStringList(nonRepeatingKeysList) is True): # check that the list is not empty
        nonRepeatingNumber = hashTableAllValues.get(nonRepeatingKeysList[0]) # we select 'index 0' i.e. nonRepeatingKeysList[0]
        return nonRepeatingNumber, nonRepeatingKeysList[0]
    else:
        return nonRepeatingNumber, nonRepeatingHashValue # turns 'None' for both i.e. no matching numbers or hashValue

# getListFromSet()
# - constructs a list from a Set
def getListFromSet(inputSet: set):
    l = list()
    for e in inputSet:
        l.append(e) # construct it one by one
    return l # return the constructed list


# def getNonRepeatingKeys()
# returns nonRepeatedKeysSet
def getNonRepeatingKeys(hashTableAllValues, hashTableRepeatingValues):
    allKeysSet = set(list(hashTableAllValues.keys())) # extract dictionary keys and convert to a set
    repeatedKeysSet = set(list(hashTableRepeatingValues.keys()))
    nonRepeatingKeysSet = allKeysSet.difference(repeatedKeysSet) # return only hashedString values that are not repeated during iteration
    return nonRepeatingKeysSet
    

# check if hashedKeyString list is empty
def checkEmptyHashStringList(testList: list):
    if ((not testList) is True) or (len(testList) == 0) or (testList == None):
        return True # i.e. confirms that the list is empty
    else:
        return False

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


def main():

    testArray =  getInputData()
    listShuffler(testArray) # shuffle the list in place to make the testing more realistic
    start_time = time.time()
    nonRepeatedNumber, nonRepeatedHashValue = findNonRepeatingNumber(testArray)
    print("Given {}, the first nonrepeated number: {} was found with a hashvalue: {}".format(testArray, nonRepeatedNumber, nonRepeatedHashValue))
    print("\nTime: {} seconds".format((time.time() - start_time)))
    print("====================================\n")

if __name__ == "__main__":
    main()
