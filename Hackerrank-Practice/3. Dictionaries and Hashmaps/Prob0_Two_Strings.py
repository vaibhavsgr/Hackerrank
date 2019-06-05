import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    #s1_list, s2_list = [], []
    #for i in range(len(s2)):
    #    for j in range(i+1, len(s2)+1):
    #        s2_list.append(s2[i:j])
    #for i in range(len(s1)):
    #    for j in range(i+1, len(s1)+1):
    #        s1_list.append(s1[i:j])
    #for subs in s1_list:
    #    if subs in s2_list:
    #        match += 1
    #    else:
    #        pass
    #if match > 0:
    #    return "Yes"
    #else: return "No"
    s1 = set(s1)
    s2 = set(s2)

    return "YES" if s1.intersection(s2) else "NO"

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    print "Enter no of testcases"
    q = int(raw_input())
    print "Enter the set of strings"
    for q_itr in xrange(q):
        s1 = raw_input()
        s2 = raw_input()

        print twoStrings(s1, s2)

        #fptr.write(result + '\n')

    #fptr.close()
