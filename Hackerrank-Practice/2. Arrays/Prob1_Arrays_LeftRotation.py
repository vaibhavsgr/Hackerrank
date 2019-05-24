import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    new_a =[]
    for i in xrange(d, len(a)):
        new_a.append(a[i])
    for i in xrange(d):
        new_a.append(a[i])

    return new_a


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    print "Enter the size of the array and the number of rotation to perform "
    nd = raw_input().split()
    n = int(nd[0])
    d = int(nd[1])
    print "Enter n space separated integers"
    a = map(int, raw_input().rstrip().split())

    result = rotLeft(a, d)
    print result
    #fptr.write(' '.join(map(str, result)))
    #fptr.write('\n')
    #fptr.close()
