import time

def parseListToString(inputList: list) -> str:  # 
    counter = 0
    newString = ""
    listLength = len(inputList)
    for e in inputList:
        if counter == (listLength - 1): # i.e. no need to add extra space at the end of the 
            newString += str(e)
        else:
            newString += str(e) + " " # add space between each string concatenation
        counter += 1  
    return newString


# define main() function
def main():

    testString = "Banner transformed into Worldbreaker Hulk, at ComicCon 2011."
    
    start_time = time.time()
    parsedListToString = parseListToString(testString)
    print("========================\n")
    print("Given the List {}'".format(testString))
    print("The generated string is '{}'".format(parsedListToString))
    print("Time: {} seconds".format((time.time() - start_time)))


if __name__ == "__main__":
    main()
