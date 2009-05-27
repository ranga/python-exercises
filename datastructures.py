""" solutions to problems in chapter 2: data structures
"""

def sum(list):
    """compute the sum of all the values in a list.

    >>> sum(["hello", "world"])
    'helloworld'
    >>> sum(["aa", "bb", "cc"])
    'aabbcc'
    >>> sum([1, 2, 3])
    6
    """
    sum = list[0]
    for i in list[1:]:
        sum = sum + i
    return sum


def product(list):
    """compute the product of all values in a list

    >>> product([1, 2, 3])
    6
    """
    prod=1
    for i in list:prod = prod * i
    return prod


def factorial(num):
    """
    To compute factorial of number
    >>> factorial(0)
    1
    >>> factorial(4)
    24
    """
    if num == 0:return 1
    else:return num * factorial(num - 1)


def reverse(list):
    """
    to reverse a list wothout list slicing
    >>> reverse([1, 2, 3, 4])
    [4, 3, 2, 1]
    >>> reverse(reverse([1, 2, 3, 4]))
    [1, 2, 3, 4]
    """

    reversed_list= []
    for i in range(1,len(list)+1):
        x = list[len(list)-i]
        reversed_list.append(x)
    return reversed_list 


def cumulative_sum(list):
    """
    Cumulative sum of a list [a, b, c, ...] is defined as [a, a+b, a+b+c, ...]
    >>> cumulative_sum([1, 2, 3, 4])
    [1, 3, 6, 10]
    >>> cumulative_sum([4, 3, 2, 1])
    [4, 7, 9, 10]
    """
    sum = 0
    cumulativesum = []
    for i in list:
        sum = sum + i
        cumulativesum.append(sum)
    return cumulativesum


def cumulative_product(list):
    """cumulative_product to compute cumulative product of a list of numbers
    >>> cumulative_product([1, 2, 3, 4])
    [1, 2, 6, 24]
    >>> cumulative_product([4, 3, 2, 1])
    [4, 12, 24, 24]
    """
    prod = 1
    cumulativeprod = []
    for i in list:
        prod = prod * i
        cumulativeprod.append(prod)
    return cumulativeprod


def lensort(list):
    """a function lensort to sort a list of strings based on length.
    >>> lensort(['python', 'perl', 'java', 'c', 'haskell', 'lisp', 'ocaml', 'smalltalk', 'ruby'])
    ['c', 'perl', 'java', 'lisp', 'ruby', 'ocaml', 'python', 'haskell', 'smalltalk']
    """
    
    list.sort(lambda x,y:len(x)-len(y))
    return list

def zip(a,b):
    """an implementation for zip function using list comprehensions
    >>> zip([1, 2, 3], ["a", "b", "c"])
    [(1, 'a'), (2, 'b'), (3, 'c')]
    
    """
    return [(a[i], b[i]) for i in range(min(len(a),len(b)))]

def map(fun,list):
    """ an implementation for map using list comprehensions.
    >>> def square(x):
    ...     return x*x
    >>> map(square, [1, 2, 3, 4])
    [1, 4, 9, 16]
    """
    return [fun(item) for item in list]

def myfilter(fun,list):
    """an implementation for filter using list comprehensions.
    >>> def even(num):
    ...     return num %2 == 0
    >>> myfilter(even, range(10))
    [0, 2, 4, 6, 8]
    """
    return [num for num in list if fun(num)]

def triplets(n):
    """Write a function triplets that takes a number n but not represent same triplet like (a, b, c) and (b, a, c) 
    >>> triplets(5)
    [(1, 1, 2), (1, 2, 3), (1, 3, 4), (2, 2, 4)]
    """
    return [(i,j,i+j)for i in range(1,n) for j in range(i,n) if i + j < n ]

def enumerate(list):
    """a function enumerate that takes a list and returns a list of tuples containing (index,item) for each item in the list
    >>> enumerate(["a", "b", "c"])
    [(0, 'a'), (1, 'b'), (2, 'c')]
    >>> for index, value in enumerate(["a", "b", "c"]):
    ...     print index, value
    0 a
    1 b
    2 c
    """
    return[(i,list[i]) for i in range(len(list))]

def valuesort(d):
    """a function valuesort to sort values of a dictionary based on the key
    >>> valuesort({'x': 1, 'y': 2, 'a': 3})
    [3, 1, 2]
    """
    sorted_keys = sorted(d.keys())
    return [d[key] for key in sorted_keys]

def anagrams(list):
    """a program to find anagrams in a given list of words. Two words are called anagrams if one word can be formed by rearranging letters of another. For example 'eat', 'ate' and 'tea' are anagrams.
    >>> anagrams(['eat', 'ate', 'done', 'tea', 'soup', 'node'])
    [['eat', 'ate', 'tea'], ['done', 'node'], ['soup']]
    """
    anag = []
    temp = [[item for item in list if sorted(item) == sorted(word)] for word in list]
    for item in temp:
        if item not in anag:
            anag.append(item)
    return anag    

def invertdict(l):
    """a function invertdict to interchange keys and values in a dictionary. For simplicity, assume that all values are unique
    >>> invertdict({'x': 1, 'y': 2, 'z': 3})
    {1: 'x', 2: 'y', 3: 'z'}
    """
    return dict([(v,k) for k,v in l.items()])


if __name__ == "__main__":       
    import doctest
    doctest.testmod()
