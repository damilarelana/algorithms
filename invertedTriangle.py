import time

start_time = time.time()                    # start time counter
def invertedPrinter():
    n = int(input("How many lines: "))
    for i in range(n, 0, -1):
        spaceDiff = 0
        for j in range(2*i-1, 0, -2):
            tempSpace = " " * spaceDiff
            tempStar = "* " * j
            print(tempSpace+tempStar)
            spaceDiff += 2
        print()
    return
invertedPrinter()
print("runtime: %s seconds\n" % (time.time() - start_time))