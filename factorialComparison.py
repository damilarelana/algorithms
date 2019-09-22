def recursive_factorial(n):
    if n <= 1 :
        return 1
    else:
        return n*recursive_factorial(n-1)


def iterative_factorial(n):
    if n <= 1:
        return 1
    else:
        count = 1
        tempProduct = n
        while count < n :
            tempProduct = tempProduct*(n-count)
            count += 1
        return tempProduct