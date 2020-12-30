# to get all subStrings include the original string
#   - this means that:
#       + minStringLength = 0
#       + maxStringLength = len(inputString)
def getUniqueSubstrings(inputString: str, minStringLength: int, maxStringLength: int):
    inputStringLength = len(inputString)
    subStringList = list() # used to store all the generated substrings
    for outerIndex in range(minStringLength, maxStringLength + 1):
        for innerIndex in range(inputStringLength - minStringLength):
            stringSlice = inputString[innerIndex: innerIndex + outerIndex]
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

# getAllSubstrings() 
# - extracts all the substrings (even when repeated) for a specific 
def getAllSubstrings(inputString: str, minStringLength: int, maxStringLength: int):
    inputStringLength = len(inputString)
    subStringList = list()
    for outerIndex in range(minStringLength, maxStringLength + 1):
        for innerIndex in range(inputStringLength - minStringLength):
            stringSlice = inputString[innerIndex: outerIndex + outerIndex]
            subStringList.append(stringSlice)
    return subStringList
