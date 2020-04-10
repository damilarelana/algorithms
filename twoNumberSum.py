import time

# define twoNumberSum function
# - takes in a user defined integer array
# - takes in a user defined integer value
# - checks if any two elements of array sums up to integer value
# - saves all 2-element `[a, b]` pairs that sum up to integer value, in a dict
# - returns
#       + an empty `[]`, when no 2-element pairs sums up to integer value
#       + a dict of all 2-element `[a, b]` pairs that sum up to integer value


def twoNumberSum():  # inputList param is of type list

    # obtain test array
    testArray = getArray()
    print("Test Array: ", testArray)
    print("Test Array is of type: ", type(testArray))
    print("    ============    \n")

    # obtain test integer
    testInteger = getInteger()
    print("Test Sum: ", testInteger)
    print("Sum is of type: ", type(testInteger))
    print("    ============    \n")

# define getArray()
# - uses a try-except-finally to catch input edge-cases
# - specifies format of user defined array
# - calls the input() to get user defined array
# - calls parseInputArrayString() to convert users `string` to `integer array`
# - returns the user defined integer array value [when all goes to plan]


def getArray():
    try:
        print("Using the format [1, 2, 3, 4] or [1,2,3,4] or [1, 2,3, 4] ...")
        inputArrayString = input("please enter an integer array: ")
        while checkEmptyList(inputArrayString):
            print("Array cannot be empty")
            inputArrayString = input("Enter an integer array: ")
        inputArray = parseInputArrayString(inputArrayString)
    except ValueError:
        raise Exception("Unable to initialize the user defined array")
    finally:
        print("Successfully initialized the *user defined integer array*")
    return inputArray

# define getInteger()
# - uses a try-except-finally to catch input edge-cases
# - calls input() to get user defined integer value
# - returns the user defined integer value [when all goes accordingly to plan]


def getInteger():
    try:
        inputInteger = input("please enter an integer value: ")
        while isinstance(inputInteger, int) is False:
            print("Input must be an integer")
            inputInteger = input("please enter an integer value: ")
    except ValueError:
        raise Exception("Unable to initialize the user defined integer value")
    finally:
        print("Successfully initialized the *user defined integer value*")
    return inputInteger

# define parseInputArrayString() function
# - assumes user leveraged string format: [1, 2, 3, 4] or [1,2,3,4] or [1, 2,3, 4] ...
# - strips away the left and right brackets
# - strips away the extra whitespaces around each element  input()
# - converts each element from a string to an int
# - returns an integer array


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
    twoNumberSum()
    print("Time: %f seconds" % (time.time() - start_time))


if __name__ == "__main__":
    main()
