import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
        arr_diff = defaultdict(int)
    for items in arr:
        arr_diff[items] = items
    c = 0
    for i in arr:
        f_items = i + k
        if f_items in arr_diff:
            c = c+1
      
    return c


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    print "Enter the size of array and the difference"
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    print "Enter the numbers"
    arr = list(map(int, input().rstrip().split()))
    result = pairs(k, arr)
    print result
    #fptr.write(str(result) + '\n')

    #fptr.close()
