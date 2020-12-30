# checks if the input string (parsed into list) is a `sentence` with words and spacing
#   - if a sentence with words + spacing then the ListFromParsedString would have len(list) > 0
#   - otherwise the list would be 1
#   - assumption is inputList is not empty i.e. len(inputList) >= 1
def isParsedStringMultiWord(inputList: list) -> bool :
    if len(inputList) == 1: # 
        return False
    else:
        return True

