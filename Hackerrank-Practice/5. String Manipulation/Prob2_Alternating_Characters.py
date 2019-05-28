import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    count = 0
    for index in xrange(len(s)-1):
        if s[index] == s[index+1]:
            count += 1
    return count

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    print "Enter the number of strings"
    q = int(raw_input())
    print "Enter the strings"
    for q_itr in xrange(q):
        s = raw_input()

        result = alternatingCharacters(s)
        print result
    #fptr.write(str(result) + '\n')

    #fptr.close()
