
import math
import os
import random
import re
import sys
from bisect import insort, bisect_left

def activityNotifications(expenditure, d):
    v = sorted(expenditure[: d])
    print v
    print "\n"
    count = 0
    for i, current in enumerate(expenditure[d:]):
        print "\n"
        print i, current
        de = expenditure[i]
        print de
        if d%2 == 0:
            if current >= v[d//2] + v[d//2-1]:
                count += 1
        elif current >= v[d//2]*2:
                count += 1
        ix = bisect_left(v, de)
        del v[ix]
        insort(v, current)
        print v

    return count

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    print "Enter the no of days and the trailing days to calculate median"
    nd = raw_input().split()
    n = int(nd[0])
    d = int(nd[1])
    print "Enter the expenses for {} days".format(n)
    expenditure = map(int, raw_input().rstrip().split())
    result = activityNotifications(expenditure, d)
    print result
