import time

def parseStringToList(inputString: str) -> list:  # 
    listOfStrings = inputString.split(" ")  # extract each string elements into a list
    counter = 0 # counter is being used because the following were not working s.strip(), s = s.replace()
    for s in listOfStrings: # using a for loop as it is fastest and constant in terms of time complexity i.e. better than list comprehension `list = [s for s in inputString]`
        listOfStrings[counter].strip() # remove whitespaces around each element 
        listOfStrings[counter] = listOfStrings[counter].replace(',', '') # remove "," around each element
        listOfStrings[counter] = listOfStrings[counter].replace('.', '') # remove "." around each element
        counter += 1
    return listOfStrings



# define main() function
def main():

    testString = "Banner transformed into Worldbreaker Hulk, at ComicCon 2011."
    
    start_time = time.time()
    parsedStringToList = parseListToString(testString)
    print("========================\n")
    print("Given the List {}'".format(testString))
    print("The generated string is '{}'".format(parsedListToString))
    print("Time: {} seconds".format((time.time() - start_time)))


if __name__ == "__main__":
    main()
