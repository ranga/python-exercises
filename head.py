def head(filename):
    """Implement unix commands head. The head commands take a file as argument and prints its first 10 lines of the file respectively.
    $ cat he.txt
    Unix does not distinguish binary files from text 
    files but windows does. On windows 'rb', 'wb', 'ab' 
    should be used to open a binary file in read, write 
    and append mode respectively.
    Easiest way to read contents of a file is by 
    using the read method.
    She sells seashells on the seashore;
    The shells that she sells are seashells I'm sure.
    So if she sells seashells on the seashore,
    I'm sure that the shells are seashore shells.
    Implement unix commands head and tail. The head 
    and tail commands take a file as argument and 
    prints its first and last 10 lines of the file 
    respectively.

    $python head.py he.txt
    Unix does not distinguish binary files from text 
    files but windows does. On windows 'rb', 'wb', 'ab' 
    should be used to open a binary file in read, write 
    and append mode respectively.
    Easiest way to read contents of a file is by 
    using the read method.
    She sells seashells on the seashore;
    the shells that she sells are seashells I'm sure.
    So if she sells seashells on the seashore,
    I'm sure that the shells are seashore shells.


    """

    lines=open(filename).readlines()
    return "".join(lines[:10])

if __name__=="__main__":
    import sys
    filename=sys.argv[1]
    print "".join(head(filename)),

