def get_algorithm_result(numList):
    numElements = len(numList)
    tempMax = numList[1]
    i = 1
    while i < numElements:
        if tempMax < numList[i]:
            tempMax = numList[i]
        i += 1
    return tempMax

def prime_number(myNum):
    exceptionList = [2, 3]
    if myNum in exceptionList:
        return True
    elif myNum%2 == 0 or myNum%3 == 0:
        return False
    elif myNum == 0 or myNum == 1:
        return False
    return True