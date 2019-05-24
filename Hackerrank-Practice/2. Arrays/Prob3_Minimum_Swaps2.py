import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    #i   arr                     swap (indices)
    #0   [7, 1, 3, 2, 4, 5, 6]   swap (0,3)
    #1   [2, 1, 3, 7, 4, 5, 6]   swap (0,1)
    #2   [1, 2, 3, 7, 4, 5, 6]   swap (3,4)
    #3   [1, 2, 3, 4, 7, 5, 6]   swap (4,5)
    #4   [1, 2, 3, 4, 5, 7, 6]   swap (5,6)
    #5   [1, 2, 3, 4, 5, 6, 7]#
    swap = 0
    items = 0
    temp = 0
    while items < len(arr):
        if arr[items] != items + 1 :
            temp = arr[arr[items] - 1]
            arr[arr[items] - 1] = arr[items]
            arr[items] = temp
            swap += 1
        else:
            items += 1
    return swap



if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    print "Enter the size of the array"
    n = int(raw_input())
    print "Enter the elements in the array"
    arr = map(int, raw_input().rstrip().split())
    res = minimumSwaps(arr)
    print res
