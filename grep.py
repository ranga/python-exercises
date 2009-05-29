def grep(word, filename):
    """Implement unix command grep. The grep command takes a string and a file as arguments and prints all lines in the file which contain the specified string.
    
    $ she.txt
    I'm sure that the shells are seashore shells.
    So if she sells seashells on the seashore,
    The shells that she sells are seashells I'm sure.
    She sells seashells on the seashore;
    
    $ python grep.py sure sht.txt
    The shells that she sells are seashells I'm sure.
    I'm sure that the shells are seashore shells.
    
    """
    lines = open(filename).readlines()
    return [line for line in lines if word in line] 

if __name__=="__main__":
    import sys
    word, filename = sys.argv[1:3]
    print "".join(grep(word, filename))
