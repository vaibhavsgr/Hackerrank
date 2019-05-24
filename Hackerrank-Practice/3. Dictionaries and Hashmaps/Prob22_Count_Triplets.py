import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the countTriplets function below.
def countTriplets(arr, r):
    #4 2
    #1 2 2 4
    #Sample Output -    #2
    #triplets satisfying our criteria, whose indices are (0,1,3) & (0,2,3)
    m1, m2 = defaultdict(int), defaultdict(int)
    triplets = 0

    for i in reversed(arr):
        if (i * r) in m2:
            triplets += m2[i * r]

        if (i * r) in m1:
            m2[i] += m1[i * r]
            print "Dictionary m2 looks like = " + str(m2)

        m1[i] += 1
        print "Dictionary m1 looks like = " + str(m1)

    print  triplets


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    print "Enter the input size and the common ratio"
    nr = raw_input().rstrip().split()
    n = int(nr[0])
    r = int(nr[1])
    print "Enter the integers"
    arr = map(long, raw_input().rstrip().split())
    ans = countTriplets(arr, r)
    #fptr.write(str(ans) + '\n')
    #fptr.close()
