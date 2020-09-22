import random
import time
import math
import copy
import secrets
from datetime import datetime
from calendar import monthrange
from calendar import weekday


# define getDate()
# - uses a try-except-finally to catch input edge-cases
# - calls input() to get user defined integer value
# - returns the user defined integer value [when all goes accordingly to plan]


def getDate(inputStringType: string):
    try:
        inputDateString = input("please enter {} in format 2009-12-21:".format(inputStringType))
        inputDate = datetime.strptime(inputDateString,"%Y-%m-%d") # convert string to datetime
        while isinstance(inputDate, datetime.date) is False:
            print("Input must be in expected datetime format")
            inputDateString = input("please enter {} in format 2009-12-21:".format(inputStringType))
            inputDate = datetime.strptime(inputDateString,"%Y-%m-%d")
    except ValueError:
        raise Exception("Unable to initialize the user defined datetime value")
    finally:
        print("Successfully initialized {} value".format(inputStringType))
    return inputDate.year, inputDate.month, inputDate.day


#
# Initialize the date ranges
#
startDateTuple = getDate("Start Date")
startDay = startDateTuple[2]
startMonth = startDateTuple[1]
startYear = startDateTuple[0]

endDateTuple = getDate("End Date")
endDay = endDateTuple[2]
endMonth = endDateTuple[1]
endYear = endDateTuple[0]


#
# initialize Dictionaries
#
monthsList = createList(0, 12, 1) # returns [0,1 ... 11]
yearsList = createList(startYear, endYear+1, 1) # returns [2001, ... , 2100]

#
# listShuffler()
#  - helps to avoid the problem that random.shuffle tends to shuffle in place
#  - copy the inputList around sometimes means references [i.e. the copies] are not copied


def listShuffler(initialList: list):
    workingList = copy.deepcopy(initialList)  # deepcopy that random sample
    randomNumber = secrets.randbits(8192)     # generate random number for random.seed()
    random.seed(randomNumber)     # improve the randomizer by calling random.seed()
    random.shuffle(workingList)  # shuffle the copy of the random sample again just to be sure :)
    # shuffledList = random.sample(workingList, len(workingList))  # take a random sample of list [which returns a shuffled version]

    # return the now shuffled list
    return workingList


#
# createList()
#  - helps to generate a list of integer numbers
#  - starting from listRangeStart
#  - up to but excluding listRangeStop
#  - while taking listRangeStep at a time

def createList(listRangeStart, listRangeStop, listRangeStep):
  createdList = [x for x in range(listRangeStart, listRangeStop, listRangeStep)]  # Generate Random Unsorted List
  createdList = listShuffler(createdList)
  return createdList



#
# indexSplitter()
#   - gives the floor of the division between inputListUpperIndex and inputListLowerIndex (i.e. a // b )
#   - alternative is to give the ceiling
#   - we are instead going with floor so as to more easily control the startIndex for rightSubList 
#           + i.e. if splitIndex = 2 and hence the last index for the leftSubList
#           + then startIndex for rightSubList is splitIndex += 1
#   - def indexSplitter(inputListLowerIndex: int, inputListUpperIndex: int):
#           numerator = inputListLowerIndex + inputListUpperIndex
#           denumerator = 2
#           splitIndex, quotient = divmod(numerator, denumerator)
#           adjustedSplitIndex = value + bool(quotient)
#           return adjustedSplitIndex


def indexSplitter(inputListLowerIndex: int, inputListUpperIndex: int):
    nuMerator = inputListLowerIndex + inputListUpperIndex
    deNumerator = 2
    splitIndex = nuMerator // deNumerator
    return splitIndex

#
# checkOrderedListEquivalence() a brutal bruteforce check for whether two lists are identical
# - in terms of:
#   + types of elements
#   + number of elements
#   + order of elements
# - assumes that the lists `r` and `k` are ordered
# - it however cannot check order of elements: since sets are random
# - it works best if the lists are already consisting of unique elements
#   + hence removal of duplicated elements (during intersection) would not be a problem
# - criteria of equivalence:
#   + len(set(r).intersection(k)) == len(set(k)) [solves for when set(r) is {} but set(k) is not]
#   + len(set(r)) == len(set(k))  [solves for the duplication issue]
#   + r == k [solves for element-wise comparison and order]
#   + len(r) == len(k) [also solves for duplication issues]


