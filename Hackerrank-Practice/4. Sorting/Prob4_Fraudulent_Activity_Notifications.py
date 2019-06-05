import math
import os
import random
import re
import sys

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    notice = 0
    median = 0
    for items in xrange(d-1, len(expenditure)-1):
        trail = []
        i = 0
        print items
        while i < d:
            #print i
            trail.append(expenditure[i])
            i += 1
        expenditure.pop(0)

        trail.sort()
        if d / 2 != 0:
            median = trail[d/2]
        else:
            median = (trail[d/2] + trail[(d+1)/2])/2

        if expenditure[d-1] >= 2*median:
            notice += 1
        #print "Trailing data for {}th day = {}".format(items+1, trail)
        #print "Remaining expense = {}".format(expenditure)
        #print "Sorted trail looks like = {}".format(trail)
        #print "Median for {}th day = {}".format(items+1, median)
        #print notice

        #print "\n"
        return notice



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
    #fptr.write(str(result) + '\n')

    #fptr.close()
