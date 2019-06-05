#!/bin/python

import math
import os
import random
import re
import sys
from collections import defaultdict, deque

# Complete the freqQuery function below.
def freqQuery(queries):
    #use Dictionary to store the frequency of each element
    #increase or decrease the frequency as per the operation input
    freq = defaultdict()
    arr = defaultdict()
    out = deque()
    value = 0
    for _ in queries:
        if _[0] == 1:
            try:
                value = arr[_[1]]
                arr[_[1]] = value + 1
            except KeyError:
                arr[_[1]] = value + 1

            if _[1] in freq[value]:
                freq[value + 1].remove(_[1])

            freq[value + 1].add(_[1])

        elif _[0] == 2:
            value = arr[_[1]]

            if value > 0:
                arr[_[1]] = value - 1

                if _[1] in freq[value]:
                    freq[value].remove(_[1])

                freq[value-1].add(_[1])
        else:
            print arr
            print "\n"
            print freq
            print "\n"
            try:
                if freq[_[1]]:
                    out.append(1)
            except KeyError:
                out.append(0)



    return out

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    print "Enter no of operations"
    q = int(raw_input().strip())
    queries = []
    print "Enter {} operations"
    for _ in xrange(q):
        queries.append(map(int, raw_input().rstrip().split()))

    print queries
    ans = freqQuery(queries)
    print ans
    #fptr.write('\n'.join(map(str, ans)))
    #fptr.write('\n')

    #fptr.close()
