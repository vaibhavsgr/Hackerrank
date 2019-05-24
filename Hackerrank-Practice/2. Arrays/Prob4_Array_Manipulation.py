import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    #a b k
    #1 5 3
    #4 8 7
    #6 9 1
    #Add the values of  between the indices  and  inclusive:
    #index->	 1 2 3  4  5 6 7 8 9 10
    #	        [0,0,0, 0, 0,0,0,0,0, 0]
    #	        [3,3,3, 3, 3,0,0,0,0, 0]
    #	        [3,3,3,10,10,7,7,7,0, 0]
    #       	[3,3,3,10,10,8,8,8,1, 0]
    #arr = [0 for i in xrange(n)]
    arr = [0] * n
    for items in queries:
        start_i, end_i, summand = items[0], items[1], items[2]
        #for i in xrange(start_i-1, end_i):
        #    arr[i] += summand
        arr[start_i] += summand
        if end_i+1 <= n:
            arr[end_i+1] -= summand
            print arr

    large = arr[0]
    for _ in range(n):
        x = x + arr[_]
        if x >  large:
            large = x

    print large
    return large



if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    print "Enter the size of zero array and no of operations"
    nm = raw_input().split()
    n = int(nm[0])
    m = int(nm[1])
    print "Enter the queries"
    queries = []
    for _ in xrange(m):
        queries.append(map(int, raw_input().rstrip().split()))
    result = arrayManipulation(n, queries)
    print result
    #fptr.write(str(result) + '\n')
    #fptr.close()
