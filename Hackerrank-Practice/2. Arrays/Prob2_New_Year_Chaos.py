import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q, n):
    bribe = 0
    start_i = 0
    for i in range(len(q)):
        if (q[i]-(i+1) > 2):
            return "Too chaotic"
        if q[i]-2 > 0:
            start_i = q[i]-2
        else: start_i = 0
        for j in range(start_i, i, 1):
            if j<i:
                if q[j] > q[i]:
                    bribe += 1
    return bribe


if __name__ == '__main__':
    print "Enter no of test cases"
    t = int(raw_input())

    for t_itr in xrange(t):
        print "Enter size of queue"
        n = int(raw_input())
        print "Enter queue configuration at present"
        q = map(int, raw_input().rstrip().split())
        print q

        result = minimumBribes(q, n)
        print result
