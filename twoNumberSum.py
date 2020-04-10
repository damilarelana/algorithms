import time

# define twoNumberSum function


def twoNumberSum(inputList: list):  # inputList param is of type list
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
    inputList = inputString.split()  # get elements using delimiter ", "
    return inputList  # return the integer array


start_time = time.time()
print("Input Array: %" % twoNumberSum())
print("Time: %f seconds" % (time.time() - start_time))
