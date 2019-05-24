import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jump = 1
    safe_cloud = True
    for items in c:
        #print items
        if items == 0:
            safe_cloud = True
        elif items == 1 and safe_cloud == True:
            jump += 1
            safe_cloud = False

    return jump

if __name__ == '__main__':
    print "Enter the no of clouds"
    n = int(raw_input())
    print "Enter 0 for safe cloud and 1 for thunderous cloud"
    c = map(int, raw_input().rstrip().split())
    result = jumpingOnClouds(c)
    print result
