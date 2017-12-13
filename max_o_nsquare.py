from random import randint

def getmax():
    a=[randint(0,100) for x in xrange(20)]
    max=0
    for n1 in a:
        if max < n1:
            max=n1

    print a
    print max
