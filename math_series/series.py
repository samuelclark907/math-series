#fib function
# the function takes a nth input then outputs the nth number in the fib sequence.

def fibonacci(n):
    if n <= 0:
        return ("error")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


# lucas function
# the function takes a nth input then outputs the nth number in the lucas sequence.

def lucas(n):
    if n == 0:
        return 2
    if n == 1:
        return 1
    else:
        return lucas(n-1)+lucas(n-2)


# sum_series function

def sum_series(a,b,c):
    pass