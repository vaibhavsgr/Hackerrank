import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    count = 0
    temp = 0
    print a
    for i in xrange(len(a)):
        for j in xrange(len(a)-1):
            if a[j] > a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
                count += 1
    return count


if __name__ == '__main__':
    print "Enter the length of array"
    n = int(raw_input())
    print "Enter the number in array"
    a = map(int, raw_input().rstrip().split())

    res = countSwaps(a)
    print "Array is sorted in {} swaps".format(res)
    print "First Element: {}".format(a[0])
    print "Last Element: {}".format(a[n-1])
