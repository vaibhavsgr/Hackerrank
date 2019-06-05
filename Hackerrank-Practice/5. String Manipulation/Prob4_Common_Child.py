import math
import os
import random
import re
import sys

# Complete the commonChild function below.
# https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
def commonChild(s1, s2):
    m, n = len(s1), len(s2)
    #print m, n
    prev, cur = [0]*(n+1), [0]*(n+1)
    #print prev, cur
    for i in xrange(1, m+1):
        for j in xrange(1, n+1):
            if s1[i-1] == s2[j-1]:
                #print s1[i-1]
                #print cur, cur[j], prev[j-1]
                cur[j] = 1 + prev[j-1]
            else:
                if cur[j-1] > prev[j]:
                    #print cur[j-1]
                    cur[j] = cur[j-1]
                    #print cur
                else:
                    cur[j] = prev[j]
            print "\n"

        cur, prev = prev, cur
        print "\n"
    return prev[n]

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    print "Enter first string"
    s1 = raw_input()
    print "Enter second string"
    s2 = raw_input()

    result = commonChild(s1, s2)
    #fptr.write(str(result) + '\n')
    #fptr.close()
