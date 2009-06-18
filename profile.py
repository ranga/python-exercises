import time

def fib(n):
    if n is 0 or n is 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def profile(f):
    """
    Function profile, which takes a function as argument and returns a new function, which behaves exactly similar to the given function, except that it prints the time consumed in executing it.

    >>> fib = profile(fib)
    >>> fib(20)
    time taken: 0.0626459121704
    10946

    """
    f.times = 0 
    def g(x):
        if f.times is 0:
            time_begin = time.time()
        f.times += 1
        value = f(x)
        f.times -= 1
        if f.times is 0:
            print "time taken:", time.time() - time_begin
        return value
    return g

if __name__ ==  "__main__":
    import doctest
    doctest.testmod()


