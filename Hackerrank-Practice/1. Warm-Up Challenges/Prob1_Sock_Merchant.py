import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    individual_count = 1
    total_count = 0
    ar.sort()
    print ar
    for i in xrange(0, n):
        try:
            if ar[i] == ar[i+1]:
                individual_count += 1
            else:
                print "Count of {} is {}".format(ar[i], individual_count)
                total_count += individual_count / 2
                individual_count = 1
        except IndexError as e:
                print "Count of {} is {}".format(ar[i], individual_count)
                total_count += individual_count / 2
                individual_count = 1

    return total_count


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    print "Enter the size of array"
    n = int(raw_input())
    ar = map(int, raw_input().rstrip().split())
    result = sockMerchant(n, ar)
    print result
