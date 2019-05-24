#!/bin/python

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    print "Enter the number of queries"
    q = int(raw_input())
    print "Enter the queries now"
    for q_itr in xrange(q):
        s = raw_input()

        result = sherlockAndAnagrams(s)
        print result
        #fptr.write(str(result) + '\n')

    #fptr.close()