def checkOrderedListEquivalence(r: list, k: list):

    # intersection test parameters
    resultSet = set(r).intersection(k)
    rSet = set(r)
    kSet = set(k)
    resultSetLength = len(resultSet)
    rSetLength = len(rSet)
    kSetLength = len(kSet)

    # list test parameters
    rLength = len(r)
    kLength = len(k)

    # Test for equivalence
    if (resultSetLength == kSetLength) and (rSetLength == kSetLength) and (r == k) and (rLength == kLength):
        return True
    return False

#
# calcPercentage()
#
def calcPercentage(validatedWednesdayCounter: float, allWednesdayCounter: float):
  computedPercentage = (validatedWednesdayCounter/allWednesdayCounter) * 100.0
  return computedPercentage


#
# getAllWedInMonth()
#
def getAllWedInMonth(month: int, year: int, monthsDayRangeLimit: int):
  wednesdayPerMonthCounter = 0
  listOfDaysInMonth = createList(1, monthsDayRangeLimit+1, 1) # returns [1 ... 31] e.g. for January
  for day in listOfDaysInMonth:
    weekdayValue = weekday(year, month, day)
    if weekdayValue is 2:
      wednesdayPerMonthCounter += 1
  return wednesdayPerMonthCounter

#
# getWedAtLastDayOfMonth()
#
def getWedAtLastDayOfMonth(month: int, year: int, monthsDayRangeLimit: int):
  wednesdayAtLastDayCounter = 0
  weekdayValue = weekday(year, month, monthsDayRangeLimit)
  if weekdayValue is 2:
    wednesdayAtLastDayCounter += 1
  return wednesdayAtLastDayCounter

#
# getAllWednesdayInPeriod()
#
def getAllWednesdayInPeriod(monthsList: list, yearsList: list):
  
  allWednesdayInPeriodCounter = 0   # Initialize Counter

  for year in yearsList:
    for month in monthsList:
      monthsDayRangeLimitTuple = monthrange(year, month)
      monthsDayRangeLimit = monthsDayRangeLimitTuple[1]
      allWednesdayInPeriodCounter += getAllWedInMonth(month, year, monthsDayRangeLimit)

  return allWednesdayInPeriodCounter


#
# getValidatedWednesdayInPeriod()
#
def getValidatedWednesdayInPeriod(monthsList: list, yearsList: list):
  
  validatedWednesdayInPeriodCounter = 0 # Initialize Counter
  for year in yearsList:
    for month in monthsList:
      monthsDayRangeLimitTuple = monthrange(year, month)
      monthsDayRangeLimit = monthsDayRangeLimitTuple[1]
      validatedWednesdayInPeriodCounter += getWedAtLastDayOfMonth(month, year, monthsDayRangeLimit)
  
  return validatedWednesdayInPeriodCounter

#
# timed runtime
#
startTime = time.time()
validatedWednesdayInPeriodCounter = getValidatedWednesdayInPeriod(monthsList, yearsList)
allWednesdayInPeriodCounter = getAllWednesdayInPeriod(monthsList, yearsList)
computedPercentage = calcPercentage(float(validatedWednesdayInPeriodCounter), float(allWednesdayInPeriodCounter))
stopTime = time.time()
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("")
print("Given the period between:")
print("  - start date {}-{}-{}".format(startYear, startMonth, startDay))
print("  - end date {}-{}-{}".format(endYear, endMonth, endDay))
print("")
print("")
print("it means:")
print("  - there are {} wednesdays overall within that period".format(allWednesdayCounter))
print("  - there are {} wednesdays that fall on the last days of the month".format(validatedWednesdayCounter))
print("  - {:.2%} of those wednesdays fall on the last days of the mont".format(computedPercentage))
print("runtime: %f seconds" % (stopTime - startTime))
print("")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")