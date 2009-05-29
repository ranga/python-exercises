def freq(filename):
#f=open("she.txt","r").read()
    line = open(filename).read()

    d={}

    for char in line:
        if d.has_key(char):
	    d[char] += 1
        else:
            d[char] = 1

#for key, value in d.items():
#    print  repr(key), value


    sorted_freq = sorted(d.items(), cmp = lambda x, y: cmp(y[1], x[1]))
    for key, value in sorted_freq:
        print  repr(key), value

if __name__ == "__main__":
    import sys
    filename = sys.argv[1]
    freq(filename)


