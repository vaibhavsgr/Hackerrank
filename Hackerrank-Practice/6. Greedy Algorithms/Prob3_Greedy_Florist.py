import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(n, k, c):
    c.sort()
    cost = 0
    for i in xrange(n-k-1, 0, -1):
        cost += c[i] * (((n-i-k)/ k) + 1)
    for i in xrange(n-1, n-k-1, -1):
        cost += c[i]

    print cost

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    print "Enter no of flowers and no of friends"
    nk = raw_input().split()
    n = int(nk[0])
    k = int(nk[1])
    print "Enter the price of {} flowers".format(n)
    c = map(int, raw_input().rstrip().split())
    minimumCost = getMinimumCost(n, k, c)
    print minimumCost
    #fptr.write(str(minimumCost) + '\n')
    #fptr.close()
