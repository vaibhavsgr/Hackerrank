import math
import os
import random
import re
import sys
from collections import Counter

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    v = 0
    r1 = Counter(a) - Counter(b)
    r2 = Counter(b) - Counter(a)
    for values in r1.itervalues():
        v += values
    for values in r2.itervalues():
        v += values
    return v

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    print "Enter first string"
    a = raw_input()
    print "Enter second string"
    b = raw_input()
    res = makeAnagram(a, b)
    print res
    #fptr.write(str(res) + '\n')
    #fptr.close()
