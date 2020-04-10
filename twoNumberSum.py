import time

# define twoNumberSum function
# - specifies format of user defined array
# - calls the input() method to get user input
# - calls inputArrayStringParser() to convert users `string` to `integer array`
# - returns the inputArray


def twoNumberSum():  # inputList param is of type list
    print("Use array format [1, 2, 3, 4, 5] \n")
    inputArrayString = input("Enter an integer array: ")
    while checkEmptyList(inputArrayString):
        print("Array cannot be empty")
        inputArrayString = input("Enter an integer array: ")
    inputArray = inputArrayStringParser(inputArrayString)
    return inputArray


# define arrayInput function
# - uses raw_input()
# - to extract/convert a user defined input string into an array
# - without using the list() constructor
# - without entering the numbers 1 by one
# - allowing using to enter the array in the format "[1, 2, 3, 4, 5, 6]


def inputArrayStringParser(inputString: str):  # inputString is of type string
    parsedString = stringStripper(inputString)
    listOfString = parsedString.split(", ")  # get elements using delimiter ", "
    listOfInt = [int(x) for x in listOfString]  # using list comprehension
    return listOfInt  # return the integer array


# define stringStripper() function
#  - takes in an input string in an array format [1, 2, 3, 4]
#  - strips away the brackets
#  - returns a bare parsed string


def stringStripper(inputArrayString: str):
    inputArrayString = inputArrayString[1:]  # strip left bracket : 'index 0'
    lastIndex = len(inputArrayString) - 1
    parsedArrayString = inputArrayString[: lastIndex]  # strip right bracket : last Index
    return parsedArrayString

# define checkEmptyList() function
# - takes in an input string in an array format [1, 2, 3, 4]
# - uses python dictionary to simulate a switch
# - uses .strip() to remove whitespaces (and multiple edges-cases of it)
# - checks if it is empty string ""
# - checks if it is empty string "[]" or "[,]"
# - checks if it is whitespace edge-cases: [, ]"" or "[ ,]"" or "[ , ]" etc.
# - returns a True (i.e. an empty list) or otherwise it returns a False


def checkEmptyList(inputArrayString: str):
    parsedString = stringStripper(inputArrayString)  # remove the brackets
    parsedStringWithNoWhitespaces = parsedString.strip()
    return {
        "": True,  # handles empty string array of type "[]" or ""
        ",": True,  # handles empty string array of types "[, ]" etc.
    }.get(parsedStringWithNoWhitespaces, False)


# define main() function
# - to allow code to be run as either standalone or re-usable code

def main():
    start_time = time.time()
    inputArray = twoNumberSum()
    print("Input Array: ", inputArray)
    print("Array is of type: ", type(inputArray))
    print("Time: %f seconds" % (time.time() - start_time))


if __name__ == "__main__":
    main()
