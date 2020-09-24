import random
import time
import math
import copy
import secrets
from datetime import datetime as dt
import datetime
from calendar import monthrange
from calendar import weekday

#
# formating space
#
print("")

# define getDate()
# - uses a try-except-finally to catch input edge-cases
# - calls input() to get user defined integer value
# - returns the user defined integer value [when all goes accordingly to plan]
def getDate(inputStringType: str):
    try:
        inputDateString = input("enter {} in format 2009-12-21: ".format(inputStringType))
        inputDate = dt.strptime(inputDateString,'%Y-%m-%d') # convert string to datetime
        while isinstance(inputDate, datetime.date) is False:
            print("Input must be in expected datetime format")
            inputDateString = input("please enter {} in format 2009-12-21: ".format(inputStringType))
            inputDate = dt.strptime(inputDateString,'%Y-%m-%d')
    except ValueError:
        raise Exception("Unable to initialize the user defined datetime value")
    finally:
        pass
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
# calcPercentage()
#
def calcPercentage(validatedWednesdayCounter: float, allWednesdayCounter: float):
  computedPercentage = (validatedWednesdayCounter/allWednesdayCounter)
  return computedPercentage


#
# getAllWedInMonth()
#
def getAllWedInMonth(month: int, year: int, monthsDayRangeLimit: int):
  wednesdayPerMonthCounter = 0
  listOfDaysInMonth = createList(1, monthsDayRangeLimit+1, 1) # returns [1 ... 31] e.g. for January
  for day in listOfDaysInMonth:
    weekdayValue = weekday(year, month, day)
    if weekdayValue == 2:
      wednesdayPerMonthCounter += 1
  return wednesdayPerMonthCounter

#
# getWedAtLastDayOfMonth()
#
def getWedAtLastDayOfMonth(month: int, year: int, monthsDayRangeLimit: int):
  wednesdayAtLastDayCounter = 0
  weekdayValue = weekday(year, month, monthsDayRangeLimit)
  if weekdayValue == 2:
    wednesdayAtLastDayCounter += 1
  return wednesdayAtLastDayCounter

#
# getAllWednesdayInPeriod()
#
def getAllWednesdayInPeriod(startYear: int, startMonth: int, endYear: int, endMonth: int):
  allWednesdayInPeriodCounter = 0   # Initialize Counter
  currentMonth = copy.deepcopy(startMonth) # initialize current month counter to start month
  currentYear = copy.deepcopy(startYear)# initialize current year counter to start year

  while (currentYear, currentMonth) <= (endYear, endMonth): # can re-use `startYear` and `startMonth` to replace every instance of `currentMonth` and `currentYear`, other opted otherwise for readability
    monthsDayRangeLimitTuple = monthrange(currentYear, currentMonth) # determine the number of days in current month/year 
    monthsDayRangeLimit = monthsDayRangeLimitTuple[1]
    allWednesdayInPeriodCounter += getAllWedInMonth(currentMonth, currentYear, monthsDayRangeLimit) # get number of Wednesdays in current month/year and add to counter

    if currentMonth == 12: # check if current month is already December, if yes then next month would be in next year
      currentMonth = 1 # reset the currentMonth in the new year
      currentYear += 1 # increment the currentYear i.e. since it is a new year
    else:
      currentMonth += 1 # if currentMonth is not already December, then we can increment and still remain in current year

  return allWednesdayInPeriodCounter


#
# getValidatedWednesdayInPeriod()
#
def getValidatedWednesdayInPeriod(monthsValidationList: list, yearsValidationList: list):
  validatedWednesdayInPeriodCounter = 0 # Initialize Counter
  for year in yearsValidationList:
    for month in monthsValidationList:
      monthsDayRangeLimitTuple = monthrange(year, month)
      monthsDayRangeLimit = monthsDayRangeLimitTuple[1]
      validatedWednesdayInPeriodCounter += getWedAtLastDayOfMonth(month, year, monthsDayRangeLimit)
  
  return validatedWednesdayInPeriodCounter


#
# initialize Validation Lists
#
monthsValidationList = createList(1, 13, 1) # returns [1 ... 12]
yearsValidationList = createList(startYear, endYear+1, 1) # returns [2001, ... , 2100]


#
# timed runtime
#
startTime = time.time()
validatedWednesdayInPeriodCounter = getValidatedWednesdayInPeriod(monthsValidationList, yearsValidationList)
allWednesdayInPeriodCounter = getAllWednesdayInPeriod(startYear, startMonth, endYear, endMonth)
computedPercentage = calcPercentage(float(validatedWednesdayInPeriodCounter), float(allWednesdayInPeriodCounter))
stopTime = time.time()
print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("")
print("Given:")
print("  * start-date: {}-{}-{}".format(startYear, startMonth, startDay))
print("  * end-date: {}-{}-{}".format(endYear, endMonth, endDay))
print("")
print("means:")
print("  - {} wednesdays exist in total within the period of {} years".format(allWednesdayInPeriodCounter, len(yearsValidationList)))
print("  - {} wednesdays fall on the last days of the period's months".format(validatedWednesdayInPeriodCounter))
print("  - {:.5%} of those wednesdays fall on the last days of the mont".format(computedPercentage))
print("")
print("runtime: %f seconds" % (stopTime - startTime))
print("")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")