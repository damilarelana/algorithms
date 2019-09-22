import time

start_time = time.time()                    # start time counter
def trianglePrinter():
    n = int(input("How many lines: "))
    for i in range(1, n+1):
        for k in range(i+1):
            tempStar = "* " * k
            print(tempStar)
        print()
    return

trianglePrinter()
print("runtime: %s seconds\n" % (time.time() - start_time))