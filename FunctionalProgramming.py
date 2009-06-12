"""
Chapter 3: Functional Programming
"""
def power(x,n):
    """
    Mathematically we can define power of a number in terms of its smaller power.
    Computes the result of x raised to the power of n.

    >>> power(2, 3)
    8
    >>> power(3, 2)
    9
    >>> power(3,0)
    1
    """
    if n == 0:
        return 1
    else:
        return x * power(x,n-1)


def recursion_power(m,n):
    """
    Number of calls to the above power function is proportional to size of the problem, which is n here. There are some recursive functions where the number of calls grow exponentially with the input size. The former kind of recursion is called linear recursion and the latter tree recursion.
    >>> power(2, 4)
    16
    >>> power(2,2)
    4
    >>> power(2,0)
    1
    """
    if n==0:
        return 1
    elif n%2==0:
        return power(m,n/2)*power(m,n/2)
    else:
        return m*power(m,n-1)


def increment(n): return n + 1
def decrement(n): return n - 1

def add(a, b):
    """
    implement a function add to add 2 numbers recursively using the following increment and decrement functions.
    >>> add(10,5)
    15
    >>> add(-10,6)
    -4
    >>> add (2,-3)
    -1
    >>> add(-2,-1)
    -3

    """
    if b == 0:
        return a
    if a == 0:
        return b
    if a>0 or b<0:
        return add(decrement(a), increment(b))
    else:
        return add(increment(a),decrement(b))


def flatten_list(a):
    """
    Consider the problem where you have a nested list and want to flatten it.
    >>> flatten_list([[1, 2, [3, 4] ], [5, 6], 7])
    [1, 2, 3, 4, 5, 6, 7]
    """
    unflatten_list = []
    for i in a:
        if isinstance(i, list):
            unflatten_list +=flatten_list(i)
        else:
            unflatten_list.append(i)
    return unflatten_list


def flatten_dict(d, p=""):    
    """ 
    Write a function flatten_dict to flatten a nested dictionary by joining the keys with . character.
    >>> flatten_dict({'a': 1, 'b': {'x': 2, 'y': 3}, 'c': 4})
    {'a': 1, 'c': 4, 'b.x': 2, 'b.y': 3}
    """
    flat_dict = {}
    for key in d.keys():
        if isinstance(d[key], dict):
            flat_dict.update(flatten_dict(d[key], p = p + key + "."))
        else:
            flat_dict[p + key] = d[key]
    return flat_dict


def unflatten_dict(d):
    """
    do the reverse of flatten_dict
    >>> unflatten_dict({'a': 1, 'b.x': 2, 'b.y': 3, 'c': 4})
    {'a': 1, 'c': 4, 'b': {'y': 3, 'x': 2}}
    """
    result = {}
    for key in d.keys():
        if "." in key:
            parent, child = key.split(".", 1)
            if parent in result.keys():
                result[parent].update(unflatten_dict({child:d[key]}))
            else:
                result.update({parent: unflatten_dict({child:d[key]})})
        else:
            result.update({key:d[key]})
    return result


def treemap(fun, list_of_args):
    """
    function treemap to map a function over nested list
    >>> treemap(lambda x: x*x, [1, 2, [3, 4, [5] ] ])
    [1, 4, [9, 16, [25]]]

    """
    result = []
    for arg in list_of_args:
        if isinstance(arg, list):
            result.append(treemap(fun, arg))
        else:
            result.append(fun(arg))
    return result


def count_change(amount,coins):
    """
    a function count_change to count the number of ways to change any given amount. Available coins are also passed as argument to the function.

    >>> count_change(10, [1, 5])
    3
    >>> count_change(10, [1, 2])
    6
    >>> count_change(100, [1, 5, 10, 25, 50])
    292

    """
    if amount == 0:
        return 1
    elif amount < 0 or not coins:
        return 0
    else:
        return count_change(amount, coins[1:]) + count_change(amount-coins[0], coins)



if __name__ == "__main__":
    import doctest
    doctest.testmod()
