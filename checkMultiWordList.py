import time

# checks if the input string (parsed into list) is a `sentence` with words and spacing
#   - if a sentence with words + spacing then the ListFromParsedString would have len(list) > 0
#   - otherwise the list would be 1
#   - assumption is inputList is not empty i.e. len(inputList) >= 1
def isParsedStringMultiWord(inputList: list):
    if len(inputList) == 1: # 
        return False, len(inputList)
    else:
        return True, len(inputList)



# define main() function
def main():

    testList = ["Banner transformed", "into Worldbreaker Hulk,", "at ComicCon 2011."]
    
    start_time = time.time()
    testFlag, listLength = isParsedStringMultiWord(testList)
    print("========================\n")
    print("Given the List {}'".format(testList))
    if testFlag == False:
        print("The input List has only {} element".format(listLength))
    else:
        print("The input List has {} elements".format(listLength))
    
    print("Time: {} seconds".format((time.time() - start_time)))


if __name__ == "__main__":
    main()
