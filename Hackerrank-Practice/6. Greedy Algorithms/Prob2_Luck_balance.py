import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the luckBalance function below.
def luckBalance(k, contests):
    contests.sort(reverse=True)
    luck, important = 0, 0
    for _ in contests:
        if _[1] == 0:
            luck += _[0]
        elif important < k:
            luck += _[0]
            important += 1
        else: luck -= _[0]

    return luck


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    print "Enter total no of contests and important contest"
    nk = raw_input().split()
    n = int(nk[0])
    k = int(nk[1])
    contests = []
    for _ in xrange(n):
        contests.append(map(int, raw_input().rstrip().split()))

    result = luckBalance(k, contests)
    print result
    #fptr.write(str(result) + '\n')

    #fptr.close()
