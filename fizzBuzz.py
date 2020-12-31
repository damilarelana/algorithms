import random
import time
import secrets
import random
import pdb
import hashlib


# fizzBuzz()
def fizzBuzz(inputInteger):
    for i in range(1, inputInteger + 1, 1):
        if ((i % 3) == 0) and (not((i % 5) == 0)):
            print("Fizz")
        elif (not (i % 3) == 0) and ((i % 5) == 0):
            print("Buzz")
        elif ((i % 3) == 0) and ((i % 5) == 0):
            print("FizzBuzz")
        else:
            print(i)
  
# define getInteger()
def getInteger():
    try:
        inputIntegerString = input("Enter a test Integer value for FizzBuzz: ")
        inputInteger = int(inputIntegerString)  # convert string to integer
        while isinstance(inputInteger, int) is False:
            print("Input must be an integer")
            getInteger() # recursive call
    except ValueError:
        raise Exception("Unable to initialize the user defined test Integer value")
    return inputInteger


def selectInputMethod():
    sampleAnswerList = ["y", "Y", "Yes", "YeS", "YEs", "YES", "yES", "yEs", "yeS", "yes", "n", "N", "no", "nO", "No", "NO"]
    while True:
        selectionAnswer = input("To enter your own test integer value, enter 'Yes', OTHERWISE enter 'No' for default test integer value: ")
        selectionAnswerString = str(selectionAnswer)  # convert input to string
        if (isinstance(selectionAnswerString, str) is True) and ((selectionAnswerString in sampleAnswerList) is True):
            return selectionAnswerString

def getInputData():
    selectionAnswerString = selectInputMethod()
    if selectionAnswerString in ["y", "Y", "Yes", "YeS", "YEs", "YES", "yES", "yEs", "yeS", "yes"]:
        # obtain test array
        testInteger = getInteger()

        return testInteger

    else: # not necessary to test for 'No', but here is the case for default
        testInteger = 10
        return testInteger
    
  
# define main() function
def main():
    testInteger = getInputData()
    print("========================\n")
    start_time = time.time()
    print("For test integer {}, FizzBuzz() instance gives ... ".format(testInteger))
    fizzBuzz(testInteger)
    print("Time: {} seconds".format((time.time() - start_time)))


if __name__ == "__main__":
    main()
