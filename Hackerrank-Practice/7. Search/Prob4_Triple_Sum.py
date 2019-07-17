import math
import os
import random
import re
import sys

# Complete the triplets function below.
def triplets(a, b, c):
    #triplet pairs cond a<=b, b>=c
    a.sort()
    b.sort()
    c.sort()
    c=0
    for t1 in a:
        for t2 in b:
            if t1<=t2:
                for t3 in c:
                    if t3>=t2:
                        c = c+1
    return c

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    print "Enter the lengths of three arrays"
    lenaLenbLenc = input().split()
    lena = int(lenaLenbLenc[0])
    lenb = int(lenaLenbLenc[1])
    lenc = int(lenaLenbLenc[2])
    print "Enter elements for first array"
    arra = list(map(int, input().rstrip().split()))
    print "Enter elements for second array"
    arrb = list(map(int, input().rstrip().split()))
    print "Enter elements for third array"
    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)
    print ans
    #fptr.write(str(ans) + '\n')
    #fptr.close()
