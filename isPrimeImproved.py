#import necessary modules
import random
import math
import time

# get number from user
# testNumber = int(input("Enter a positive number: "))

def isPrime(testNumber):

    # start time counter
    start_time = time.time() 
    
    # set Prime test flag
    primeflag = True
    
    # create factors i.e. x is Prime if no i in [2:sqrt(x)] is factor
    factorList = range(2,int(math.ceil(math.sqrt(testNumber))),1)

    # test if Prime number 
    for i in factorList:
        if testNumber%i == 0:
            primeflag = False
            break
            
    # return False if a factor is found
    if not(primeflag) :
        stop_time = time.time()
        time_estimate = stop_time - start_time
        return False
        
    # return True if no factor is found
    stop_time = time.time()
    time_estimate = stop_time - start_time
    return True


print(isPrime(3424))