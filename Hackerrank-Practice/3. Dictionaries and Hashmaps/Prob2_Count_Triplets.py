import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    #4 2
    #1 2 2 4
    #Sample Output -    #2
    #triplets satisfying our criteria, whose indices are (0,1,3) & (0,2,3)
    triplet = 0
    for t1 in xrange(0, len(arr) - 2):
            a = arr[t1]
            p1 = a * r
            p2 = a * math.pow(r,2)
            #print "\n"
            #print a, p1 , p2
            for t2 in xrange(t1+1, len(arr)-1):
                #print "Entered second loop"
                #print arr[t2]
                if arr[t2] == p1:
                    #print "Second term of GP found = " + str(arr[t2])
                    for t3 in xrange(t2+1, len(arr)):
                        #print "Entered third loop"
                        #print arr[t3]
                        if arr[t3] == p2:
                            #print "Third term of GP found = " + str(arr[t3])
                            #print "GP formed = " + str(arr[t1]) + " " + str(arr[t2]) + " " + str(arr[t3])
                            triplet += 1

    print triplet


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
