def filereverse(infile,outfile):
    """
    >>> a program reverse.py to print lines of a file in reverse order.
    >>>

    $ cat she.txt
    She sells seashells on the seashore;
    The shells that she sells are seashells I'm sure.
    So if she sells seashells on the seashore,
    I'm sure that the shells are seashore shells.

    $ python reverse.py she.txt hello.txt
    $ cat hello.txt
    I'm sure that the shells are seashore shells.
    So if she sells seashells on the seashore,
    The shells that she sells are seashells I'm sure.
    She sells seashells on the seashore;

    """
    f1=open(outfile ,"w")
    f2=open(infile ,'r')
    lines=f2.readlines()
    for line in lines[::-1]:
	f1.write(line)
    f1.close()
    f2.close()
if __name__ == "__main__":
    import sys
		
    infile =sys.argv[1]
    outfile=sys.argv[2]
    filereverse(infile, outfile)


