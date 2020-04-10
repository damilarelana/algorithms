import time

# define twoNumberSum function
# * specifies format of user defined array
# * calls the input() method to get user input
# * calls inputArrayStringParser() to convert users `string` to `integer array`
# * returns the inputArray


def twoNumberSum():  # inputList param is of type list
    print("Use array format [1, 2, 3, 4, 5] \n")
    inputArrayString = input("Enter an integer array: ")
    inputArray = inputArrayStringParser(inputArrayString)
    return inputArray


# define arrayInput function
# * uses raw_input()
# * to extract/convert a user defined input string into an array
# * without using the list() constructor
# * without entering the numbers 1 by one
# * allowing using to enter the array in the format "[1, 2, 3, 4, 5, 6]


def inputArrayStringParser(inputString: str):  # inputString is of type string
    inputString = inputString[1:]  # strip left bracket : 'index 0'
    lastIndex = len(inputString) - 1
    inputString = inputString[: lastIndex]  # strip right bracket : last Index
    listOfString = inputString.split(", ")  # get elements using delimiter ", "
    listOfInt = [int(x) for x in listOfString]  # using list comprehension
    return listOfInt  # return the integer array


start_time = time.time()
inputArray = twoNumberSum()
print("Input Array: ", inputArray)
print("Array is of type: ", type(inputArray))
print("Time: %f seconds" % (time.time() - start_time))
